import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.bot.api import TelegramAPIServer
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from tgbot.config import load_config, Config
from tgbot.filters.admin import AdminFilter
from tgbot.filters.private_chat import IsPrivate
from tgbot.handlers.user import register_user
from tgbot.infrastructure.database.models.base import DatabaseModel
from tgbot.middlewares.db import DbMiddleware
from tgbot.middlewares.enviroment import EnvironmentMiddleware
from tgbot.middlewares.ignore import IgnoreGroupUpdatesMiddleware
from tgbot.middlewares.throttling import ThrottlingMiddleware
from tgbot.misc.notify_admins import on_startup_notify

logger = logging.getLogger(__name__)


def register_all_middlewares(dp: Dispatcher,
                             config: Config,
                             session_pool: sessionmaker,
                             bot: Bot,
                             scheduler: AsyncIOScheduler):
    dp.setup_middleware(DbMiddleware(session_pool))
    dp.setup_middleware(EnvironmentMiddleware(config=config, bot=bot, dp=dp, scheduler=scheduler))
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(IgnoreGroupUpdatesMiddleware())


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsPrivate)


def register_all_handlers(dp):
    register_user(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    storage = RedisStorage2(host='redis_cache',
                            password=config.misc.redis_password) if config.tg_bot.use_redis else MemoryStorage()

    bot = Bot(token=config.tg_bot.token, parse_mode='HTML', )
    dp = Dispatcher(bot, storage=storage)
    scheduler = AsyncIOScheduler(timezone="UTC")

    bot['config'] = config

    engine = create_async_engine(
        config.db.construct_sqlalchemy_url(),
        query_cache_size=1200,
        pool_size=100,
        max_overflow=200,
        future=True,
        echo=False
    )

    async with engine.begin() as conn:
        # await conn.run_sync(DatabaseModel.metadata.drop_all)
        await conn.run_sync(DatabaseModel.metadata.create_all)

    # noinspection PyTypeChecker
    session_pool = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

    register_all_middlewares(dp, config, session_pool, bot, scheduler)
    register_all_filters(dp)
    register_all_handlers(dp)

    # start
    try:
        await on_startup_notify(bot)
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")

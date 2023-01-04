from dataclasses import dataclass
from pathlib import Path

from environs import Env
from sqlalchemy.engine import URL


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str
    port: int

    def construct_sqlalchemy_url(self, library='asyncpg') -> str:
        return str(URL.create(
            drivername=f"postgresql+{library}",
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database,
        ))


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    use_redis: bool


@dataclass
class Miscellaneous:
    I18N_DOMAIN: str
    LOCALES_DIR: Path
    redis_password: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    misc: Miscellaneous


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            use_redis=env.bool("USE_REDIS"),
        ),
        db=DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASS'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME'),
            port=env.int('DB_PORT'),
        ),
        misc=Miscellaneous(
            I18N_DOMAIN='textbot',
            LOCALES_DIR=Path(__file__).parent / 'locales',
            redis_password=env.str('REDIS_PASSWORD'),
        )
    )

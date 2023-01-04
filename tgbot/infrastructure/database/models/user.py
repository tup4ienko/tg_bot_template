
from sqlalchemy import ForeignKey, BIGINT, Column, VARCHAR, Integer, Text, Index, Boolean, DECIMAL, TIMESTAMP
from sqlalchemy.sql import expression

from tgbot.infrastructure.database.models.base import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(BIGINT, unique=True)
    lang = Column(VARCHAR(200), server_default=expression.null(), nullable=True)
    token = Column(VARCHAR(200), unique=True)
    user_code = Column(VARCHAR(200), unique=True)
    user_web_url = Column(Text, unique=True)
    client_id = Column(Integer, unique=True)
    balance = Column(DECIMAL, default=0)
    referrer_code = Column(
        VARCHAR(250),
        ForeignKey("users.user_code", ondelete="SET NULL", name="FK__users_referrer_code"),
        nullable=True
    )
    is_guest = Column(Boolean, nullable=True)
    client_at = Column(TIMESTAMP(), server_default=expression.null())

    Index('telegram_id_referrer_web_url', telegram_id, user_web_url, unique=True)
    Index('telegram_id_referrer_telegram_code', telegram_id, user_code, unique=True)

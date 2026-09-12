from sqlalchemy.orm import Mapped, mapped_column
from bot.storage.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    discord_id: Mapped[int] = mapped_column()
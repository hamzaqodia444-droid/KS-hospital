from sqlalchemy import Column, Integer, String, Text

from app.database.connection import Base


class Medicine(Base):

    __tablename__ = "medicines"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    name = Column(
        String(150),
        nullable=False,
        unique=True
    )


    description = Column(
        Text,
        nullable=True
    )


    usage = Column(
        Text,
        nullable=True
    )


    side_effects = Column(
        Text,
        nullable=True
    )


    warnings = Column(
        Text,
        nullable=True
    )

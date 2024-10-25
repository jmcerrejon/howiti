from sqlalchemy import JSON, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class QR(Base):
    __tablename__ = "qr"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    qr_info = Column(JSON)

    def __repr__(self):
        return f"QR(id={self.id}, email={self.email}, qr_info={self.qr_info})"

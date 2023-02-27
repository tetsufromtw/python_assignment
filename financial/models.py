from sqlalchemy import Column, Integer, Date, Numeric, String
from .database import Base

"""
    Define Database
"""


class FinancialData(Base):
    __tablename__ = 'financial_data'

    symbol = Column(String, nullable=False, primary_key=True)
    date = Column(Date, nullable=False, primary_key=True)
    open_price = Column(Numeric(10, 2), nullable=True)
    close_price = Column(Numeric(10, 2), nullable=True)
    volume = Column(Integer, nullable=True)

    def date_str(self):
        return str(self.date)

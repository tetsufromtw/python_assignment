from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Union, Optional
from ..database import get_db
from ..schemas import GetFinancialDataResponse, InfoResponse
from .. import crud

router = APIRouter()


@router.get("/api/financial_data", response_model=Union[GetFinancialDataResponse, InfoResponse])
async def get_financial_data(start_date: Optional[str] = None, end_date: Optional[str] = None,
                             symbol: Optional[str] = None, limit: Optional[int] = 5, page: Optional[int] = 1,
                             db: Session = Depends(get_db)):
    try:
        query_info = {"start_date": start_date, "end_date": end_date, "symbol": symbol}
        page_info = {"limit": limit, "page": page}
        items, pagination = crud.get_financial_data(db, query_info=query_info,
                                                    page_info=page_info)

        return GetFinancialDataResponse(data=items, pagination=pagination, info=InfoResponse(error=""))
    except Exception as e:
        return InfoResponse(error=str(e))

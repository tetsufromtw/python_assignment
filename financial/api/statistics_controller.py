from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Union
from ..database import get_db
from ..schemas import GetStatisticsDataResponse, InfoResponse
from .. import crud

router = APIRouter()


@router.get("/api/statistics", response_model=Union[GetStatisticsDataResponse, InfoResponse])
async def get_statistics(start_date: str, end_date: str, symbol: str, db: Session = Depends(get_db)):
    try:
        query_info = {"start_date": start_date, "end_date": end_date, "symbol": symbol}
        statistics = crud.get_statistics(db, query_info)
        return GetStatisticsDataResponse(data=statistics, info=InfoResponse(error=""))
    except Exception as e:
        return InfoResponse(error=str(e))

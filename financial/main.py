from fastapi import FastAPI
from .database import engine
from . import models
from .api.financial_controller import router as financial_router
from .api.statistics_controller import router as statistics_router


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(financial_router)
app.include_router(statistics_router)

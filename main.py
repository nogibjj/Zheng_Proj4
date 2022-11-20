from db import init_db
from fastapi import FastAPI
import uvicorn
from queries import (
    searchAll,
    searchTop100ChineseCompanies,
    searchCountriesByNumberOfTop100Companies,
    searchCountriesRankedByMarketValue,
)

app = FastAPI()


@app.get("/")
async def root():
    init_db()
    return {"message": "Hello"}


@app.get("/query/searchAll")
async def search_all():
    search_result = searchAll()
    return search_result


@app.get("/query/seachChnTop100")
async def search_chn_top100():
    search_result = searchTop100ChineseCompanies()
    return search_result


@app.get("/query/seachCountriesWithMostGiants")
async def search_countries_most_giants():
    search_result = searchCountriesByNumberOfTop100Companies()
    return search_result


@app.get("/query/seachCountriesWithMostMarketValue")
async def search_countries_most_marketvalue():
    search_result = searchCountriesRankedByMarketValue()
    return search_result


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")

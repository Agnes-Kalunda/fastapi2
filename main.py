#Views

import uvicorn
from fastapi import FastAPI
from utils import series_utils
from models import model
import requests


app = FastAPI()

#hardcoded fred_apikey
api_key="644cd67ebf8d504be3973f6b815a4ac9"

@app.get('/')
async def welcome():
    return {"message:""Hi"}

@app.get('/series_id')
async def get_seriesID(series_id:series_id):

    url = "https://api.stlouisfed.org/fred/series/observations"+\
          "?series_id={seriesID}&api_key={api_key}&file_type=json"+\
            "&observation_start={start}&observation_end{end}&units{units}"

    def get_series(self, seriesID, start, end , units):
        url_formatted = self.url.format(
            seriesID=seriesID, start=start, end=end, units=units, key=api_key
        )

        response = requests.get(url_formatted)

        return response
        response = requests.get(url_formatted)

        return response





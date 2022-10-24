import requests
# import pandas as pd 
import json
from models import model




#hardcoded fred_apikey
api_key="644cd67ebf8d504be3973f6b815a4ac9"


    
#interacts with FredAPI
class SeriesID:
    def __init__(self, token =None):
        self.url = "https://api.stlouisfed.org/fred/series/observations"+\
          "?series_id={seriesID}&api_key={api_key}&file_type=json"+\
          "&observation_start={start}&observation_end{end}&units{units}"
    
    def set_token(self, token):
        self.token = token

    def get_series(self, seriesID, start, end , units):
        url_formatted = self.url.format(
            seriesID=seriesID, start=start, end=end, units=units, key=api_key
        )

        response = requests.get(url_formatted)

        return response




    seriesid = SeriesID()
    
    data = seriesid.get_series(
        seriesID = "GDP",
        start ="2010-10-05",
        end ="2020 -12-01",
        units = "pc1"
    )
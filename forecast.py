import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, timezone

url = "https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="YOUR_CITY", key="YOUR_API_KEY")
jsondata = requests.get(url).json()

df = pd.DataFrame(columns=["temperature", "pressure"])
tz = timezone(timedelta(hours=+9), 'JST')

for dat in jsondata["list"]:
    jst = str(datetime.fromtimestamp(dat["dt"], tz))[:-9]
    temperature = dat["main"]["temp"]
    pressure = dat["main"]["pressure"]
    df.loc[jst] = temperature, pressure

df.plot(subplots=True, layout=(2, 1), figsize=(15, 15), grid=True)
plt.show()

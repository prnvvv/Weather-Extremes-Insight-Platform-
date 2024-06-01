import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

def WeatherExtremesForecaster():

    url = "https://www.weather-forecast.com/maps/India"

    Permission = requests.get(url).text

    soup = BeautifulSoup(Permission, "lxml")

    temperaturesList = []
    cityNamesList = []

    cityNames = soup.find_all("a", class_ = "loclink")

    temperatures = soup.find_all("span", class_ = "temp")

    for temperature in temperatures:
        temperaturesList.append(temperature.text)

    for cityName in cityNames[:len(temperaturesList)]:
        cityNamesList.append(cityName.text)

    data = {"City Names": cityNamesList, "Temperatures": temperaturesList}

    sno = np.arange(len(cityNamesList))

    dataSheet = pd.DataFrame(data, index = sno)

    print(dataSheet)

    return dataSheet


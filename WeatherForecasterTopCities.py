import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

def WeatherForecasterTopCities():
    
    url = "https://www.weather-forecast.com/"

    Permission = requests.get(url).text

    soup = BeautifulSoup(Permission, "lxml")

    temperaturesList = []
    cityNamesList = []

    cityNamesDiv = soup.find_all("div", class_ = "relevant-city")
    temperatures = soup.find_all("span", class_ = "temp")

    for cityNameDiv in cityNamesDiv:
        cityNamesList.append(cityNameDiv.find("a").text)
    
    for temperature in temperatures[:len(cityNamesList)]:
        temperaturesList.append(temperature.text)

    data = {"City Names": cityNamesList, "Temperatures": temperaturesList}  

    sno = np.arange(len(cityNamesList))

    dataSheet = pd.DataFrame(data, index = sno)
    
    print(dataSheet)
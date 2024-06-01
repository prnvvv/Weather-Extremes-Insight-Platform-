import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from pychatgpt import Chat

def WeatherForecasterTopCities():
    
    url = "https://www.weather-forecast.com/"

    Permission = requests.get(url).text

    soup = BeautifulSoup(Permission, "lxml")

    presentDay = datetime.datetime.now().strftime("%A")
    dateTime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    temperaturesList = []
    cityNamesList = []

    print()
    print(f"Today is {presentDay}")
    print(dateTime)
    print()
    
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

def WeatherExtremesForecaster():

    url = "https://www.weather-forecast.com/maps/India"

    Permission = requests.get(url).text

    soup = BeautifulSoup(Permission, "lxml")

    presentDay = datetime.datetime.now().strftime("%A")
    dateTime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    print()
    print(f"Today is {presentDay}")
    print(dateTime)
    print()

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

    return dataSheet


def HotCities():

    dataSheet = WeatherExtremesForecaster()

    dataValues = dataSheet.values
    
    cityNamesList = []
    temperaturesList = []

    for i in range(12):
        if (float(dataValues[i][1]) >= 40):
            cityNamesList.append(dataValues[i][0])
            temperaturesList.append(dataValues[i][1])
            temperaturesList = [float(temperature) for temperature in temperaturesList]
            
    hotCitiesData = {"City Names": cityNamesList, "Temperatures": temperaturesList}

    hotCitiesDataFrame = pd.DataFrame(hotCitiesData)

    print(hotCitiesDataFrame)
    print()

    maxTemperature = max(temperaturesList)
    maxTemperaturecityName = cityNamesList[temperaturesList.index(maxTemperature)]

    print(f"The highest temperature is {maxTemperature}°C, recorded in {maxTemperaturecityName}.")
    print()

def ColdCities():

    dataSheet = WeatherExtremesForecaster()

    dataValues = dataSheet.values
    
    cityNamesList = []
    temperatureList = []

    for i in range(12):
        if (float(dataValues[i][1]) <= 20 ):
            cityNamesList.append(dataValues[i][0])
            temperatureList.append(dataValues[i][1])
            temperatureList = [float(temperature) for temperature in temperatureList]
            
    coldCitiesData = {"City Names": cityNamesList, "Temperatures": temperatureList}

    coldCitiesDataFrame = pd.DataFrame(coldCitiesData)

    print(coldCitiesDataFrame)
    print()

    minTemperature = min(temperatureList)
    minTemperaturecityName = cityNamesList[temperatureList.index(minTemperature)]

    print(f"The lowest temperature is {minTemperature}°C, recorded in {minTemperaturecityName}.")
    print()


def BarGraph(cityNamesList, temperatureList):
    
    plt.bar(cityNamesList, temperatureList, color = 'r', width = 0.3)
    plt.title("Coldest Cities")
    plt.xlabel("City Names")
    plt.ylabel("Temperatures")
    plt.xticks(rotation=45)
    plt.tight_layout
    plt.show()

def AnyCityWeatherReport():
    chat = Chat(email="email", password="password") 
    answer, parent_conversation_id, conversation_id = chat.ask("Hello!")

AnyCityWeatherReport()

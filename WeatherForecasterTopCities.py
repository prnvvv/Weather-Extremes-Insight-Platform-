import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from BarGraph import BarGraph

def WeatherForecasterTopCities():
    
    url = "https://www.weather-forecast.com/"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return False

    Permission = response.text

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

    print()

    graphRep = input("Do you want to view the details in graph format?('Y' for yes and 'N' for no)")
    if graphRep.lower() == 'y':
        BarGraph(cityNamesList, temperaturesList, "Temperature of Top Cities")
    elif graphRep.lower() == 'n':
        pass
    else:
        print("Invalid Input")


import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from BarGraph import BarGraph

def WeatherExtremesForecaster():
    url = "https://www.weather-forecast.com/maps/India"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure we got a successful response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return False

    soup = BeautifulSoup(response.text, "lxml")

    temperaturesList = []
    cityNamesList = []

    cityNames = soup.find_all("a", class_="loclink")
    temperatures = soup.find_all("span", class_="temp")

    for temperature in temperatures:
        temp_value = temperature.text.replace('°', '').strip()  # Remove degree symbol and whitespace
        temperaturesList.append(float(temp_value))

    for cityName in cityNames[:len(temperaturesList)]:
        cityNamesList.append(cityName.text)

    if not cityNamesList:
        print("No cities or temperatures found on the page.")
        return False

    data = {"City Names": cityNamesList, "Temperatures": temperaturesList}
    sno = np.arange(len(cityNamesList))
    dataSheet = pd.DataFrame(data, index=sno)

    print(dataSheet)
    print()

    title = "Temperature of Extreme Cities"
    graphRep = input("Do you want to view the details in graph format? ('Y' for yes and 'N' for no): ")
    if graphRep.lower() == 'y':
        BarGraph(cityNamesList, temperaturesList, title)
    elif graphRep.lower() == 'n':
        pass
    else:
        print("Invalid Input")

    return dataSheet



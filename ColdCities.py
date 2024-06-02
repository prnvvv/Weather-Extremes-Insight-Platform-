import pandas as pd
from WeatherExtremesForecaster import WeatherExtremesForecaster
from BarGraph import BarGraph

def ColdCities():

    dataSheet = WeatherExtremesForecaster()

    dataValues = dataSheet.values
    
    cityNamesList = []
    temperaturesList = []

    for i in range(12):
        if (float(dataValues[i][1]) <= 20 ):
            cityNamesList.append(dataValues[i][0])
            temperaturesList.append(dataValues[i][1])
            temperaturesList = [float(temperature) for temperature in temperaturesList]
            
    coldCitiesData = {"City Names": cityNamesList, "Temperatures": temperaturesList}

    coldCitiesDataFrame = pd.DataFrame(coldCitiesData)

    print(coldCitiesDataFrame)
    print()

    minTemperature = min(temperaturesList)
    minTemperaturecityName = cityNamesList[temperaturesList.index(minTemperature)]

    print(f"The lowest temperature is {minTemperature}°C, recorded in {minTemperaturecityName}.")

    print()

    title = "Coldst Cities"
    graphRep = input("Do you want to view the details in graph format?('Y' for yes and 'N' for no) : ")
    if graphRep.lower() == 'y':
        BarGraph(cityNamesList, temperaturesList, title)
    elif graphRep.lower() == 'n':
        pass
    else:
        print("Invalid Input")
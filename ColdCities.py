import pandas as pd
from WeatherExtremesForecaster import WeatherExtremesForecaster

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
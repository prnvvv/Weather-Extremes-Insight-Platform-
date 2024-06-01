import pandas as pd
from WeatherExtremesForecaster import WeatherExtremesForecaster

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

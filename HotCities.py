import pandas as pd
from WeatherExtremesForecaster import WeatherExtremesForecaster
from BarGraph import BarGraph

def HotCities():
    # Instantiate the WeatherExtremesForecaster to get the data
    dataSheet = WeatherExtremesForecaster()
    dataValues = dataSheet.values

    cityNamesList = []
    temperaturesList = []

    # Collect city names and temperatures where the temperature is >= 40°C
    for i in range(12):
        temperature = float(dataValues[i][1])
        if temperature >= 40:
            cityNamesList.append(dataValues[i][0])
            temperaturesList.append(temperature)
    
    # Handle case where no cities meet the criteria
    if not cityNamesList:
        print("No cities with temperatures above or equal to 40°C found.")
        return

    # Create a DataFrame from the collected data
    hotCitiesData = {"City Names": cityNamesList, "Temperatures": temperaturesList}
    hotCitiesDataFrame = pd.DataFrame(hotCitiesData)

    # Print the DataFrame
    print(hotCitiesDataFrame)
    print()

    # Find and print the city with the highest temperature
    maxTemperature = max(temperaturesList)
    maxTemperatureCityName = cityNamesList[temperaturesList.index(maxTemperature)]
    print(f"The highest temperature is {maxTemperature}°C, recorded in {maxTemperatureCityName}.")
    print()

    # Prompt the user to display the data in a graph format
    title = "Hottest Cities"
    graphRep = input("Do you want to view the details in graph format? ('Y' for yes and 'N' for no): ")
    if graphRep.lower() == 'y':
        BarGraph(cityNamesList, temperaturesList, title)
    elif graphRep.lower() == 'n':
        pass
    else:
        print("Invalid Input")



import pandas as pd
from WeatherExtremesForecaster import WeatherExtremesForecaster
from BarGraph import BarGraph

def ColdCities():
    # Instantiate the WeatherExtremesForecaster to get the data
    dataSheet = WeatherExtremesForecaster()
    dataValues = dataSheet.values

    cityNamesList = []
    temperaturesList = []

    # Collect city names and temperatures where the temperature is <= 20°C
    for i in range(12):
        temperature = float(dataValues[i][1])
        if temperature <= 20:
            cityNamesList.append(dataValues[i][0])
            temperaturesList.append(temperature)
            
    # Handle case where no cities meet the criteria
    if not cityNamesList:
        print("No cities with temperatures below or equal to 20°C found.")
        return

    # Create a DataFrame from the collected data
    coldCitiesData = {"City Names": cityNamesList, "Temperatures": temperaturesList}
    coldCitiesDataFrame = pd.DataFrame(coldCitiesData)

    # Print the DataFrame
    print(coldCitiesDataFrame)
    print()

    # Find and print the city with the lowest temperature
    minTemperature = min(temperaturesList)
    minTemperatureCityName = cityNamesList[temperaturesList.index(minTemperature)]
    print(f"The lowest temperature is {minTemperature}°C, recorded in {minTemperatureCityName}.")
    print()

    # Prompt the user to display the data in a graph format
    title = "Coldest Cities"
    graphRep = input("Do you want to view the details in graph format? ('Y' for yes and 'N' for no): ")
    if graphRep.lower() == 'y':
        BarGraph(cityNamesList, temperaturesList, title)
    elif graphRep.lower() == 'n':
        pass
    else:
        print("Invalid Input")



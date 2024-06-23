# Import necessary libraries
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from BarGraph import BarGraph

# Function to fetch and display weather data for top cities
def WeatherForecasterTopCities():
    url = "https://www.weather-forecast.com/"  # URL of the weather forecast website

    # Try to fetch data from the website
    try:
        response = requests.get(url)  # Send a GET request to the URL
        response.raise_for_status()  # Ensure we got a successful response
    except requests.exceptions.RequestException as e:
        # Handle any request exceptions
        print(f"Error fetching data from {url}: {e}")
        return False

    # Parse the response text with BeautifulSoup
    soup = BeautifulSoup(response.text, "lxml")

    # Initialize lists to store city names and temperatures
    temperaturesList = []
    cityNamesList = []

    # Find all relevant city names and temperatures on the page
    cityNamesDiv = soup.find_all("div", class_="relevant-city")
    temperatures = soup.find_all("span", class_="temp")

    # Extract and store city names
    for cityNameDiv in cityNamesDiv:
        cityNamesList.append(cityNameDiv.find("a").text)
    
    # Extract and store temperatures, matching the number of city names
    for temperature in temperatures[:len(cityNamesList)]:
        temp_value = temperature.text.replace('°', '').strip()  # Remove degree symbol and whitespace
        temperaturesList.append(float(temp_value))

    # Check if city names were found, if not, print a message and return False
    if not cityNamesList:
        print("No cities or temperatures found on the page.")
        return False

    # Create a DataFrame with the collected data
    data = {"City Names": cityNamesList, "Temperatures": temperaturesList}
    sno = np.arange(len(cityNamesList))  # Generate an index for the DataFrame
    dataSheet = pd.DataFrame(data, index=sno)

    # Print the DataFrame
    print(dataSheet)
    print()

    # Ask the user if they want to view the data in a graph format
    title = "Temperature of Top Cities"
    graphRep = input("Do you want to view the details in graph format? ('Y' for yes and 'N' for no): ")
    
    # Display the bar graph if user input is 'Y'
    if graphRep.lower() == 'y':
        BarGraph(cityNamesList, temperaturesList, title)
    elif graphRep.lower() == 'n':
        pass
    else:
        # Handle invalid input
        print("Invalid Input")

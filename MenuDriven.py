import time
from WeatherForecasterTopCities import WeatherForecasterTopCities
from WeatherExtremesForecaster import WeatherExtremesForecaster
from HotCities import HotCities
from ColdCities import ColdCities

def main():
    print()
    print("Welcome to the Weather Forecasting Program (India)...")
    print("Thank You www.weather-forecast.com for giving permission for scraping")
    
    while True:
        print()
        print("Options")
        print("1. To view the Temperatures of the Top Cities")
        print("2. To view the Extreme Temperatures recorded")
        print("3. To view the highest recorded Temperatures of the day")
        print("4. To view the lowest recorded Temperatures of the day")
        print("5. To exit")
        print()

        try:
            option = int(input("Enter the desired number as specified from the options: "))
            
            if option == 1:
                WeatherForecasterTopCities()
                print("Waiting for 10 seconds...")
                time.sleep(10)
            elif option == 2:
                WeatherExtremesForecaster()
                print("Waiting for 10 seconds...")
                time.sleep(10)
            elif option == 3:
                HotCities()
                print("Waiting for 10 seconds...")
                time.sleep(10)
            elif option == 4:
                ColdCities()
                print("Waiting for 10 seconds...")
                time.sleep(10)
            elif option == 5:
                print("Exiting...")
                time.sleep(10)
                break
            else:
                print("Invalid Input")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()

# Import necessary libraries and functions
import time
from WeatherForecasterTopCities import WeatherForecasterTopCities
from WeatherExtremesForecaster import WeatherExtremesForecaster
from HotCities import HotCities
from ColdCities import ColdCities

# Main function to run the weather forecasting program
def main():
    # Welcome message and acknowledgment of the data source
    print()
    print("Welcome to the Weather Forecasting Program (India)...")
    print("Thank You www.weather-forecast.com for giving permission for scraping")
    
    # Infinite loop to keep the program running until the user chooses to exit
    while True:
        # Display options to the user
        print()
        print("Options")
        print("1. To view the Temperatures of the Top Cities")
        print("2. To view the Extreme Temperatures recorded")
        print("3. To view the highest recorded Temperatures of the day")
        print("4. To view the lowest recorded Temperatures of the day")
        print("5. To exit")
        print()

        try:
            # Get the user's choice
            option = int(input("Enter the desired number as specified from the options: "))
            
            # Call the corresponding function based on user's choice
            if option == 1:
                WeatherForecasterTopCities()  # View temperatures of top cities
                print("Waiting for 10 seconds...")
                time.sleep(10)  # Wait for 10 seconds before continuing
            elif option == 2:
                WeatherExtremesForecaster()  # View extreme temperatures recorded
                print("Waiting for 10 seconds...")
                time.sleep(10)  # Wait for 10 seconds before continuing
            elif option == 3:
                HotCities()  # View highest recorded temperatures of the day
                print("Waiting for 10 seconds...")
                time.sleep(10)  # Wait for 10 seconds before continuing
            elif option == 4:
                ColdCities()  # View lowest recorded temperatures of the day
                print("Waiting for 10 seconds...")
                time.sleep(10)  # Wait for 10 seconds before continuing
            elif option == 5:
                # Exit the program
                print("Exiting...")
                time.sleep(10)  # Wait for 10 seconds before exiting
                break
            else:
                # Handle invalid input
                print("Invalid Input")
        except ValueError:
            # Handle non-integer input
            print("Please enter a valid number.")

# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()

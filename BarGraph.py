import matplotlib.pyplot as plt

def BarGraph(cityNamesList, temperatureList, title):
    # Remove degree symbol and convert temperatures to float
    temperatureList = [float(temp.replace('°', '').strip()) for temp in temperatureList]

    # Set the figure size
    plt.figure(figsize=(10, 6)) 
    
    # Create bar graph
    plt.bar(cityNamesList, temperatureList, color='r', width=0.3)
    
    # Add title and labels
    plt.title(title)
    plt.xlabel("City Names")
    plt.ylabel("Temperatures")
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Adjust layout to prevent clipping of tick-labels
    plt.tight_layout()
    
    # Show the graph
    plt.show()


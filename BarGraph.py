import matplotlib.pyplot as plt

def BarGraph(cityNamesList, temperatureList):
    
    plt.bar(cityNamesList, temperatureList, color = 'r', width = 0.3)
    plt.title("Coldest Cities")
    plt.xlabel("City Names")
    plt.ylabel("Temperatures")
    plt.xticks(rotation=45)
    plt.tight_layout
    plt.show()
import matplotlib.pyplot as plt

def BarGraph(cityNamesList, temperatureList, title):
    
    plt.bar(cityNamesList, temperatureList, color = 'r', width = 0.3)
    plt.title(title)
    plt.xlabel("City Names")
    plt.ylabel("Temperatures")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
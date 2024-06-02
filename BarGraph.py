import matplotlib.pyplot as plt

def BarGraph(cityNamesList, temperatureList, title):

    temperatureList = [float(temp.replace('°', '').strip()) for temp in temperatureList]

    plt.figure(figsize=(10, 6)) 
    
    plt.bar(cityNamesList, temperatureList, color = 'r', width = 0.3)
    plt.title(title)
    plt.xlabel("City Names")
    plt.ylabel("Temperatures")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()
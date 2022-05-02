# import csv
#
import pandas

if __name__ == "__main__":
    data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    info_squirrel = {
        'Fur Color': ['grey', 'red', 'black'],
        'Count': []
    }
    gray = data[data["Primary Fur Color"] == "Gray"]
    black = data[data["Primary Fur Color"] == "Black"]
    red = data[data["Primary Fur Color"] == "Cinnamon"]
    info_squirrel['Count'] = [gray.X.count(), red.X.count(), black.X.count()]
    data_squirrel = pandas.DataFrame(info_squirrel)
    data_squirrel.to_csv('squirrel_count.csv')


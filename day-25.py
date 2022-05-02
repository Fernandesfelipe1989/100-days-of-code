# import csv
#
import pandas

if __name__ == "__main__":
    data = pandas.read_csv("weather_data.csv")
    print(data)
    data_dict = data.to_dict()
    print(data_dict)
    temperature_column = data['temp'].to_list()
    print(temperature_column)
    avg = sum(temperature_column) / len(temperature_column)
    print(f"{avg:.1f}")
    print(data['temp'].max())

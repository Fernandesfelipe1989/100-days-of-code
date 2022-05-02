# import csv
#
import pandas

if __name__ == "__main__":
    data = pandas.read_csv("weather_data.csv")
    # print(data)
    # data_dict = data.to_dict()
    # print(data_dict)
    temperature_column = data['temp'].to_list()
    # print(temperature_column)
    # avg = sum(temperature_column) / len(temperature_column)
    # print(f"{avg:.1f}")
    # print(data['temp'].max())
    # print(data[data.day == "Monday"])
    # print(data[data.temp == data.temp.max()])
    # monday = data[data.day == "Monday"]
    # monday_temp = int(monday.temp)
    # monday_temp_f = monday_temp * 9/5 + 32
    # print(monday_temp_f)
    data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }
    data_frame = pandas.DataFrame(data_dict)
    data_frame.to_csv("new_data.csv")

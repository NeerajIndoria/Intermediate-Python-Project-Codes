# import csv
#
# with open("weather_data.csv") as df:
#     temperatures = []
#     data = csv.reader(df)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data['temp'])

# temp_list = data['temp'].to_list()
# print(temp_list)
#
# ave = sum(temp_list) / len(temp_list)
# max_temp = data['temp'].max()
# print(ave)
# print(list_max)

# row_max_temp = data[data.temp == max_temp]
# print(row_max_temp)

# monday = data[data.day == 'Monday']
# print(monday)
# fah = (monday.temp * 9/5) + 32
#
# print(monday.temp, "F")
# print(fah, "F")

data = pandas.read_csv("2018_Squirrel_Data.csv")
grey_Squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
Black_Squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
Cinnamon_Squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# print(grey_Squirrel_count)
# print(Black_Squirrel_count)
# print(Cinnamon_Squirrel_count)

data_dict = {
    "Fur Color": ['Gray', 'Cinnamon', 'Black'],
    "Count": [grey_Squirrel_count, Cinnamon_Squirrel_count, Black_Squirrel_count]
}
print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")

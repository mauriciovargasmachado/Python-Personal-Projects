# with open("weather_data.csv") as data:
#     new_data = data.readlines()
#     print(new_data)

# import csv

# with open("weather_data.csv") as data:
#     new_data = csv.reader(data)
#     temperatures =[]
#     for i in new_data:
#         if i[1] != "temp":
#             temperatures.append(int(i[1]))
#     print(temperatures)


# import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# print(data["temp"])


import pandas

data = pandas.read_csv("weather_data.csv")

data_to_dict =data.to_dict()

print(data_to_dict)

temp_list =data["temp"].to_list()

print(temp_list)

average = sum(temp_list)/len(temp_list)

print(average)

print(data["temp"].mean())

print(data["temp"].max())

print(data[data.day == "Monday"])

print(data.temp.max())

monday = data[data.day == "Monday"]
import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squireels_count= len(data[data["Primary Fur Color"] == "Gray"])
red_squireels_count= len(data[data["Primary Fur Color"] == "Red"])
black_squireels_count= len(data[data["Primary Fur Color"] == "Black"])

data_color_dict = {
   "Fur_color":["Gray","Red","Black"],
    "Count":[gray_squireels_count,red_squireels_count,black_squireels_count]
}

new_data = pandas.DataFrame(data_color_dict)

new_data.to_csv("Squirrel_Color_Census.csv")
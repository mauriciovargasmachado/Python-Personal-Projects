import pandas

data_dict ={
    "students":["Daniel", "Amy", "James", "Angela"],
    "scores": [11,30,24,10]
}

data = pandas.DataFrame(data_dict)
# print(data)
data.to_csv("new_data_file.csv")
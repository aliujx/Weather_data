import csv

#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperature = []
#    for row in data:
#        if row[1] != "temp":
#            temperature.append(int(row[1]))
#        print(row)
#    print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
#print(data)
#print(data["temp"])
data_dict = data.to_dict()
#print(data_dict)
data_temp = data.temp.tolist()
#print(round(sum(data_temp) / len(data_temp)))
#print(data.temp.mean())
#print(data.temp.max())
#print(data[data.day =="Monday"])
##print(data[data.temp == data.temp.max()])
#monday = data[data.day == "Monday"]
#print(monday.condition)
#fahrenheit = monday.temp * 1.8 + 32
#print(fahrenheit)
#data_dict = {
#    "students": ["Amy", "James", "Angela"],
#    "scores": [76, 56, 65]
#}
#dd = pandas.DataFrame(data_dict)
#print(dd)
#dd.to_csv("new_data.csv")
squirres_data = pandas.read_csv("/Users/aliuj/Downloads/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = squirres_data["Primary Fur Color"]
num_gray = squirres_data["Primary Fur Color"] == "Gray"
print(num_gray)
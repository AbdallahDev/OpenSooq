# with open("weather_data.csv") as file:
#     lines = file.readlines()
#
# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     data = list(data)
#     temps = []
#     for index in range(1, len(data)):
#         temps.append(int(data[index][1]))
#
# print(temps)

import pandas
import openpyxl

data = pandas.read_csv("weather_data.csv")
# writer = pandas.ExcelWriter('converted-to-excel.xlsx')
#
# data.to_excel(writer)
# writer.save()
# print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
print(monday.temp)
f_temp = ((monday.temp) * 9 / 5) + 32

print(f_temp)

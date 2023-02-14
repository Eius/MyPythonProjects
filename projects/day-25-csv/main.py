import pandas

data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# print(data["temp"].mean())
# print(data.temp.mean())

# Get data in row
# print(data[data.temp == data.temp.max()])

# Convert C to F
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday.temp * 1.8 + 32
# print(monday_temp_F)

# Create DataFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
#
# print(data.to_csv("new_data.csv"))
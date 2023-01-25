import pandas

data = pandas.read_csv("squirrel_data.csv")
fur_colors = data["Primary Fur Color"]
gray_squirrels_count = len(data[fur_colors == "Gray"])
cinnamon_squirrels_count = len(data[fur_colors == "Cinnamon"])
black_squirrels_count = len(data[fur_colors == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

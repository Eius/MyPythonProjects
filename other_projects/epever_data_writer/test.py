import sqlite3

c = sqlite3.connect("epever_logs.db")
cursor = c.cursor()

querry = "SELECT solar_voltage FROM epever_data WHERE id > 0"
cursor.execute(querry)

rows = cursor.fetchall()
voltages = [float(row[0]) for row in rows]
print(voltages)

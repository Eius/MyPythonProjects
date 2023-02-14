import pandas

student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.score)

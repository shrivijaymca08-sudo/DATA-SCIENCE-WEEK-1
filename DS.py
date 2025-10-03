import pandas as da
import matplotlib.pyplot as data
dr = da.read_csv('gender_submission.csv')
print(dr)
Total_Pass = dr["Survived"].value_counts()
total = len(dr)
a = Total_Pass[0]
perc = (a / total) * 100
print(f"Percentage of non-survivors is: {perc:.2f}%")
Total_Pass.plot(kind = 'bar',color = ["red","purple"])
data.xlabel("Survived people")
data.ylabel("Non-Survived people")
data.title("Survived passenger in the flight")
data.xticks(rotation = 0)
data.yticks(rotation =24)
data.show()

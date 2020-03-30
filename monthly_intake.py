import csv
import matplotlib.pyplot as plt
from collections import Counter

# month
file = open('data/shelter_intakes_outcomes_monthly_intake.csv')
read_file = csv.reader(file)
next(file, None)

month = []

for row in file:
    month.append(row)

counts = Counter(month[:-1])
plt.pie(counts.values(), labels=counts.keys(), autopct='%1.1f%%')
plt.axis('equal')
plt.show()

# weekday
file = open('data/shelter_intakes_outcomes_weekday_intake.csv')
read_file = csv.reader(file)
next(file, None)

day = []

for row in file:
    day.append(row)

counts = Counter(day[:-1])
plt.pie(counts.values(), labels=counts.keys(), autopct='%1.1f%%')
plt.axis('equal')
plt.show()

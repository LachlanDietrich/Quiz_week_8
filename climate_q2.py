import matplotlib.pyplot as plt
import pandas as pd

years = []
co2 = []
temp = []

usecols = ["Year", "CO2", "Temperature"]
df = pd.read_csv('climate.csv', index_col='Year', usecols=usecols)     #   load .csv data
df.head()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.show()
plt.savefig("co2_temp_2.png")


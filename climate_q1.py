import sqlite3
import matplotlib.pyplot as plt
        
years = []
co2 = []
temp = []

connection = sqlite3.connect(r'C:\Users\lachl\Desktop\Quiz_week_8\climate.db')
cursor = connection.cursor()                #   cursor oject required for db access
cursor.execute("select * from ClimateData") #   fetching all values from ClimateData table
print("fetchall:")
result = cursor.fetchall()                  #   query rows returned as list
for r in result:
    print(r)                                #   printing list to the commandline

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
plt.savefig("co2_temp_1.png") 

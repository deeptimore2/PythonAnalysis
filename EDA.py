import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print("----------------------------------------------------------------------------------------")
print("\t\t Basic Analysis with graphs of WOWOCommerce Product Data\t\t")
print("---------------------------------------------------------------------------------------")

# 1.Read CSV File
df = pd.read_csv("./data/woocommerce-product-export.csv")

# 2.Show a concise summary of the columns.
print(df.info())

# 3.Summary of statistics pertaining to the column data 
print(df.describe(include="all"))

# 4/5.Show first 5 rows and last 5 rows
print(df.head(5))
print(df.tail(5))

# 6.Print  the "total_profit" and “month_number” columns only.
print(df[["total_profit","month_number"]])

# 7. Read the total profit of all months and show it using the Bar plot. 
plt.bar(df["month_number"], df["total_profit"])
plt.xlabel("Month number")
plt.ylabel("Total profit")
plt.title("Company profit per month")
plt.yticks(range(0,600000,100000))
plt.grid(linestyle="--")
plt.show()

#8.Read the total profit of all of the months, and show the line plot with the following style properties:
# Create a plot style dictionary
plt.figsize=(20,10)
plot_style = {
    "linestyle": "--",
    "color" : "red",
    "linewidth":3,
    "marker":"o",
    "markersize":6,
    "markerfacecolor":"black",
    "label":"Profit data of last year"
}
plt.xlabel("Month Number")
plt.ylabel("Total profit")
plt.title("Company profit per month")
plt.plot(df["month_number"], df["total_profit"], **plot_style)
plt.xticks(df["month_number"])
plt.yticks(range(0,600000,100000))
plt.legend(loc="lower right")
plt.show()

# 9.Print all of the product sales data and show it using a multi-line plot.

plt.plot(df["month_number"],df["facecream"],marker="o",label="Face Cream Sales Data")
plt.plot(df["month_number"],df["facewash"],marker="o",label="Face Wash Sales Data")
plt.plot(df["month_number"],df["toothpaste"],marker="o",label="Toothpaste Sales Data")
plt.plot(df["month_number"],df["bathingsoap"],marker="o",label="Bathingsoap Sales Data")
plt.plot(df["month_number"],df["shampoo"],marker="o",label="Shampoo Sales Data")
plt.plot(df["month_number"],df["moisturizer"],marker="o",label="Moisturizer Sales Data")
plt.xticks(df["month_number"])
plt.title("Sales Data")
plt.xlabel("Month Number")
plt.ylabel("Sales units in Number")
plt.legend()
plt.show()

# 10.Read “bathingsoap” sales data for each month and show it using a scatter plot

plt.scatter(df["month_number"],df["bathingsoap"],label="bathing Soap Sales data")
plt.grid(linestyle="--")
plt.xticks(df["month_number"])
plt.title("Bathing Soap Sales Data")
plt.xlabel("Month Number")
plt.ylabel("Number of units Sold")
plt.legend()
plt.show()

print("----------------------------------------------------------------------------------------")
print("--------------------------------SECTION TWO---------------------------------------------")

#1.Create a line chart
'''
Given Dataset
date=["25/12","26/12","27/12"]
temp=[8.5,10.5,6.8]

Must include the following properties: 
X label name = Date
Y label name = temperature
Title = Date-wise Temperature
'''
date=["25/12","26/12","27/12"]
temp=[8.5,10.5,6.8]
plt.plot(date,temp)
plt.xlabel("Date")
plt.ylabel("temperature")
plt.title("Date-wise Temperature")
plt.show()

#2.Create a line or any chart using following dataset
'''
Given Dataset:
height=[121.9,124.5,129.5,134.6,139.7,147.3,152.4,157.5,162.6]
weight=[19.7,21.3,23.5,25.9,28.5,32.1,35.7,39.6,43.2]

Show the average weight against the average height 

Style properties:
The line style should be dash-dot and the line color should be green.
Show the legend at the lower-right location.
X label name = Weight in kg.
Y label name = Height in cm.
Title = Average weight with respect to average height.
Add a circle marker: marker size = 10; circle marker color = green.

'''
height=[121.9,124.5,129.5,134.6,139.7,147.3,152.4,157.5,162.6]
weight=[19.7,21.3,23.5,25.9,28.5,32.1,35.7,39.6,43.2]
pStyle={
    "linestyle":"-.",
    "color": "green",
    "marker": "o",
    "markersize": 10,
    "markerfacecolor": "green"
}
plt.plot(weight,height,**pStyle)
plt.title("Average weight with respect to average height.")
plt.xlabel("Weight in Kg")
plt.ylabel("Height in cm")
plt.legend(loc="lower right")
plt.show()
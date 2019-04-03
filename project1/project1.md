

# Project 1 - Exploring Weather Trends

### **Extract the data**

I worte a SQL query like below to extract the data I want

```SQL
SELECT city_data.year, city_data.avg_temp AS "South Korea temp", global_data.avg_temp AS "Global temp"
FROM city_data INNER JOIN global_data
ON city_data.year = global_data.year
WHERE country = 'South Korea';
```



### Open up the CSV and Create a line chart

I downloaded CSV file evaluted by SQL above. And I created a line chart that compares my city's temperature (Seoul) with the global temperature	using the ***moving average***. I used the python library to calculate moving average and create line chart with local and global temperature trends. Below is the full python code that I made. I just used the ***class*** object in case of general cases.

```python
import pandas as pd
import matplotlib.pyplot as plt

class ExploreWeather():
    def __init__(self, csvFile, movingAverage, TITLE, MY_COUNTRY_NAME, GLOBAL_NAME, X_LABEL, Y_LABEL):
        self.df = pd.read_csv(csvFile)
        self.movingAverage = movingAverage
        self.TITLE = TITLE
        self.MY_COUNTRY_NAME = MY_COUNTRY_NAME
        self.GLOBAL_NAME = GLOBAL_NAME
        self.X_LABEL = X_LABEL
        self.Y_LABEL = Y_LABEL

    # set dataFrame by 'year' index
    def set_df_index(self, df, index):
        return df.set_index(index)

    def make_moving_average(self, df):
        return df.rolling(window = self.movingAverage).mean()

    def plot_chart(self, myCountryTempDF, globalTempDF):
        plt.plot(myCountryTempDF, label = self.MY_COUNTRY_NAME)
        plt.plot(globalTempDF, label = self.GLOBAL_NAME)
        plt.title(self.TITLE)
        plt.xlabel(self.X_LABEL)
        plt.ylabel(self.Y_LABEL)
        plt.legend(loc='upper left')
        plt.show()


if __name__ == '__main__':
    # input data that you want
    csvFile = 'results.csv'
    movingAverage = 10
    title, myCountryName, globalName = 'Explore Weather Trends', 'South Korea', 'Global'
    x_label, y_label = 'Year', 'Moving Average Temperatue (mv = ' + str(movingAverage) + ')'
    
    # make instance
    exploreWeather = ExploreWeather(csvFile, movingAverage, title, myCountryName, globalName, x_label, y_label)
    
    # set index and make moving average
    df = exploreWeather.set_df_index(exploreWeather.df, 'year')
    df = exploreWeather.make_moving_average(df)
    
    # plot chart
    exploreWeather.plot_chart(df['South Korea temp'], df['Global temp'])
```



### Make observations

![Figure_1](C:\Users\weroo\Desktop\KIworkshop\DAND\project1\Figure_1.png)



This is a line chart comparing my city's average temperature and global average temperature.

- Is your city hotter or cooler on average compared to the global average? Has the difference been consistent over time?

  **My city (Seoul) is hotter than the global average. And the difference has been almost consistent.**

  

- How do the changes in your city’s temperatures over time compare to the changes in the global average?

  **My city (Seoul) temperature has risen gradually like the global average.**

  

- What does the overall trend look like? Is the world getting hotter or cooler? Has the trend been consistent over the last few hundred years?

  **Overall, it's getting hotter. This trend is getting faster than the last few hundred years , especially for my city.**

  

- What does it happen to your city based on this trend.
  **Seoul has been industrialized rapidly since 1980. Therefore, it's been getting hotter rapidly since 1980.**

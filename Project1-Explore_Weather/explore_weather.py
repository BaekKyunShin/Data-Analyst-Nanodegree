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


plt.scatter(data = df, x = 'num_var1', y = 'num_var2', s = 'num_var3')
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

print("Current working directory:", os.getcwd())


df = pd.read_csv('gld_price.csv')




print("head of data:-\n",df.head())
print("info of data:-",df.tail())
print(df.describe())



plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['GLD'], label='Gold Price', color='gold')

plt.title('Gold Price Over Time')
plt.xlabel('Date')
plt.ylabel('GLD Price')
plt.legend()

# 🟢 Limit how many date ticks are shown
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))  # every 3 months
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # e.g. Jan 2020

plt.gcf().autofmt_xdate()  # rotates labels nicely
plt.tight_layout()
plt.show()

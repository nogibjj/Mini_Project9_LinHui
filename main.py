import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('AAPL.csv', index_col = 0)\
    .fillna(method = 'backfill')
print(df.head())

summary_stats = pd.concat([df.describe(include='all').drop('count').T, \
                           df.median().rename('median')], axis=1).T.round(decimals=2)
print(summary_stats)

plt.plot(df['Open'])
plt.xticks(df.index[::40], rotation=20)
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.title('Open price for AAPL in the past year')
#plt.savefig('Open price figure.png')
plt.show()

average_close = df['Close'].mean()
print(f"Average Closing Price: {average_close}")

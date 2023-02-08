import numpy as np

stock_price = [23.5, 24.1, 22.7, 24.2, 25.2, 28.4, 27.8, 26.5, 27.5, 28.2]

mean_stock_price = np.mean(stock_price)
print("Mean stock price:", mean_stock_price)

greater_than_25 = [price for price in stock_price if price > 25]
count = len(greater_than_25)
print("Number of times stock price was greater than 25:", count)

daily_return = [(today - yesterday) / yesterday * 100 for yesterday, today in zip(stock_price[:-1], stock_price[1:])]
print("Daily rate of return:", daily_return)

up_or_down_3 = [return_ for return_ in daily_return if abs(return_) >= 3]
count = len(up_or_down_3)
print("Number of days with price up or down 3%:", count)

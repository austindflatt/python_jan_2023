sales = {'Jan': 150, 'Feb':200, 'Mar': 175, 'April': 75, 'May': 80, 'Jun': 300, 'July': 250, 'August':130, 'September': 195, 'October': 75, 'November': 120, 'December': 400}

months = []
high_sales = []
low_sales = []

for month, sales_amount in sales.items():
    if sales_amount >= 150:
        months.append(month)
    if sales_amount >= 300:
        high_sales.append((month, sales_amount))

months_list = list(sales.keys())
for i in range(len(months_list) - 2):
    total_sales = sum([sales[months_list[j]] for j in range(i, i+3)])
    if total_sales < 500:
        low_sales.append((months_list[i], months_list[i+1], months_list[i+2], total_sales))

print("Months with sales greater than or equal to 150:", months)
print("Tuple of all months and sales amounts greater than or equal to 300:", high_sales)
print("3 consecutive month periods where sales are below 500:", low_sales)

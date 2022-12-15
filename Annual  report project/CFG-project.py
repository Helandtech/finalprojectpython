#Annual Financial Report
import pandas as pd
import csv
import operator




def sales():
    with open('sales.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
#sales()


def read_data():
    data = []
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)

    return data

def run():
    data = read_data()

    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

    print('Sales:', sales)

#run()



def salespermonth():
    with open('sales.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            month_sales = row[1] + "    " + row[2]
            print(month_sales)
#salespermonth()


def calculation():
    df = pd.read_csv(r'sales.csv')

    # average
    mean1 = df['sales'].mean()
    mean2 = df['expenditure'].mean()

    # percentage change
    sales_pct_change = df['sales'].pct_change()
    exp_pct_change = df['expenditure'].pct_change()

    print(mean1)
    print(mean2)
    print(sales_pct_change)
    print(exp_pct_change)
#calculation()


def high_low_months():
    with open("sales.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    monthly_sales = {}

    for row in data:
        month = row["month"]
        sales = float(row["sales"])
        if month in monthly_sales:
            monthly_sales[month] += sales
        else:
            monthly_sales[month] = sales

    sorted_sales = sorted(monthly_sales.items(), key=operator.itemgetter(1), reverse=True)

    print("The month with the highest sales is", sorted_sales[0][0])
    print("The month with the lowest sales is", sorted_sales[-1][0])

#high_low_months()
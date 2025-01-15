import csv
import datetime

# Get current date, month, and year
d = datetime.datetime.now()
current_date = d.strftime("%d")
current_month = d.strftime("%m")
current_year = d.strftime("%y")

def day_sale():
    print('Enter date:')
    date = input()
    print('Enter month:')
    month = input()
    print('Enter Year:')
    year = input()
    count = 0.0

    with open('sales.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        print("------------Day's Sales------------")
        for r in reader:
            if r['sale_date'] == date and r['sale_month'] == month and r['sale_year'] == year:
                count += float(r['total'])
                print('Medicine Name :', r['medi_name'])  # Corrected key
                print('Medicine ID :', r['med_id'])      # Corrected key
                print('SALE :', r['sale'])              # Matches your header
                print('Quantity :', r['quantity'])      # Corrected key
                print('Total:', r['total'])             # Matches your header
                print('\n')
        print("====================================")
        print("Total sale for the day:", count)
        print("===============================")


def month_sale():
    print('Enter month:')
    month = input()
    print('Enter Year:')
    year = input()
    count = 0.0

    with open('sales.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        print("------------Month's Sales------------")
        for r in reader:
            if r['sale_month'] == month and r['sale_year'] == year:
                count += float(r['total'])
                print('Medicine Name:', r['medi_name'])
                print('Medicine ID:', r['medi_ID'])
                print('SALE:', r['sale'])
                print('Quantity:', r['Quantity'])
                print('Total:', r['total'])
                print('\n')
        print("====================================")
        print("Total sale for the month:", count)
        print("===============================")

def day_purchase():
    print('Enter Date:')
    date = input()
    print('Enter Month:')
    month = input()
    print('Enter Year:')
    year = input()
    count = 0.0

    with open('Purchase.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        print("=============Day's Purchase=============")
        for r in reader:
            if r['pur_date'] == date and r['pur_month'] == month and r['pur_year'] == year:
                count += float(r['cost'])
                print('Medicine Name:', r['medi_name'])
                print('Medicine ID:', r['medi_ID'])
                print('Purchase Cost per item:', r['unit'])
                print('Quantity:', r['Quantity'])
                print('Total:', r['cost'])
                print('\n')
        print("=====================================")
        print("Total purchase cost of the day:", count)
        print("=======================================")

def month_purchase():
    print('Enter Month:')
    month = input()
    print('Enter Year:')
    year = input()
    count = 0.0

    with open('Purchase.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        print("=============Month's Purchase=============")
        for r in reader:
            if r['pur_month'] == month and r['pur_year'] == year:
                count += float(r['cost'])
                print('Medicine Name:', r['medi_name'])
                print('Medicine ID:', r['medi_ID'])
                print('Purchase Cost per item:', r['unit'])
                print('Quantity:', r['Quantity'])
                print('Total:', r['cost'])
                print('\n')
        print("=====================================")
        print("Total purchase cost of the month:", count)
        print("=======================================")

def profit_report():
    print('Enter Month:')
    month = input()
    print('Enter Year:')
    year = input()
    total_sales = 0.0
    total_purchases = 0.0

    with open('sales.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for r in reader:
            if r['sale_month'] == month and r['sale_year'] == year:
                total_sales += float(r['total'])

    with open('Purchase.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for r in reader:
            if r['pur_month'] == month and r['pur_year'] == year:
                total_purchases += float(r['cost'])

    profit = total_sales - total_purchases
    print(f"Profit for {month} -- {year} is {profit}!\n")

# Call the functions to test the output
day_sale()
month_sale()
day_purchase()
month_purchase()
profit_report()

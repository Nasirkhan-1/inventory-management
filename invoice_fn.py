import csv
from tempfile import NamedTemporaryFile
import shutil
import datetime

# DATE-MONTH-YEAR CODE
d = datetime.datetime.now()
date = d.strftime("%d")
month = d.strftime("%m")
year = d.strftime("%Y")

def sup_invoice():
    medi_name = input("Enter medicine name: ")
    Quantity = int(input("Enter the Quantity: "))
    sup_id = input("Enter the Supplier ID: ")

    # Get unit price and medi_id from medi.csv
    unit = 0
    medi_id = ""
    with open('medi.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['medi_name'].lower() == medi_name.lower():  # Case-insensitive match
                medi_id = row['medi_id']
                unit = float(row['unit'])
                break

    if not medi_id or unit == 0:
        print("Medicine not found in stock.")
        return

    cost = Quantity * unit

    # Append purchase record
    with open('Purchase.csv', 'a', newline='') as csvfile:
        columns = ['medi_name', 'medi_id', 'unit', 'Quantity', 'pur_date', 'pur_month', 'pur_year', 'sup_id', 'cost']
        writer = csv.DictWriter(csvfile, fieldnames=columns)

        if csvfile.tell() == 0:  # Add header if file is empty
            writer.writeheader()

        writer.writerow({
            'medi_name': medi_name,
            'medi_id': medi_id,
            'unit': unit,
            'Quantity': Quantity,
            'pur_date': date,
            'pur_month': month,
            'pur_year': year,
            'sup_id': sup_id,
            'cost': cost
        })

    # Update stock in medi.csv
    tempfile = NamedTemporaryFile(mode='w', delete=False, newline='')
    with open('medi.csv', 'r') as csvfile, tempfile:
        columns = ['medi_name', 'medi_id', 'sale', 'unit', 'Quantity', 'min_quantity', 'comp_name', 'sup_id', 'to_pur']
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(tempfile, fieldnames=columns)
        writer.writeheader()

        for row in reader:
            if row['medi_name'].lower() == medi_name.lower():
                row['Quantity'] = int(row['Quantity']) + Quantity
                row['to_pur'] = max(0, int(row['min_quantity']) - int(row['Quantity']))
            writer.writerow(row)

    shutil.move(tempfile.name, 'medi.csv')
    print("The file is updated successfully.")


def customer_invoice():
    medicinename = []
    medicinecost = []
    medicine_quantity = []
    total_cost = 0

    customer_name = input("Enter customer name: ")
    customer_id = ""

    # Check customer record
    with open('customer_men.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['customer_name'].lower() == customer_name.lower():  # Case-insensitive match
                customer_id = row['customer_id']
                break

    if not customer_id:
        print("Customer not found.")
        return

    while True:
        medi_name = input("Enter medicine name (or type 'done' to finish): ")
        if medi_name.lower() == 'done':
            break

        Quantity = int(input("Enter quantity: "))

        # Process medicine record
        tempfile = NamedTemporaryFile(mode='w', delete=False, newline='')
        with open('medi.csv', 'r') as csvfile, tempfile:
            columns = ['medi_name', 'medi_id', 'sale', 'unit', 'Quantity', 'min_quantity', 'comp_name', 'sup_id', 'to_pur']
            reader = csv.DictReader(csvfile)
            writer = csv.DictWriter(tempfile, fieldnames=columns)
            writer.writeheader()

            for row in reader:
                if row['medi_name'].lower() == medi_name.lower():  # Case-insensitive match
                    sale_price = float(row['sale'])
                    available_qty = int(row['Quantity'])

                    if Quantity > available_qty:
                        print(f"Only {available_qty} units available in stock.")
                        continue

                    # Update stock
                    row['Quantity'] = available_qty - Quantity
                    row['to_pur'] = max(0, int(row['min_quantity']) - int(row['Quantity']))
                    total_cost += Quantity * sale_price

                    # Add to invoice
                    medicinename.append(medi_name)
                    medicinecost.append(sale_price)
                    medicine_quantity.append(Quantity)

                writer.writerow(row)

        shutil.move(tempfile.name, 'medi.csv')

    # Generate invoice
    print("\n|========== Generating Invoice ==========|")
    print(f"Customer Name: {customer_name}")
    print(f"Customer ID: {customer_id}")
    print(f"Date: {d.strftime('%x')}")
    print("\n| Medicine Name | Quantity | Unit Price | Total |")
    grand_total = 0
    for i in range(len(medicinename)):
        line_total = medicine_quantity[i] * medicinecost[i]
        print(f"| {medicinename[i]} | {medicine_quantity[i]} | {medicinecost[i]:.2f} | {line_total:.2f} |")
        grand_total += line_total
    print(f"\n| GRAND TOTAL: {grand_total:.2f} |")
    print("|============== Thank You ==============|")


if __name__ == "__main__":
    print("Choose an operation:")
    print("1. Supplier Invoice")
    print("2. Customer Invoice")
    choice = input("Enter your choice: ")
    if choice == '1':
        sup_invoice()
    elif choice == '2':
        customer_invoice()
    else:
        print("Invalid choice. Exiting.")

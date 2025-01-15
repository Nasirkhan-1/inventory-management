import csv
import shutil
import datetime
from tempfile import NamedTemporaryFile

d = datetime.datetime.now()

def add_medicine():
    columns = ['medi_name', 'medi_id', 'sale', 'unit', 'Quantity', 'min_quantity', 'comp_name', 'sup_id', 'to_pur']
    with open('medi.csv', 'a+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        if csvfile.tell() == 0:
            writer.writeheader()

        medi_name = input("Enter medicine name: ")
        with open('medi.csv', 'r') as readfile:
            reader = csv.DictReader(readfile)
            for row in reader:
                if row['medi_name'] == medi_name:
                    print("Medicine Already exists.")
                    return

        medi_id = input("Enter ID: ")
        sale = float(input("Enter sale price: "))
        unit = float(input("Enter cost price: "))
        Quantity = int(input("Enter Quantity: "))
        min_quantity = int(input("Enter Minimum Quantity: "))
        comp_name = input("Enter company name: ")
        sup_id = input("Supplier ID: ")
        to_pur = max(0, min_quantity - Quantity)
        cost = Quantity * unit

        writer.writerow({
            'medi_name': medi_name,
            'medi_id': medi_id,
            'sale': sale,
            'unit': unit,
            'Quantity': Quantity,
            'min_quantity': min_quantity,
            'comp_name': comp_name,
            'sup_id': sup_id,
            'to_pur': to_pur
        })

def search_medicine():
    with open('medi.csv', 'r') as csvfile:
        name = input("Enter the medicine name to search: ")
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['medi_name'] == name:
                print(f"Name: {row['medi_name']}\nQuantity: {row['Quantity']}\nPrice: {row['sale']}")
                return
        print("Medicine not found.")

def update_medicine():
    columns = ['medi_name', 'medi_id', 'sale', 'unit', 'Quantity', 'min_quantity', 'comp_name', 'sup_id', 'to_pur']
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    with open('medi.csv', 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(tempfile, fieldnames=columns)
        writer.writeheader()

        med_name = input("Enter the name of the medicine you want to modify: ")
        for row in reader:
            if row['medi_name'] == med_name:
                print("1. Update Name\n2. Update Cost Price\n3. Update Sale Price\n4. Update Supplier ID")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    row['medi_name'] = input("Enter the new Name: ")
                elif choice == 2:
                    row['unit'] = input("Enter the New Cost Price: ")
                elif choice == 3:
                    row['sale'] = input("Enter the New Sale Price: ")
                elif choice == 4:
                    row['sup_id'] = input("Enter the New Supplier ID: ")
            writer.writerow(row)
    shutil.move(tempfile.name, 'medi.csv')

def medicine_to_be_purchased():
    count = 0
    with open('medi.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row['to_pur']) > 0:
                count += 1
                print(f"Name: {row['medi_name']}\nQuantity: {row['Quantity']}\n"
                      f"Minimum Quantity: {row['min_quantity']}\nTo be purchased: {row['to_pur']}\nSupplier ID: {row['sup_id']}")
    if count == 0:
        print("No medicine to be purchased.\n")

# Test the functions as needed

add_medicine()
search_medicine()
update_medicine()
medicine_to_be_purchased()

import csv
import os
from tempfile import NamedTemporaryFile
import shutil


# Generate unique supplier ID
def supplier_id_generator():
    if not os.path.exists('supplier.csv'):
        return 1

    with open('supplier.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        max_id = 0
        for r in reader:
            max_id = max(max_id, int(r['sup_id']))
        return max_id + 1


# Create a new supplier
def create_supplier():
    if not os.path.exists('supplier.csv'):
        with open('supplier.csv', 'w', newline='') as csvfile:
            columns = ['sup_name', 'sup_id', 'sup_city', 'sup_cont', 'sup_email']
            writer = csv.DictWriter(csvfile, fieldnames=columns)
            writer.writeheader()

    with open('supplier.csv', 'a', newline='') as csvfile:
        columns = ['sup_name', 'sup_id', 'sup_city', 'sup_cont', 'sup_email']
        writer = csv.DictWriter(csvfile, fieldnames=columns)

        sup_name = input("Enter the supplier's name: ")
        sup_id = supplier_id_generator()
        print('Unique Supplier ID Generated:', sup_id)
        sup_city = input("Enter the supplier's city: ")
        sup_contact = input("Enter the supplier's contact number: ")
        sup_email = input("Enter the supplier's email: ")

        writer.writerow({
            'sup_name': sup_name,
            'sup_id': sup_id,
            'sup_city': sup_city,
            'sup_cont': sup_contact,
            'sup_email': sup_email
        })
        print("Supplier added successfully!")


# Update supplier information
def update_sup_info():
    tempfile = NamedTemporaryFile(mode='w', delete=False, newline='')
    columns = ['sup_name', 'sup_id', 'sup_city', 'sup_cont', 'sup_email']

    with open('supplier.csv', 'r', newline='') as csvfile, tempfile:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(tempfile, fieldnames=columns)
        writer.writeheader()

        supp_name = input("Enter the name of the supplier you want to modify: ")
        found = False

        for row in reader:
            if row['sup_name'].lower() == supp_name.lower():
                found = True
                print("Supplier found. Choose what to update:")
                print("1. Name")
                print("2. City")
                print("3. Contact")
                print("4. Email")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    row['sup_name'] = input("Enter the new name: ")
                elif choice == 2:
                    row['sup_city'] = input("Enter the new city: ")
                elif choice == 3:
                    row['sup_cont'] = input("Enter the new contact: ")
                elif choice == 4:
                    row['sup_email'] = input("Enter the new email: ")
                else:
                    print("Invalid choice. No updates made.")
            writer.writerow(row)

        if not found:
            print("Supplier not found.")

    shutil.move(tempfile.name, 'supplier.csv')
    print("Supplier information updated successfully!" if found else "No updates made.")


# Search for a supplier by name
def sup_search_by_name():
    with open('supplier.csv', 'r', newline='') as csvfile:
        name = input("Enter Supplier Name: ")
        reader = csv.DictReader(csvfile)
        found = False
        for r in reader:
            if r['sup_name'].lower() == name.lower():
                found = True
                print(f"Name: {r['sup_name']}, ID: {r['sup_id']}, City: {r['sup_city']}, "
                      f"Contact No: {r['sup_cont']}, Email: {r['sup_email']}")
        if not found:
            print("Supplier not found.")


# Search for a supplier by ID
def sup_search_by_id():
    with open('supplier.csv', 'r', newline='') as csvfile:
        sup_id = input("Enter Supplier ID: ")
        reader = csv.DictReader(csvfile)
        found = False
        for r in reader:
            if r['sup_id'] == sup_id:
                found = True
                print(f"Name: {r['sup_name']}, ID: {r['sup_id']}, City: {r['sup_city']}, "
                      f"Contact No: {r['sup_cont']}, Email: {r['sup_email']}")
        if not found:
            print("Supplier not found.")


# Main menu for supplier search
def search_supplier():
    while True:
        print("-----------------------------------------------")
        print("|Enter 1 to search the supplier by name!      |")
        print("|Enter 2 to search supplier by ID!            |")
        print("|Enter 3 to EXIT supplier search!             |")
        print("-----------------------------------------------")
        ss_choice = int(input("Enter your choice: "))
        if ss_choice == 1:
            sup_search_by_name()
        elif ss_choice == 2:
            sup_search_by_id()
        elif ss_choice == 3:
            break
        else:
            print("Invalid input! Try again.")


# Example usage
def main():
    while True:
        print("1. Add a Supplier")
        print("2. Search Supplier")
        print("3. Update Supplier")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_supplier()
        elif choice == 2:
            search_supplier()
        elif choice == 3:
            update_sup_info()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again!")


# Start the program
if __name__ == "__main__":
    main()

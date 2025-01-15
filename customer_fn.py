import csv
import shutil
from tempfile import NamedTemporaryFile


def customer_id_generator():
    """Generates a unique customer ID."""
    with open('customer_men.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        i = 1
        for row in reader:
            if int(row['customer_id']) == i:
                i += 1
    return i


def new_customer():
    """Adds a new customer."""
    with open('customer_men.csv', 'a+', newline='') as csvfile:
        names = ['customer_name', 'customer_id', 'customer_phone', 'customer_address']
        writer = csv.DictWriter(csvfile, fieldnames=names)

        # Write header only if file is empty
        csvfile.seek(0)
        if csvfile.read() == '':
            writer.writeheader()

        customer_name = input("Enter the name of the customer: ")
        customer_id = customer_id_generator()
        print("Unique ID Generated:", customer_id)
        customer_phone = input("Enter the phone number: ")
        customer_address = input("Enter the address: ")

        writer.writerow({'customer_name': customer_name,
                         'customer_id': customer_id,
                         'customer_phone': customer_phone,
                         'customer_address': customer_address})


def search_customer():
    """Searches for a customer by name."""
    name = input("Enter the name of the customer:\n")
    with open('customer_men.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        found = False
        for row in reader:
            if row['customer_name'] == name:
                found = True
                print("----------------------------------")
                print(
                    f"Name: {row['customer_name']}\nID: {row['customer_id']}\nPhone: {row['customer_phone']}\nAddress: {row['customer_address']}")
                print("----------------------------------")
        if not found:
            print("Customer not found.")


def update_customer_info():
    """Updates customer information."""
    names = ['customer_name', 'customer_id', 'customer_phone', 'customer_address']
    tempfile = NamedTemporaryFile(mode='w', delete=False, newline='')

    with open('customer_men.csv', 'r') as csvfile:import csv
import shutil
from tempfile import NamedTemporaryFile
import os

FILE_NAME = 'customer_men.csv'


def ensure_file_exists():
    """Ensures the CSV file exists with the correct header."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['customer_name', 'customer_id', 'customer_phone', 'customer_address'])
            writer.writeheader()
        print(f"File '{FILE_NAME}' created.")


def customer_id_generator():
    """Generates a unique customer ID."""
    ensure_file_exists()
    with open(FILE_NAME, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        ids = [int(row['customer_id']) for row in reader if row['customer_id'].isdigit()]
    return max(ids) + 1 if ids else 1


def new_customer():
    """Adds a new customer."""
    ensure_file_exists()
    with open(FILE_NAME, 'a+', newline='') as csvfile:
        names = ['customer_name', 'customer_id', 'customer_phone', 'customer_address']
        writer = csv.DictWriter(csvfile, fieldnames=names)

        customer_name = input("Enter the name of the customer: ")
        customer_id = customer_id_generator()
        print("Unique ID Generated:", customer_id)
        customer_phone = input("Enter the phone number: ")
        customer_address = input("Enter the address: ")

        writer.writerow({
            'customer_name': customer_name,
            'customer_id': customer_id,
            'customer_phone': customer_phone,
            'customer_address': customer_address
        })
        print("Customer added successfully.")


def search_customer():
    """Searches for a customer by name."""
    ensure_file_exists()
    name = input("Enter the name of the customer:\n")
    with open(FILE_NAME, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        found = False
        for row in reader:
            if row['customer_name'].lower() == name.lower():
                found = True
                print("----------------------------------")
                print(
                    f"Name: {row['customer_name']}\nID: {row['customer_id']}\nPhone: {row['customer_phone']}\nAddress: {row['customer_address']}")
                print("----------------------------------")
        if not found:
            print("Customer not found.")


def update_customer_info():
    """Updates customer information."""
    ensure_file_exists()
    names = ['customer_name', 'customer_id', 'customer_phone', 'customer_address']
    tempfile = NamedTemporaryFile(mode='w', delete=False, newline='')

    with open(FILE_NAME, 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(tempfile, fieldnames=names)
        writer.writeheader()

        id_no = input("Enter the ID of the customer you want to modify:\n")
        found = False
        for row in reader:
            if row['customer_id'] == id_no:
                found = True
                print("----------------------------")
                print("| Enter 1 to change name          |")
                print("| Enter 2 to change phone number  |")
                print("| Enter 3 to change address       |")
                print("----------------------------")
                try:
                    choice = int(input("Enter choice:\n"))
                    if choice == 1:
                        row['customer_name'] = input("Enter the new name: ")
                    elif choice == 2:
                        row['customer_phone'] = input("Enter the new phone number: ")
                    elif choice == 3:
                        row['customer_address'] = input("Enter the new address: ")
                    else:
                        print("Invalid choice. No changes made.")
                except ValueError:
                    print("Invalid input. No changes made.")
            writer.writerow(row)

        if not found:
            print("Customer ID not found.")

    shutil.move(tempfile.name, FILE_NAME)
    print("Customer information updated successfully.")


# Menu for testing the functions
def menu():
    print("----------------------------")
    print("Customer Management System")
    print("----------------------------")
    print("1. Add a New Customer")
    print("2. Search for a Customer")
    print("3. Update Customer Information")
    print("4. Exit")
    print("----------------------------")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                new_customer()
            elif choice == 2:
                search_customer()
            elif choice == 3:
                update_customer_info()
            elif choice == 4:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    try:
        menu()
    except Exception as e:
        print(f"An error occurred: {e}")

        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(tempfile, fieldnames=names)
        writer.writeheader()

        id_no = input("Enter the ID of the customer you want to modify:\n")
        found = False
        for row in reader:
            if row['customer_id'] == id_no:
                found = True
                print("----------------------------")
                print("| Enter 1 to change name          |")
                print("| Enter 2 to change phone number  |")
                print("| Enter 3 to change address       |")
                print("----------------------------")
                choice = int(input("Enter choice:\n"))

                if choice == 1:
                    row['customer_name'] = input("Enter the new name: ")
                elif choice == 2:
                    row['customer_phone'] = input("Enter the new phone number: ")
                elif choice == 3:
                    row['customer_address'] = input("Enter the new address: ")

            writer.writerow(row)

        if not found:
            print("Customer ID not found.")

    shutil.move(tempfile.name, 'customer_men.csv')

import medi_fn
import customer_fn
import report_fn
import invoice_fn
import supllier_fn

def medicine_menu():
    m_menu_choice=0
    while(m_menu_choice!=5):
        print('---------------------------------------------')
        print("|Enter 1 to Add medicine                    |")
        print('---------------------------------------------')
        print("|Enter 2 to search medicine                 |")
        print('---------------------------------------------')
        print("|Enter 3 to update medicine info           |")
        print('---------------------------------------------')
        print("|Enter 4 for medicine  to be purchased list |")
        print('---------------------------------------------')
        print("|Enter 5 to go back to Main Menu            |")
        print('---------------------------------------------')
        m_menu_choice= int(input("Enter you choice!\n"))
        if(m_menu_choice==1):
            medi_fn.add_medicine()
        elif(m_menu_choice==2):
            medi_fn.search_medicine()
        elif (m_menu_choice == 3):
            medi_fn.update_medicine()
        elif (m_menu_choice == 4):
            medi_fn.medicine_to_be_purchased()
        elif m_menu_choice==5:
            break
        else:
            print("Invalid Input! try again!\n")

def customer_menu():
    c_menu_choice=0
    while(c_menu_choice!=4):
        print("----------------------------------------")
        print("|Enter 1  to search customer           |")
        print("----------------------------------------")
        print("|Enter 2  to create new customer       |")
        print("----------------------------------------")
        print("|Enter 3  to update customer info      |")
        print("----------------------------------------")
        print("|Enter 4  to go back to main menu       ")
        print("----------------------------------------")
        c_menu_choice==int(input("Enter your choice!\n"))
        customer_menu = int(input("Enter you choice!\n"))
        if ( customer_menu == 1):
            customer_fn.search_customer()
        elif (customer_menu == 2):
            customer_fn.new_customer()
        elif (customer_menu == 3):
            customer_fn.update_customer_info()
        elif (customer_menu == 4):
            break
        else:
            print("Invalid Input! try again!\n")

def supplier_menu():
    s_menu_choice=0
    while(s_menu_choice!=4):
        print("-------------------------------------------------")
        print("|   Enter 1 to searh supplier                   |")
        print("-------------------------------------------------")
        print("|   Enter 2 to create new supplier              |")
        print("-------------------------------------------------")
        print("|   Enter 3 to update supplier info             |")
        print("-------------------------------------------------")
        print("|   Enter 4 to go back to main menu             |")
        print("-------------------------------------------------")
        print("Enter 1 to search supplier. \nEnter 2 to create new supplier. \nEnter 3 to update supplier information."
              "\nEnter 4 to go back to main menu. ")
        s_menu_choice= int(input("Enter choice.!\n"))
        if(s_menu_choice==1):
            supllier_fn.search_supplier()
        elif (s_menu_choice == 2):
            supllier_fn.create_supplier()
        elif(s_menu_choice == 3):
            supllier_fn.update_sup_info()
        elif(s_menu_choice == 4):
            break
        else:
            print("Invalid input! try again !\n")

def report_menu():
    r_menu_choice=0
    while(r_menu_choice!=6):
        while(r_menu_choice!=6):
            print("-------------------------------------------")
            print("| enter 1 for todays sale                 |")
            print("-------------------------------------------")
            print("| enter 2 for monthly sale                |")
            print("-------------------------------------------")
            print("| enter 3 for todays purchase             |")
            print("-------------------------------------------")
            print("| enter 4 for monthly purchase            |")
            print("-------------------------------------------")
            print("| enter 5 for profit report               |")
            print("-------------------------------------------")
            print("| enter 6 to go to main menu              |")

            r_menu_choice=int(input("Enter your choice!\n"))
            if (r_menu_choice==1):
                report_fn.day_sale()
            elif (r_menu_choice==2):
                report_fn.month_sale()
            elif (r_menu_choice==3):
                report_fn.day_purchase()
            elif (r_menu_choice==4):
                report_fn.month_purchase()
            elif (r_menu_choice==5):
                report_fn.profit_report()
            elif r_menu_choice==6:
                break
            else:
                print("invaid report! tr again!\n")

def invoicing_menu():
    i_menu_choice=0
    while(i_menu_choice!=3):
        print("-------------------------------------------")
        print("|Enter 1 for supplier invoice             |")
        print("-------------------------------------------")
        print("|Enter 2 for customer invoice             |")
        print("-------------------------------------------")
        print("|Enter 3 to return to main menu           |")
        print("-------------------------------------------")
        i_menu_choice= int(input("Enter your choice!\n"))
        if(i_menu_choice==1):
            invoice_fn.sup_invoice()
        elif(i_menu_choice==2):
            invoice_fn.customer_invoice()
        elif(i_menu_choice==3):
            break
        else:
            print("invalid input! try again!")


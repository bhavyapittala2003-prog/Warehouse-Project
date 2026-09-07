from app import global_warehouse_stock_details,low_stock_safety_alert,days_of_supply,add_item_to_list,fastest_selling_report
from app import update_item_info,search_by_id,del_item,update_stock,item_checkout,view_transaction_history,save_companies_info,active_suppliers

print('''=======================================================
           SMART INVENTORY MANAGEMENT SYSTEM                    
=======================================================''')
print('''[ MANAGING YOUR ITEMS CATALOG ]
Click 1  : Add a brand new item to the store list
Click 2  : Change details of an item (like its Name, Category, or Price)
Click 3  : Search for specific item by typing ID 
Click 4  : Delete an item permanently by ID 

[ CHECKING STOCK ON THE SHELVES ]
Click 5  : View all items at once and see the total money tied up in stock
Click 6  : Run a quick scan to show only the items running dangerously low

[ THE CASH REGISTER & CARGO DOCK ]
Click 7 : Add new items coming from a delivery truck (Stock goes up)
Click 8 : Record items bought by a customer at checkout (Stock goes down)
Click 9 : View the timeline history page to see every single stock change

[ THE SUPPLIER ADDRESS BOOK ]
Click 10 : Save a new manufacturing company's phone and email details
Click 11 : View the full contacts directory of all active suppliers

[ FUTURE PREDICTIONS & SPECIAL REPORTS ]
Click 12 : Calculate the supply duration and days remaining for warehouse stock
Click 13 : Show a quick report card of the top 3 fastest-selling items
Click 14 : Exit  ''')
print("=======================================================\n")

while(True):
    choice = input("Enter your choice:")
    if choice == "1":
        add_item_to_list()
    elif choice == "2":
        update_item_info()
    elif choice == "3":
        id = int(input("\nEnter the ID that got to be searched : "))
        search_by_id(id)
    elif choice == "4":
        id = int(input("\nEnter the ID that got to be Deleted : "))
        del_item(id)
    elif choice == "5":
        global_warehouse_stock_details()
    elif choice == "6":
        low_stock_safety_alert()
    elif choice == "7":
        id = int(input("\nEnter Product Id arriving on the cargo truck : "))
        update_stock(id)
    elif choice == "8":
        id = int(input("\nEnter Product ID for customer checkout : "))
        item_checkout(id)
    elif choice == "9":
        view_transaction_history()
    elif choice == "10":
        save_companies_info()
    elif choice == "11":
        active_suppliers()
    elif choice == "12":
        days_of_supply()
    elif choice == "13":
        fastest_selling_report()
    elif choice == "14":
        print("\nExiting Smart Inventory Management System. Goodbye!")
        break
    else :
        print("\n[INVALID CHOICE] Please select a number between 1 and 14.\n")
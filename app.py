from db import get_connection
##choice = 1
def add_item_to_list():
    connection = get_connection()
    print('''\n=======================================================
                ADD A BRAND NEW ITEM TO LIST  
=======================================================''')
    cursor = connection.cursor()
    try:
        item = input("Enter Product Name : ")
        categ = input("Enter Category of the product : ")
        stock_quantity = int(input("Enter Initial on-hand stock Quantity : "))
        limit = int(input("Enter Low-Stock Safety Limit Level : "))
        price = float(input("Enter Wholesale Purchase Price : "))
        sales = int(input("Enter Expected Daily Sales Speed : "))

        q = '''insert into warehouse_inventory
        (product_name,category,current_stock,min_safety_stock,unit_cost,daily_sales_rate) values(%s,%s,%s,%s,%s,%s)'''
        cursor.execute(q,(item,categ,stock_quantity,limit,price,sales))
        connection.commit()
        print("Successfully added to list!")
    except ValueError:
        print("[ERROR] Failed to save. You must enter numbers for quantity, limit, price, and sales.")
    except Exception:
        print("[ERROR] Failed to save.You cannot add duplicate product names.")
    finally:
        print("=======================================================\n")
        cursor.close()
        connection.close()

##choice = 2
def update_item_info():
    connection = get_connection()
    cursor = connection.cursor()
    print("\n=============UPDATE EXISTING PRODUCT DETAILS===========")
    try:
        id = int(input("Enter the product ID that should be update : "))
        print('''What details would you like to update?
1. Product Name
2. Business Category
3. Wholesale Unit Cost
4. Safety Threshold Limit (Change the alert line)
5. Expected Daily Sales Velocity (Adjust sales calculations)
6. Update new product information all at once ''')
        num = input("Choose an option from above : ")
        if num == "1" :
            name = input("Enter Product Name : ")
            q = "update warehouse_inventory set product_name=%s where product_id=%s"
            cursor.execute(q,(name,id))
        elif num == "2":
            category = input("Enter Product Category : ")
            q = "update warehouse_inventory set category=%s where product_id=%s"
            cursor.execute(q,(category,id))
        elif num == "3" :
            cost = float(input("Enter cost : "))
            q = "update warehouse_inventory set unit_cost=%s where product_id=%s"
            cursor.execute(q,(cost,id))
        elif num == "4":
            limit = int(input("Enter safety threshold limit : "))
            q = "update warehouse_inventory set min_safety_stock=%s where product_id =%s"
            cursor.execute(q,(limit,id))
        elif num == "5":
            sales = int(input("Enter Expected Daily Sales : "))
            q = "update warehouse_inventory set daily_sales_rate=%s where product_id=%s"
            cursor.execute(q,(sales,id))
        elif num == "6":
            name = input("Enter Product Name : ")
            category = input("Enter Product Category : ")
            stock = int(input("Enter Current Stock Quantity : "))
            cost = float(input("Enter cost : "))
            limit = int(input("Enter safety threshold limit : "))
            sales = int(input("Enter Expected Daily Sales : "))
            q = '''update warehouse_inventory set
            product_name=%s,category=%s,unit_cost=%s,current_stock = %s,min_safety_stock=%s,daily_sales_rate=%s
            where product_id=%s '''      
            cursor.execute(q,(name,category,stock,cost,limit,sales,id))  
        connection.commit()
        if cursor.rowcount == 0:
            print(f"[INFO] No changes made. Product ID {id} does not exist.")
        else:
            print("Successfully got updated")
    except Exception as e:
        print(f"[ERROR] Database error occurred: {e}")
    finally:
        print("=======================================================\n")
        cursor.close()
        connection.close()
        
##choice = 3
def print_single_item(product):
    print("\n==================Product Details=======================")
    print(f"Product ID : {product[0]}")
    print(f"Product Name : {product[1]}")
    print(f"Category : {product[2]}")
    print(f"Stock : {product[3]}")
    print(f"Safety  : {product[4]}")
    print(f"Cost : {product[5]}")
    print(f"Daily Sales : {product[6]}")
def search_by_id(id):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        query = "select * from warehouse_inventory where product_id = %s"
        cursor.execute(query, (id,))
        product = cursor.fetchone()
        if product is not None:
            print_single_item(product)
        else : 
            print(f"Product id {id} does not exit in the list of products")
    except ValueError:
        print("[ERROR] Invalid input. Product ID must be a whole number.")
    finally:
        print("=========================================================\n")
        cursor.close()
        connection.close()    

##choice = 4
def del_item(id):
    connection = get_connection()
    cursor = connection.cursor()
    query = "select * from warehouse_inventory where product_id = %s"
    cursor.execute(query, (id,))
    product = cursor.fetchone()
    if product == None:
            print("Product ID not registered in the system")
    else:
        q = "delete from warehouse_inventory where product_id = %s"
        cursor.execute(q,id)
        connection.commit()
        print("Deleted Successfully")
    print("=========================================================\n")
    cursor.close()
    connection.close()    

##choice = 5
def print_stock_details(products):
    total_valuation = 0
    for product in products:
        total_valuation += (product[3] * product[5])
        print("\n=======GLOBAL WAREHOUSE STOCK DETAILS & VALUATION========")
        print(f"Product ID : {product[0]}")
        print(f"Product Name : {product[1]}")
        print(f"Category : {product[2]}")
        print(f"Stock : {product[3]}")
        print(f"Safety  : {product[4]}")
        print(f"Cost : {product[5]}")
        print(f"Daily Sales : {product[6]}")
    print("=======================================================")
    print(f"Total warehouse Capital Tied Up In Stock : {total_valuation:,.2f}")
    print("=======================================================\n")
def global_warehouse_stock_details():
    connection = get_connection()
    q = "select * from warehouse_inventory"
    cursor = connection.cursor()
    cursor.execute(q)
    res = cursor.fetchall()
    print_stock_details(res)
    cursor.close()
    connection.close()

##choice = 6
def low_stock_safety_alert():
    connection = get_connection()
    q = "select * from warehouse_inventory"
    cursor = connection.cursor()
    cursor.execute(q)
    res = cursor.fetchall()
    alert_count = 0
    print("\n=============LOW-STOCK SAFETY ALERTS===================")
    for product in res:
        if product[3] <= product[4]:
            print(f'''ID :  {product[0]}
Product Name : {product[1]}  is dangerously low in stock
Current Stock : {product[3]} units   
Safety Threshold Limit : {product[4]} units

ACTION REQUIRED : Order stock immediately
=======================================================\n''')  
            alert_count += 1
    if alert_count == 0:
        print("All products maintain healthy safety stock thresholds.")
        print("=======================================================\n")
    cursor.close()
    connection.close()

##choice = 7
def update_stock(id):
    connection = get_connection()
    cursor = connection.cursor()
    q = "select product_name,current_stock from warehouse_inventory where product_id = %s"
    cursor.execute(q,(id,))
    product = cursor.fetchone()
    print("\n============ INCOMING SHIPMENT & DELIVERY =============")
    if product == None :
        print("Product ID not registered in the system.")
        print("=======================================================\n")
        cursor.close()
        connection.close()
        return 
    product_name = product[0]
    current_stock = product[1]
    print(f"Target Verified: '{product_name}'. On-Hand Stock: {current_stock} units")
    qty = int(input("Enter incoming stock unit quantity: "))
    if qty <= 0 :
        print("Incoming units must be a positive number.")
        print("=======================================================\n")
    else:
        updated_q = "update warehouse_inventory set current_stock=current_stock + %s where product_id = %s"
        cursor.execute(updated_q,(qty,id))
        log_q = "INSERT INTO transaction_logs (product_id, quantity, transaction_type) VALUES (%s, %s, 'PURCHASE')"
        cursor.execute(log_q, (id, qty))
        connection.commit()
        print("Warehouse stock update successfully completed!")
        print("=======================================================\n")
    cursor.close()
    connection.close()

##click = 8
def item_checkout(id):
    connection = get_connection()
    cursor = connection.cursor()
    q = "select product_name,current_stock from warehouse_inventory where product_id = %s"
    cursor.execute(q,(id,))
    print("\n============== CUSTOMER CHECKOUT COUNTER ==============")
    product = cursor.fetchone()
    if product == None :
        print("Product ID not registered in the system.")
        print("=======================================================\n")
        cursor.close()
        connection.close()
        return 
    product_name = product[0]
    current_stock = product[1]
    print(f"Target Verified: '{product_name}'. On-Hand Stock: {current_stock} units")
    qty = int(input("Enter sales checkout unit quantity: "))
    if qty <= 0:
        print("QUANTITY ERROR: Sales quantity must be a positive number.")
        print("=======================================================\n")
    elif qty > current_stock :
        print("SHORTAGE EXCEPTION: Insufficient stock available to complete this consumer order!")
        print(f"Requested: {qty}units | Available: {current_stock}units  ")
        print("Action: Order cancelled. Please restock this item first.")
        print("=======================================================\n")
    else:
        down_q = "update warehouse_inventory set current_stock=current_stock - %s where product_id = %s"
        cursor.execute(down_q,(qty,id))
        log_q = "INSERT INTO transaction_logs (product_id, quantity, transaction_type) VALUES (%s, %s, 'SALE')"
        cursor.execute(log_q, (id, qty))
        connection.commit()
        print("SUCCESS: Customer checkout processed successfully!")
        print("=======================================================\n")
    cursor.close()
    connection.close()

##click = 9
def view_transaction_history():
    connection = get_connection()
    cursor = connection.cursor()
    q = """
        SELECT a.transaction_id, b.product_name, a.quantity, a.transaction_type, a.date_time
        FROM transaction_logs as a
        INNER JOIN warehouse_inventory as b ON a.product_id = b.product_id
        ORDER BY a.transaction_id DESC
    """
    cursor.execute(q)
    print("\n=================Transaction Details===================")
    products = cursor.fetchall()
    if len(products) == 0:
        print(f"{'No transaction events registered in the ledger history yet.'}")
        print("=======================================================\n")
    else:
        for product in products:
            qty = f"-{product[2]}" if product[3] == "SALE" else f"{product[2]}"
            print(f"Transaction ID : {product[0]}")
            print(f"Product Name   : {product[1]}")
            print(f"Quantity Change: {qty}")
            print(f"Type           : {product[3]}")
            print(f"Timestamp      : {str(product[4])}")
            print("=======================================================\n")
    cursor.close()
    connection.close()

## choice = 10
def save_companies_info():
    connection = get_connection()
    cursor = connection.cursor()
    print("\n===========SAVE NEW MANUFACTURING COMPANY==============")
    try : 
        c_name = input("Enter Company Name : ")
        pho_number = input("Enter Phone Number : ")
        email_address = input("Enter Email Address : ")
        person = input("Enter Contact Person : ")
        if not c_name or not pho_number or not email_address:
            print("[ERROR] Failed to save. Company Name, Phone, and Email cannot be left blank.")
            return
        q = '''insert into manufacturing_companies
        (company_name,phone_number,email_address,contact_name) values (%s,%s,%s,%s) '''
        cursor.execute(q,(c_name,pho_number,email_address,person))
        connection.commit()
        print("[SUCCESS] Company details saved successfully!")
    except Exception as e:
        print(f"[ERROR] Failed to save database record. Details: {e}")
    finally:
        print("=======================================================\n")
        cursor.close()
        connection.close()

##choice = 11
def active_suppliers():
    connection = get_connection()
    cursor = connection.cursor()
    q = "select * from manufacturing_companies"
    cursor.execute(q)
    print("\n=========ACTIVE SUPPLIERS CONTACT DIRECTORY============")
    suppliers = cursor.fetchall()
    if not suppliers :
        print("[INFO] No active suppliers found in the database directory.")
        print("=======================================================\n")
    else :
        for supplier in suppliers:
            print(f"Company Name   : {supplier[0]}")
            print(f"Phone Number   : {supplier[1]}")
            print(f"Email Address  : {supplier[2]}")
            print(f"Contact Person : {supplier[3]}")
            print("=======================================================\n")
    cursor.close()
    connection.close()

##choice = 12
def days_of_supply():
    connection = get_connection()
    q = "select * from warehouse_inventory"
    cursor = connection.cursor()
    cursor.execute(q)
    res = cursor.fetchall()
    print("\n=======================================================")
    print("  PREDICTIVE STOCK DEPLETION ANALYTICS(DAYS OF SUPPLY) ")
    print("=======================================================")
    for product in res:
        if product[6] <= 0:
            days_remaining = float('inf') 
            status = "No Sales / Stable"
        else:
            days_remaining = (product[3] / product[6])
            if days_remaining <= 5:
                status = "Critical Risk"
            elif days_remaining <= 15 :
                status = "Moderate Risk"
            else:
                status = "Stable"
        final_days_remaining = "Infinite" if days_remaining == float('inf') else f"{days_remaining:.1f}"
        print(f'''ID : {product[0]}
Product Name : {product[1]}
Supply Duration : {final_days_remaining} Days remaining
[Status : {status}]
=======================================================\n''')
    cursor.close()
    connection.close()

## choice = 13
def fastest_selling_report():
    connection = get_connection()
    cursor = connection.cursor()
    q = "select product_id ,product_name , daily_sales_rate   from warehouse_inventory order by daily_sales_rate DESC limit 3"
    cursor.execute(q)
    res = cursor.fetchall()
    print("\n=========== TOP 3 FASTEST-SELLING ITEMS ===============")
    i = 0
    for product in res:
        i +=1
        print(f"==> RANK {i}")
        print(f"    ID          :  {product[0]}")
        print(f"    Product Name:  {product[1]}")
        print(f"    Sales Speed :  {product[2]} units/days")
        print("=======================================================\n")
    cursor.close()
    connection.close()
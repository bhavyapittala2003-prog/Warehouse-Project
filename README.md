# 📦 Smart Inventory Management System

> 🚀 A Python + MySQL based inventory management system designed to efficiently manage products, stock, suppliers, transactions, and inventory analytics.

---

## 🌟 Project Overview

The **Smart Inventory Management System** is a console-based application developed using **Python and MySQL**.

It helps stores and warehouses manage their inventory efficiently by providing features for:

* 📦 Product management
* 📊 Stock monitoring
* ⚠️ Low-stock alerts
* 🚚 Incoming stock management
* 🛒 Customer checkout
* 📜 Transaction history
* 🏭 Supplier management
* 🔮 Stock depletion prediction
* 🏆 Fastest-selling product reports

---

## ✨ Features

### 📋 1. Product Management

The system provides complete product management functionality.

You can:

* ➕ Add new products
* ✏️ Update product details
* 🔍 Search products by ID
* 🗑️ Delete products

Product information includes:

* 🏷️ Product Name
* 📂 Category
* 📦 Stock Quantity
* ⚠️ Safety Stock Limit
* 💰 Unit Cost
* 📈 Expected Daily Sales

---

### 📊 2. Warehouse Stock Management

View complete warehouse inventory details including:

* 🆔 Product ID
* 🏷️ Product Name
* 📂 Category
* 📦 Current Stock
* ⚠️ Safety Stock
* 💰 Unit Cost
* 📈 Daily Sales Rate

The system also calculates the **total capital tied up in inventory**.

💡 **Formula:**

```text
Total Inventory Value = Current Stock × Unit Cost
```

---

### ⚠️ 3. Low-Stock Safety Alerts

The system automatically checks whether products have reached their minimum safety stock level.

```text
Current Stock <= Safety Stock
```

🚨 If the condition is satisfied, the system displays a warning asking the user to restock the product.

This helps prevent **inventory shortages** and stock-outs.

---

### 🚚 4. Incoming Stock Management

When new products arrive from a supplier, the user can increase the available stock.

The system:

1. 🔍 Verifies the Product ID
2. 📦 Accepts incoming quantity
3. ➕ Increases current stock
4. 📝 Records the transaction as `PURCHASE`
5. 💾 Updates the database

---

### 🛒 5. Customer Checkout

The system handles customer purchases.

Before completing a sale, it:

1. 🔍 Checks whether the product exists
2. 📦 Checks available stock
3. 🔢 Validates the requested quantity
4. ➖ Deducts the sold quantity
5. 📝 Records the transaction as `SALE`

🚫 The system prevents checkout if the requested quantity is greater than the available stock.

---

### 📜 6. Transaction History

The application maintains a transaction history containing:

* 🆔 Transaction ID
* 🏷️ Product Name
* 🔢 Quantity
* 🔄 Transaction Type
* 🕒 Timestamp

This makes it easier to track inventory movement over time.

---

### 🏭 7. Supplier Management

The system maintains a directory of manufacturing companies and suppliers.

Supplier information includes:

* 🏢 Company Name
* 📞 Phone Number
* 📧 Email Address
* 👤 Contact Person

Users can:

* ➕ Add supplier information
* 📖 View the complete supplier directory

---

### 🔮 8. Days of Supply Prediction

The system provides a simple inventory prediction feature to estimate how many days the current stock can last.

💡 **Formula:**

```text
Days of Supply = Current Stock ÷ Daily Sales Rate
```

### 📌 Inventory Status

| ⏳ Days Remaining  | 🚦 Status           |
| ----------------- | ------------------- |
| 0–5 Days          | 🔴 Critical Risk    |
| 6–15 Days         | 🟡 Moderate Risk    |
| More than 15 Days | 🟢 Stable           |
| No Sales          | ⚪ No Sales / Stable |

This helps identify products that may need to be restocked soon.

---

### 🏆 9. Fastest-Selling Products Report

The system generates a report of the **Top 3 Fastest-Selling Products**.

Products are ranked according to their daily sales rate.

```text
🏆 Rank 1
🥈 Rank 2
🥉 Rank 3
```

This helps identify products with high sales velocity.

---

# 🛠️ Technologies Used

| Technology      | Purpose                   |
| --------------- | ------------------------- |
| 🐍 Python       | Application development   |
| 🐬 MySQL        | Database management       |
| 🔌 PyMySQL      | Python-MySQL connectivity |
| 🗃️ SQL         | Database operations       |
| 🐙 Git & GitHub | Version control           |

---

# 📁 Project Structure

```text
📦 Smart-Inventory-Management-System
│
├── 🐍 main.py
├── 🐍 app.py
├── 🗄️ db.py
├── 📄 README.md
└── 📦 requirements.txt
```

> 💡 Update the filenames above if your actual GitHub files have different names.

---

# 🗄️ Database

The application uses a MySQL database named:

```text
smart_inventory_db
```

### 📋 Main Tables

```text
📦 warehouse_inventory
📜 transaction_logs
🏭 manufacturing_companies
```

### 📦 warehouse_inventory

Stores product and inventory information such as:

* 🆔 Product ID
* 🏷️ Product Name
* 📂 Category
* 📦 Current Stock
* ⚠️ Minimum Safety Stock
* 💰 Unit Cost
* 📈 Daily Sales Rate

### 📜 transaction_logs

Stores inventory transactions such as:

* 🚚 Purchases
* 🛒 Sales
* 🕒 Transaction Date/Time

### 🏭 manufacturing_companies

Stores supplier information such as:

* 🏢 Company Name
* 📞 Phone Number
* 📧 Email Address
* 👤 Contact Person

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

```bash
cd Smart-Inventory-Management-System
```

---

## 2️⃣ Install Dependencies

Install PyMySQL:

```bash
pip install pymysql
```

Or use:

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Create the Database

Open MySQL and create the database:

```sql
CREATE DATABASE smart_inventory_db;
```

Then create the required tables used by the application.

---

## 🔐 4️⃣ Configure Database Connection

⚠️ **IMPORTANT:** Never upload your real MySQL password to GitHub.

Your database connection should use environment variables instead of hard-coding your password.

Example:

```python
import os
from pymysql import connect

def get_connection():
    connection = connect(
        host="localhost",
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database="smart_inventory_db"
    )
    return connection
```

Create your local environment variables:

```text
DB_USER=root
DB_PASSWORD=your_mysql_password
```

🚫 Do not commit `.env` files or passwords to GitHub.

---

# ▶️ How to Run

Run the main Python program:

```bash
python main.py
```

The application provides a menu with **14 different operations**.

---

# 🖥️ Application Menu

```text
1️⃣  Add a brand new item
2️⃣  Update item details
3️⃣  Search item by ID
4️⃣  Delete item by ID
5️⃣  View warehouse stock details
6️⃣  Check low-stock alerts
7️⃣  Add incoming stock
8️⃣  Process customer checkout
9️⃣  View transaction history
🔟  Add supplier information
1️⃣1️⃣ View active suppliers
1️⃣2️⃣ Calculate days of supply
1️⃣3️⃣ View top 3 fastest-selling items
1️⃣4️⃣ Exit
```

---

# 💡 Example

Suppose a product has:

```text
📦 Current Stock       : 20 units
📈 Daily Sales Rate    : 2 units/day
⚠️ Safety Stock        : 5 units
```

The system calculates:

```text
Days of Supply = 20 ÷ 2
               = 10 Days
```

🚦 Result:

```text
🟡 Moderate Risk
```

The store manager can then plan the next stock purchase.

---

# 🎯 Key Benefits

✅ Reduces manual inventory tracking
✅ Provides centralized stock management
✅ Helps identify low-stock products
✅ Prevents sales when stock is insufficient
✅ Maintains transaction history
✅ Organizes supplier information
✅ Provides basic inventory forecasting
✅ Identifies fast-moving products
✅ Calculates inventory valuation

---

# 🚀 Future Improvements

The project can be enhanced further with:

* 🖥️ Graphical User Interface (GUI)
* 🌐 Web-based dashboard
* 🔐 User authentication
* 👥 Role-based access control
* 📷 Barcode/QR code scanning
* 📧 Automated email alerts
* 📱 SMS notifications
* 🤖 Machine Learning based sales forecasting
* 📊 Advanced analytics dashboard
* 📑 Excel/PDF report generation
* ☁️ Cloud database integration

---

# 📚 Learning Outcomes

Through this project, I gained practical experience in:

🐍 Python Programming
🗃️ MySQL Database Management
🔎 SQL Queries
🔄 CRUD Operations
🔌 Database Connectivity using PyMySQL
⚠️ Exception Handling
📦 Inventory Management
📜 Transaction Management
📊 Data Analysis
🔮 Basic Inventory Prediction

---

# 👩‍💻 Author

### **Bhavya**

📌 **Project:** Smart Inventory Management System
🐍 **Technology:** Python
🗄️ **Database:** MySQL

---

⭐ **If you find this project useful, consider giving it a star!**

💻 Built with Python + MySQL ❤️

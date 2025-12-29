import pandas as pd
import glob
import os

#Verify if the file exists
files = glob.glob("./data/*.csv")

if len(files) == 0:
    print("No files found")
else:
    print("Files found:", len(files))
    
#Read the files
df_brands = pd.read_csv("./data/ecommerce_brands.csv")
df_categories = pd.read_csv("./data/ecommerce_categories.csv")
df_customers = pd.read_csv("./data/ecommerce_customers.csv")
df_inventory = pd.read_csv("./data/ecommerce_inventory.csv")
df_order_items = pd.read_csv("./data/ecommerce_order_items.csv")
df_orders = pd.read_csv("./data/ecommerce_orders.csv")
df_products = pd.read_csv("./data/ecommerce_products.csv")
df_promotions = pd.read_csv("./data/ecommerce_promotions.csv")
df_reviews = pd.read_csv("./data/ecommerce_reviews.csv")
df_suppliers = pd.read_csv("./data/ecommerce_suppliers.csv")
df_warehouses = pd.read_csv("./data/ecommerce_warehouses.csv")

#Explore the data
print("Resume")
print("Brands: ", df_brands.shape)
print("Categories: ", df_categories.shape)
print("Customers: ", df_customers.shape)
print("Inventory: ", df_inventory.shape)
print("Order Items: ", df_order_items.shape)
print("Orders: ", df_orders.shape)
print("Products: ", df_products.shape)
print("Promotions: ", df_promotions.shape)
print("Reviews: ", df_reviews.shape)
print("Suppliers: ", df_suppliers.shape)
print("Warehouses: ", df_warehouses.shape)

print("\nFirst rows:")
print(df_orders.head())

print("\nInformation of the data:")
print(df_orders.info())

#Identify null values
print("\nNull Brands values:")
print(df_brands.isnull().sum())
print("\nNull Categories values:")
print(df_categories.isnull().sum())
print("\nNull Customers values:")
print(df_customers.isnull().sum())
print("\nNull Inventory values:")
print(df_inventory.isnull().sum())
print("\nNull Order Items values:")
print(df_order_items.isnull().sum())
print("\nNull Orders values:")
print(df_orders.isnull().sum())
print("\nNull Products values:")
print(df_products.isnull().sum())
print("\nNull Promotions values:")
print(df_promotions.isnull().sum())
print("\nNull Reviews values:")
print(df_reviews.isnull().sum())
print("\nNull Suppliers values:")
print(df_suppliers.isnull().sum())
print("\nNull Warehouses values:")
print(df_warehouses.isnull().sum())

#Identify duplicate values
print("\nDuplicate Brands values:")
print(df_brands.duplicated().sum())
print("\nDuplicate Categories values:")
print(df_categories.duplicated().sum())
print("\nDuplicate Customers values:")
print(df_customers.duplicated().sum())
print("\nDuplicate Inventory values:")
print(df_inventory.duplicated().sum())
print("\nDuplicate Order Items values:")
print(df_order_items.duplicated().sum())
print("\nDuplicate Orders values:")
print(df_orders.duplicated().sum())
print("\nDuplicate Products values:")
print(df_products.duplicated().sum())
print("\nDuplicate Promotions values:")
print(df_promotions.duplicated().sum())
print("\nDuplicate Reviews values:")
print(df_reviews.duplicated().sum())
print("\nDuplicate Suppliers values:")
print(df_suppliers.duplicated().sum())
print("\nDuplicate Warehouses values:")
print(df_warehouses.duplicated().sum())

#Identify data types
print("\nData types:")
print(df_orders.dtypes)

#Transform data types
df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])
df_orders['total_amount'] = pd.to_numeric(df_orders['total_amount'], errors='coerce')
df_order_items['quantity'] = pd.to_numeric(df_order_items['quantity'], errors='coerce')

print("\nData types after transformation:")
print(df_orders.dtypes)

#Find the top 5 by total amount
sales_by_customer = df_orders.groupby('customer_id').agg({'total_amount': 'sum','order_id':'count'}).sort_values('total_amount',ascending=False)
print("\nTop 5 customers by total amount:")
print(sales_by_customer.head())

#Find the product with the most sales
sales_by_product = df_order_items.groupby('product_id')['quantity'].sum().sort_values(ascending=False)
print(f"\nMost sold product: ID {sales_by_product.idxmax()} ({sales_by_product.max()} quantity)")

#Sales by month
df_orders['month'] = df_orders['order_date'].dt.to_period('M')
sales_by_month = df_orders.groupby('month')['total_amount'].sum().reset_index()
print("\nSales by month:")
print(sales_by_month)

#Save the data
df_orders.to_csv("./output/orders.csv", index=False)
sales_by_customer.to_csv("./output/sales_by_customer.csv", index=False)
sales_by_month.to_csv("./output/sales_by_month.csv", index=False)
df_orders.to_parquet("./output/orders.parquet", index=False)

#Compare sizes
csv_size = os.path.getsize("./output/orders.csv") /1024
parquet_size = os.path.getsize("./output/orders.parquet") /1024

print(f"CSV size: {csv_size:.1f} KB")
print(f"Parquet size: {parquet_size:.1f} KB")
print(f"Parquet is {csv_size/parquet_size:.1f}x smaller")
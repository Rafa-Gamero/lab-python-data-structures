products =["t-shirt" , "mug", "hat", "book", "keychain"]

inventory = {}  

for product in products: 
   quantity = int(input(f"Ingrese la cantidad disponible de  {product}: "))
   inventory[product] = quantity
   
customer_orders = set()  

for i in range(3):
    order = input(f"Ingrese el nombre del producto que desea ordenar({i+1}/3): ").lower()
    if order in products:
        customer_orders.add(order)
print("\nProductos ordenados por el cliente:",customer_orders) 

total_products_ordered = len(customer_orders)
percentage_ordered = (total_products_ordered / len(products)) * 100
           
order_status = (total_products_ordered, percentage_ordered)

print("\nOrder Statistics:")
print(f"Total Products Ordered: {order_status[0]}")           
print(f"Percentage of Products Ordered: {order_status[1]:.2f}% ")

for order in customer_orders:
    if inventory[order] > 0:
        inventory[order] -= 1
        
print("\nInventario actualizado:")
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")        
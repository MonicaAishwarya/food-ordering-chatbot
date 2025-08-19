import pandas as pd

# Create a simple menu database
menu_data = {
    'Item': ['Pizza', 'Burger', 'Salad', 'Pasta', 'Soda'],
    'Price': [10, 5, 7, 9, 2],
    'Category': ['Main', 'Main', 'Side', 'Main', 'Drink']
}

menu_df = pd.DataFrame(menu_data)

# Simple ordering system
orders = []

def show_menu():
    print("\n--- MENU ---")
    print(menu_df[['Item', 'Price']].to_string(index=False))
    print("------------")

def take_order():
    show_menu()
    print("\nType the item name exactly as shown to order (or 'done' to finish)")
    
    while True:
        choice = input("What would you like to order? ").strip().title()
        
        if choice.lower() == 'done':
            break
            
        if choice in menu_df['Item'].values:
            item = menu_df[menu_df['Item'] == choice].iloc[0]
            orders.append(item)
            print(f"Added {choice} (${item['Price']}) to your order!")
        else:
            print("Item not found. Please choose from the menu.")

def show_receipt():
    if not orders:
        print("You haven't ordered anything yet!")
        return
    
    print("\n--- YOUR ORDER ---")
    total = 0
    for item in orders:
        print(f"{item['Item']}: ${item['Price']}")
        total += item['Price']
    print(f"\nTOTAL: ${total}")
    print("-----------------")

# Main program
print("Welcome to Simple Food Ordering System!")
while True:
    print("\nOptions:")
    print("1. View Menu")
    print("2. Order Food")
    print("3. View My Order")
    print("4. Exit")
    
    choice = input("What would you like to do? (1-4): ")
    
    if choice == '1':
        show_menu()
    elif choice == '2':
        take_order()
    elif choice == '3':
        show_receipt()
    elif choice == '4':
        print("Thank you for your order! Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-4.")
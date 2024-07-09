import json

def add_inventory(inventory):
    #Add a new item with details like name, quantity, price, and category.
    try:
        no_added=int(input("Enter the no.of added to be added in the inventory: "))
    
    except ValueError as e:
        print(f"An error occured: {e}")
        
    else:
        for i in range(no_added):
            inventory_id=input("Enter the inventory id: ")
            inventory_name=input("Enter the inventory name: ")
            inventory_quantity=int(input("Enter the quantity for inventory: "))
            inventory_price=float(input("Enter the price for inventory: "))
            inventory_category=input("Enter the category for inventory: ")
            print("\n")
            add_invt={
                inventory_id:{
                    "name"      :inventory_name,
                    "quantity"  :inventory_quantity,
                    "price"     :inventory_price,
                    "category"  :inventory_category
                }
            }
            inventory.update(add_invt)
        
    return inventory
    
def remove_inventory(inventory):
    try:
        inventory_id=input("Enter the inventory id which needs to be removed: ")
        print(inventory,inventory_id)
        if inventory_id in inventory:
            print("Are you sure, you want to remove the inventory. Press 1 for Yes, 2 for No:")
            remove_confirmation=int(input("Enter your choice: "))
            
            if remove_confirmation==1:
                del inventory[inventory_id]
                print("Inventory deleted")

            elif remove_inventory==2:
                print("Inventory removal cancelled")
            else:
                print("Enter the valid confirmation")
        else:
            print("Inventory ID doesn't exists")  

    except KeyError as e:
        print(f"An error occured {e}")
    except TypeError as e:
        print(f"An error occured {e}")
    except ValueError as e:
        print(f"Error occured {e}")      

def update_inventory(inventory):

    try:
        inventory_id=input("Enter the inventory id which needs to be updated: ")

    except KeyError as e:
        print(f"An Error occured {e}")
    except TypeError as e:
        print(f"Error occured {e}")
    except ValueError as e:
        print("Error Occured {e}")
    else:
        if inventory_id in inventory:
            in_name=input("Enter the inventory name which needs to be updated: ")
            in_quantity=int(input("Enter the quantity which needs to be updated: "))
            in_price=float(input("Enter the price which needs to be updated: "))
            in_category=input("Enter the category which needs to be updated: ")
            update_inventory={
                inventory_id:{
                    "name"      :in_name,
                    "quantity"  :in_quantity,
                    "price"     :in_price,
                    "category"  :in_category
                }
            }
            inventory.update(update_inventory)
        return inventory
    
def display_single_inventory(inventory):
    try:
        inventory_id=input("Enter the ID where you needs to see the details: ")
    except:
        print("Error occured")
    else:
        if inventory_id in inventory:
            print({inventory_id :inventory[inventory_id]})


def display_all_inventory(inventory):
    try:
        if len(inventory)>0:
            print("Available inventory\n")
            print(inventory)
        else:
            print("No items available in the inventory")
    except KeyError as e:
        print(f"Error occured {e}")

def total_value(inventory):
    try:
        
            total_price=0.0
            for id,inv in inventory.items():
                total_price += inv['price'] * inv['quantity']
            print(total_price)
    except KeyError as e:
        print(f"Error occured {e}")

def save_inventory(inventory):
    try:

        f=open("G:\Python1\inventory.txt", "w")
        json.dump(inventory,f)
        f.close()
        
        print()

    except Exception as e:
        print(f"Error occured: {e}")       

def main():
    inventory={}
    try:
        while True:
            print("***************************")
            print("Inventory Management System")
            print("***************************")
           
            print("Select the option from below")
            print("1. Add new item in the inventory management system.")
            print("2. Remove item from inventory management system.")
            print("3. Update the details of an existing item.")
            print("4. Display the details of a specific item by its ID.")
            print("5. Display all items in the inventory.")
            print("6. Calculate the total value of the inventory.")
            print("7. Save the inventory data to a file and load it from a file.")
            print("8. Exit")

            choice=int(input("Enter your choice: "))

            if choice==1:
                add_inventory(inventory)
                print(inventory)
            elif choice==2:
                remove_inventory(inventory)
            elif choice==3:
                update_inventory(inventory)
                print(inventory)
            elif choice==4:
                display_single_inventory(inventory)
            elif choice==5:
                display_all_inventory(inventory)
            elif choice==6:
                total_value(inventory)
            elif choice==7:
                save_inventory(inventory)
            elif choice==8:
                break
            else:
                print("Enter the valid input")

    except ValueError as e:
        print(f"An error occured: {e}")

if __name__ == "__main__":
    main()





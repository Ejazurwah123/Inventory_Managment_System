# print("Hello world..")
# First of all defining the class for User
class User:
    def __init__(self, username, passcode, authority):
        self.username = username
        self.passcode = passcode
        self.authority = authority
        

class Item:
    def __init__(self, item_id, item_name, item_category, cost, stock_level):
        self.item_id = item_id
        self.item_name = item_name
        self.item_category = item_category
        self.cost = cost
        self.stock_level = stock_level
        
    def display_item_detail(self):
        print(f"Item ID: {self.item_id}")
        print(f"Item Name: {self.item_name}")
        print(f"Item Category: {self.item_category}")
        print(f"Cost: {self.cost}")
        print(f"Stock Level: {self.stock_level}")
        
        
class Inventory_Management_System:
    def __init__(self):
        self.users_list = [
            User("admin","054321","Admin"),
            User("Urwah1","2249091","User"),
            User("Marwa","Mavo43","User"),
            User("Ahmed","Ahmed123","User"),
            User("Ali","Ali123","User") 
        ]
        self.current_user = None
        self.items = {}
        
    def Login_Sys(self, username, password):
        for user in self.users_list:
            if user.username == username and user.passcode == password:
                self.current_user = user
                print(f"Welcome, {user.username}")
                return True
        print("Invalid Details")
        return False
    
    def add_item(self,item01):
        if self.current_user.authority != "Admin":
            print('Only Admins are allowed to add products \n')
            return
        # handling the case where if the item already exists
        if item01.item_id in self.items:
            print(f"Item ID {item01.item_id} already exists")
            return
        
        # now add the product
        self.items[item01.item_id] = item01
        print(f"Item {item01.item_id} added successfully")
        
    def Edit_Item(self,itemid,name=None,cat=None,cost=None,stock_quantity=None):
        if self.current_user.authority != "Admin":
            print('Only Admins are allowed to edit products \n')
            return
        if itemid not in self.items:
            print(f"Item ID {itemid} does not exist")
            return
        item = self.items[itemid]
        if name:
            item.item_name = name
        if cat:
            item.category = cat
        if price is not None:
            item.cost = cost
        if stock_quantity is not None:
            item.stock_level = stock_quantity
        print(f"Item {itemid} edited successfully")
        
    def Remove_Item(self,item_id):
        if self.current_user.authority != "Admin":
            print('Only Admins are allowed to remove products \n')
            return
        if item_id not in self.items:
            print(f"Item ID {item_id} does not exist")
            return
        del self.items[item_id]
        print(f"Item {item_id} removed successfully")
        
        
    def See_Item(self):
        if not self.items:
            print("No items in the store")
            return
        # else print all items
        for item in self.items.values():
            print(item)
            
    def Search_Item(self,item_nam):
        found_check = [itm for itm in self.items.values() if name.lower() in itm.item_name.lower()]
        if not found_check:
            print(f"No item found with name {item_nam}")
            return
        for itms in found_check:
            print(itms)
            
    def Analyse_Stock_level(self,value_max=10):
        itm_low_in_stock = [itm for itm in self.items.values() if itm.stock_level<value_max]
        if not itm_low_in_stock:
            print("No items are low in stock")
            return
        for item in itm_low_in_stock:
            print("Low in Stock!!")
            print(item)
            
def main():
    
    System_Inv = Inventory_Management_System()
    print("Inventory Management System \n")
    while True:
        if System_Inv.current_user is None:
            print("Please login to access the system \n")
            usrname = input("Enter username: ")
            password = input("Enter password: ")
            if not System_Inv.Login_Sys(usrname,password):
                continue
        print("\nOptions: \n")
        print("1. Display Items")
        print("2. Insert Item (Admin Allowed only)")
        print("3. Edit Item (Admin Allowed Only)")
        print("4. Delete Item (Admin Allowed Only)")
        print("5. Search Item")
        print("6. Items Low in Stock")
        print("7. Sign-out")
        print("8. Exit System")
        
        usr_c = input("Choose an Option: ")
        
        if usr_c == "1":
            System_Inv.See_Item()
        
        elif usr_c == "2":
            if System_Inv.current_user.authority == "Admin":
                itm_id = input("Enter Item ID: ")
                itm_name = input("Enter Item Name: ")
                cat = input("Enter Item Category: ")
                cost = float(input("Enter Item Cost: "))
                stk = int(input("Enter Stock Quantity of Item: "))
                System_Inv.add_item(Item(itm_id,itm_name,cat,cost,stk))
            else:
                print("Access Denied")
        
        elif usr_c =="3":
            if System_Inv.current_user.authority == "Admin":
                itm_id = input("Enter Item ID to Edit: ")
                nm = input("Enter New Name: ")
                cat = input("Enter New Category: ")
                cost = input("Enter New Cost: ")
                cost = float(cost) if cost else None
                stk = input("Enter New Stock Quantity: ")
                stk = int(stk) if stk else None
                System_Inv.edit_item(itm_id,nm,cat,cost,stk)
            else:
                print("Access Denied")
        
        elif usr_c=="4":
            if System_Inv.current_user.authority == "Admin":
                itm_id = input("Enter Item ID to Delete: ")
                System_Inv.delete_item(itm_id)
            else:
                print("Access Denied")
        
        elif usr_c=="5":
            search = input("Enter Item Name to Search: ")
            System_Inv.search_item(search)
            
        elif usr_c=="6":
            nm = input("Enter Item to Search: ")
            System_Inv.Search_Item(nm)
            
        elif usr_c=="7":
            System_Inv.current_user=None
            print("You have been signed out")
        elif usr_c=="8":
            print("Exiting the System")
            
        else:
            print("Invalid option. Try Again")
            
            
if __name__ == "__main__" :
    main()
    
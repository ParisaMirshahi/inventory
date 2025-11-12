
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country=country 
        self.code=code
        self.product=product
        self.cost=float(cost)
        self.quantity=int (quantity) 
        
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    def get_cost(self):
        return self.cost
    
        '''
        Add the code to return the cost of the shoe in this method.
        '''

    def get_quantity(self):
        return self.quantity 
        '''
        Add the code to return the quantity of the shoes.
        '''

    def __str__(self):
        return f"country:{self.country},code:{self.code},product:{self.product},cost:{self.cost},quantity:{self.quantity}"
        '''
        Add a code to returns a string representation of a class.
        '''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    try:
        with open('inventory.txt','r') as file:
            #make each line in the file into a list
            #skip the first line
            lines=file.readlines()[1:] 
            for line in lines:
                parts=line.strip().split(",")
                #unpack data in each line and assign it to variables 
                country, code, product, cost, quantity = parts
                if len(parts)==5:
                    #create a shoe objective and append it to the shoe list
                    shoe=Shoe (country, code, product, float(cost), int(quantity))
                    shoe_list.append(shoe)
    except FileNotFoundError:
        print("inventory.txt file not found")
        #general error handling for other exceptions 
    except Exception as e:
        print(f"An error occurred: {e}")
        
                
        
        '''
        This function will open the file inventory.txt
        and read the data from this file, then create a shoes object with this data
        and append this object into the shoes list. One line in this file represents
        data to create one object of shoes. You must use the try-except in this function
        for error handling. Remember to skip the first line using your code.
        '''
def capture_shoes():
    country = input("enter a country:")
    code = input("Enter shoe code: ")
    product = input("Enter product name: ")
    cost = input("Enter cost: ")
    quantity = input("Enter quantity: ")
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    with open('inventory.txt','a')as file:
        file.write(f"\n{country},{code},{product},{cost},{quantity}")
    print("Shoe added successfully!")

    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

def view_all():
    if not shoe_list:
        print("no shoes in inventory")
    else:
        for shoe in shoe_list:
            print(shoe)
    
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

def re_stock():
    lowest_quantity_shoe = min(shoe_list, key=lambda shoe: shoe.get_quantity())
    print(f"shoe with lowest quantity is : {lowest_quantity_shoe.product} with quantity: {lowest_quantity_shoe.quantity}")
    add_quantity = int(input("Do you want to add quantity? Enter quantity to add: "))
    lowest_quantity_shoe.quantity += add_quantity 
    print(f"Updated quantity: {lowest_quantity_shoe.quantity}")
    #write updated data back to the file 
    with open('inventory.txt','w') as file:
        file.write("country,code,product,cost,quantity\n ")
        for shoe in shoe_list:
            file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
        
    
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def search_shoe():
    code_to_search = input("Enter shoe code to search: ").strip()
    for shoe in shoe_list:
        if shoe.code == code_to_search:
            print(f"shoe found:{shoe.product} in country:{shoe.country} with cost:{shoe.cost} and quantity:{shoe.quantity}")
            return shoe
    print("Shoe not found")
    return -1
    '''
    This function will search for a shoe from the list
    using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    for shoe in shoe_list:
        value= shoe.get_cost()*shoe.get_quantity()
        print(f"the total value for {shoe.product} is {value}")
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty():
    if not shoe_list:
        print("no shoes in inventory")
    else:
        highest_quantity=max(shoe_list, key=lambda shoe:shoe.get_quantity())
        print(f"hot sale:{highest_quantity.product} with quantity:{highest_quantity.quantity}")
        '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
def main_menu():
    read_shoes_data()
    while True:
        print("1. add shoe to inventory list ")
        print("2. view all shoes in inventory list ")
        print("3. restock shoe with lowest quantity ")
        print("4. search shoe by code ")
        print("5. calculate total value per item ")
        print("6. display shoe with highest quantity ")
        print("7. exit ")
        choice = input("Enter your choice (1-7): ")
        if choice == "1":
            capture_shoes()
        elif choice == "2":
            view_all()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            search_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")     
#call the main menu function  
main_menu()
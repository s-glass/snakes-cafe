def menu():
  print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************""")

menu()

# Create an empty dictionary and loop until user enters quit
# take order and check if that item already exists
# if it does, give it a key/value pair where key is item and value is number. then add 1 to it
# if it isn't in the dictionary already, add it

def user_order():
  menuItems = {}
  while True:
    user_input = input("> ")
    if user_input == "quit":
      break
    if user_input in menuItems:
      menuItems[user_input] += 1
    else:
        menuItems[user_input] = 1
    print(f"** {menuItems[user_input]} order(s) of {user_input} has been added to your meal**")
  print("quit")

if __name__ == "_main__":
  menu()
  user_order()
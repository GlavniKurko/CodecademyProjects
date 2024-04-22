from store import Store

print(''' __      __       .__                                ___________      ___________.__               _________ __                        
/  \    /  \ ____ |  |   ____  ____   _____   ____   \__    ___/___   \__    ___/|  |__   ____    /   _____//  |_  ___________   ____  
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \    |    | /  _ \    |    |   |  |  \_/ __ \   \_____  \\   __\/  _ \_  __ \_/ __ \ 
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/    |    |(  <_> )   |    |   |   Y  \  ___/   /        \|  | (  <_> )  | \/\  ___/ 
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >   |____| \____/    |____|   |___|  /\___  > /_______  /|__|  \____/|__|    \___  >
       \/       \/          \/            \/     \/                                   \/     \/          \/                         \/''')
print("Welcome Shopper!")
print("Are you ready to shop?\n")
user_input = input("Yes or No: ")

def main():
    try:
        user_name = str(input("Enter your name: "))
        user_object = Store(user_name)

    except Exception as error:
        print(error)

    user_object.get_inventory()
    
    user_cart = input("Enter a list of items you want to purchase [separated by commas: Carrots,Vanilla Ice Cream]: ")
    user_cart = user_cart.split(",")

    user_object.purchase_items(user_cart)

if user_input.lower() == "yes":
    main()
else:
    print("We look forward to seeing you shop with us next time!")
class Store:
    def __init__(self, shopper_name):
        self.shopper_name = shopper_name
        print(f"Welcome {self.shopper_name}!")
    
    def get_inventory(self):
        ice_cream = ["Vanilla Ice Cream", "Strawberry Ice Cream", "Chocolate Ice Cream", "Superman Ice Cream", "MooseTracks Ice Cream"]
        vegetables = ["Carrots", "Beans", "Asparagus", "Broccoli", "Celery"]
        fruits = ["Oranges", "Bananas", "Strawberrys", "Mangos", "Peaches"]
        store_inventory = {"Ice Cream": ice_cream, "Vegetables": vegetables, "Fruits": fruits}

        print("\n")
        print("Here is our current inventory: ")
        print(store_inventory.get("Ice Cream"))
        print(store_inventory.get("Vegetables"))
        print(store_inventory.get("Fruits"))
    
    def purchase_items(self, items):
        cart = []
        prices = {"Oranges": .50, "Bananas": 1.00, "Strawberrys": 1.50, "Mangos": 1.00, "Peaches": 1.00, "Vanilla Ice Cream": 2.00, "Strawberry Ice Cream": 3.00, "Chocolate Ice Cream": 2.00, "Superman Ice Cream": 5.00, "MooseTracks Ice Cream": 10.00, "Carrots": 0.75, "Beans": 1.00, "Asparagus": 1.00, "Broccoli": 1.00, "Celery": 1.00}
        total = 0
        for x in items:
            cart.append(x)
        
        for x in cart:
            total += prices.get(x)

        print(f"Here are the items in your cart: {cart}")
        print(f"You are due {total}")
        print("Thank you for shopping with us!")

'''
Product inside the Department
'''

import random

class Product:
    def __init__(self, policy = 'No returns. No exchanges after 60 days!', product = []):
        self.policy = policy # private; class-unqiue attribute
        self.product = product # protected; Only used and passed through to cart

    def disclaimer(self): # private; uses the private policy attribute
        return f'Reminder about our store policies: {self.policy}'
    
    def insert_obj(self): # protected; only passed on to cart
        object = input('Enter the name of your item and we will add that to your order: ')
        self.product.append(object)
        return f'{self.product}\n'

    def random_item(self): # protected; shared and used with cart only
        groceries = ['Ketchup', 'Bread', 'Rice', 'Soup', 'Milk', 'Chips', 'Beans', 'Sparkling Water', 'Soda', 'Lettuce', 'Grapes', 'Bottled Water']
        clothes = ['Levi Shorts', 'Tank Top', 'Graphic Tee', 'Leggings', 'Mom Jeans', 'Crew Socks', 'Button Up', 'Pajama Pants', 'Baseball Cap', 'Belt']
        product_dept = ['groceries', 'clothing'] 
        chosen = input('Please choose a department (Groceries or Clothing): ').lower()
        while chosen in product_dept:
            if chosen == product_dept[0]:
                item = random.choice(groceries)
                self.product.append(item)

            elif chosen == product_dept[1]:
                item = random.choice(clothes)
                self.product.append(item)
            return f'{self.product} added.'

        while chosen not in product_dept:
            return f'Please choose from one of the listed departments.'
        
prod = Product(3)
print(prod.insert_obj())
print(prod.random_item())
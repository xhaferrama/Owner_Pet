###############################################################################
#import the following that allows me to complete the implementations successfully
import pet
import turtle

################################################################################
class owner:
    '''The class creats an object, the pet in this case, that it will interact with pet object'''
    max_money = 1000
    def __init__(self, name_for_pet = 'cujo'):
        '''The constructor for this object.'''
        self.money = 500
        self.food_bag = 100
        self.house_animal = pet.pet(name_for_pet)#creates an instance of the object pet

################################################################################
#The folllowing draws the shape, size, and color of the pet
        self.house_animal.body.shape('circle')
        self.house_animal.body.resizemode('user')
        self.house_animal.body.shapesize(5, 8)
        self.house_animal.body.color('hotpink')
################################################################################
# the function that makes sure the pet is fed
    def feed(self, amount = 10):
        '''The following makes sure the pet if fed and each time it is fed it
        decreased a total amount of 10 from the bag'''
        self.house_animal.increase_hunger(amount*(-1))
        self.food_bag += -amount

################################################################################
# the following makes sure the pet has been played with
    def play(self):
        '''After the owner has interacted with the pet, the pet risks its health,
        hunger, and energy level. This tracks by how much these levels
        increase or decrease'''
        self.house_animal.increase_health(15)
        self.house_animal.increase_hunger(-15)
        self.house_animal.increase_energy(-10)
################################################################################
# the following makes sure that there more food is added to the bag
    def buy_food(self, amount_to_buy = 40):
        '''The following adds more food to the bank and if there is low cash, it
        alerts the user that they do not have a sufficient amount of cash'''
        if self.money >= amount_to_buy:
            #print("Balance" + str(self.money))
            self.money -= amount_to_buy
            self.food_bag += amount_to_buy
        else:
            print('Low balance. Your current balance is: $' + str(self.money))
################################################################################

################################################################################
import time
import turtle
################################################################################
class pet:
    '''Encompases the data and methods that are possible with the pet'''
    #max_hunger = 100
    max_energy = 100
    max_toilet = 100
    max_health = 100
    def __init__(self, pet_name = 'Peto'):
        '''The constructor makes sure we have set some characteristics for the
        pet such as hunger or energy level. The name of the pet will be taken as
        a parameter '''

        self.hunger_level = 0
        self.happiness_level = 50
        self.name = pet_name
        self.energy_level = 100
        self.toilet_need = 20
        self.health_level = 100
        self.body = turtle.Turtle()

################################################################################
# The following function is concerned with the hunger level of the pet
    def increase_hunger(self, increase_by = 15):
        '''It will increase the number of hunger by 15'''
        self.hunger_level += increase_by
        if self.hunger_level > 100: # the following makes sure the hunger level doesnt go above than 100 or lower than 0
            self.hunger_level = 100
        elif self.hunger_level < 0:
            self.hunger_level = 0

################################################################################
# The following function is concerned with the energy the pet uses
    def increase_energy(self, increase_by = 0):
        '''The function increases the energy used by the pet making sure it does not
        exceed 100 or go below 0. As the pet plays the energy is dropped down by 10'''
        self.energy_level += increase_by
        if self.energy_level > 100:
            self.energy_level = 100
        elif self.energy_level < 0:
            self.increase_hunger(20)
            self.energy_level = 0

################################################################################
# The following is concerned with the health of the pet
    def increase_health(self, increase_by = -10):
        '''It will decrease the health of the pet by 10. It makes sure the health
        level does not go above 100 or below 0'''
        self.health_level += increase_by
        if self.health_level > 100:
            self.health_level = 100
        elif self.health_level < 0:
            self.health_level = 0

################################################################################
# I imported the following to help me with my implementation
import sched, time, pet, owner
import turtle, Tkinter
################################################################################

name_for_pet = ''
name_for_pet = raw_input('Pick a creative name for your pet please?: ') # asks the user to input the name of his/her pet
if name_for_pet != '':
    win = turtle.Screen()
    win.screensize(620,480) #adjusts the window/canvas size
    Me = owner.owner(name_for_pet)
else:
    win = turtle.Screen()
    win.screensize(620,480)
    Me = owner.owner()

################################################################################

#The following draws a ball using a turtle to represent the hunger level of the dog
button_feed = turtle.Turtle()
button_feed.penup()
button_feed.setpos(-280, 220)
button_feed.shape('circle')
button_feed.color('blue')
button_feed.shapesize(3)

################################################################################
#The following draws a ball using a turtle to represent the amount of food that is available for the dog
button_buy_food = turtle.Turtle()
button_buy_food.penup()
xpos, ypos = button_feed.pos() # sets the position of the turtle
button_buy_food.setpos(xpos + 180, ypos)
button_buy_food.shape('circle')
button_buy_food.shapesize(3)

################################################################################
# The following draws the ball using a turtle to represent the amount of health the pet has
button_play = turtle.Turtle()
button_play.penup()
xpos, ypos = button_buy_food.pos() #sets the position of the turtle
button_play.setpos(xpos + 180, ypos)
button_play.shape('circle')
button_play.shapesize(3)

#button_play = turtle.Turtle()

################################################################################
# The three handler functions for feed, buy, and play
def handler_feed(x,y):
    '''Handler for the turtle button_feed and it will print
         the hunger level as the title of the window'''
    Me.feed(20)
    button_feed.color('red')
    win.title('Hunger level is: ' + str(Me.house_animal.hunger_level)) #refers back to the hunger level

def handler_buy(x,y):
    ''' Handler for the turtle button_buy_feed and it will print
        the available amount of food left in the food bag'''
    Me.buy_food()
    button_buy_food.color('blue')
    win.title('The available amount of food is: ' + str(Me.food_bag)) #refers back to the food bag

def handler_play(x,y):
    '''Handler for the turtle button_play and it will print the
        health of the pet'''
    Me.play()
    button_play.color('green')
    win.title('The health of the pet is: ' + str(Me.house_animal.hunger_level))# refers back to the hunger level

################################################################################
#create a turtle called turtle2 that helps the user to know what balls to click when taking care of the pet
turtle2 =turtle.Turtle()
turtle2.penup()
turtle2.setpos(-329, 160)
turtle2.pendown()
turtle2.write ('The three balls above help you know the hunger level, food available, and pet health. Click on them to take care of your pet.', move = False,  font=("Arial", 9, "normal"))
################################################################################
#create a turtle called turtle3 that helps the user recognize his/her pet
turtle3=turtle.Turtle()
turtle3.penup()
turtle3.setpos(-160,10)
turtle3.write ('This giant ball is your pet!' , move = False,  font=("Arial", 9, "normal"))
################################################################################



################################################################################
# The following is my main function; it shows the hunger level, health level, and energy level as the title of the window
def decrement_hunger(): # the job of this function is to reduce everything
    ''' It determines the amount to decrease/increase the hunger, health, and energy level.
    It makes sure that the amounts of the different levels are printed as they are reduced or increased that
    way the user is aware what is going on with the dog. Then calls the function end_game() that will
    clear the window and end the game '''
    Me.house_animal.increase_hunger(15)
    Me.house_animal.increase_health()
    Me.house_animal.increase_energy(-10)
    win.title('Hunger level is : ' + str(Me.house_animal.hunger_level) + '. ' + 'Health level is : ' +str(Me.house_animal.health_level) +'. ' 'Energy level is : ' + str(Me.house_animal.energy_level))
    end_game() #calls the function end_game() to end the game
    win.ontimer(decrement_hunger, 3000)



################################################################################
# The following function ends the game after it has been called by decrement_hunger()
def end_game():
    '''When the health of the pet and the energy of the pet have hit the value of 0
    that means that the pet is going to die thus this function makes sure the game ends
    by cleaing everything and closing the window. '''
    if Me.house_animal.health_level == 0 and Me.house_animal.energy_level == 0:
        win.clear() # clears the window
        turtle1 =turtle.Turtle()
        #turtle1.write(arg, move=False, align="left", font=("Arial", 8, "normal"))
        turtle1.penup()
        turtle1.setpos(-280, 180)
        turtle1.pendown()
        turtle1.write ('You havent taken care of your poor pet : ' + str(Me.house_animal.name) +' Shame on you!', move = False,  font=("Arial", 15, "normal"))
        time.sleep(10) # waits ten seconds for the window to close
        win.bye()
################################################################################


### def decrement_happines():
###     Me.house_animal.increase_health(15)
###     win.title('The health level is: ' + str(Me.house_animal.health_level))
###     win.ontimer(decrement_happines, 3000)
##


################################################################################
#This is where we call the handlers and also our main function decrement_hunger


button_feed.onclick(handler_feed)
button_buy_food.onclick(handler_buy)
button_play.onclick(handler_play)
decrement_hunger()

################################################################################
    ### This is where we call the handlers
    ##button_feed.onclick(handler_feed)
    ##button_buy_food.onclick(handler_buy)
    ##button_play.onclick(handler_play)


##print(Me.house_animal.hunger_level)
###while True:
## #   event_timer = sched.scheduler.()
################################################################################
Tkinter.mainloop()

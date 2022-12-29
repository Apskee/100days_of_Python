#Goal of this project is to navigate a robot through the maze to reach the exit, using functions which define direction for the robot.
#Fuction turn_left() and move() is pre-defined in the website.
#LINK: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json


##### SOLUTION #####
#Defining function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()
      
#While loop to repeat steps until goal is reached     
while not at_goal():
    while not wall_on_right(): #Following the right wall, if wall is not or the right, turn right and move until it is.
        turn_right()
        move()
    if front_is_clear(): #If wall is on the right and front is clear move forward.
        move()
    elif wall_in_front(): #If wall is in front.
        if wall_on_right == False: #If no wall on right and wall in front turn right.
            turn_right()
            move()
        else:
           turn_left() #If wall in front and wall is on right, turn left.
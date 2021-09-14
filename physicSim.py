# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()

    #set window title
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 300 x 200
    (width, height) = (300, 200)
    screen = pygame.display.set_mode((width, height))

    #set a background color
    background_color = (255,255,255) #white
    screen.fill(background_color)
     
    # define a variable to control the main loop
    running = True

    pygame.display.flip()
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
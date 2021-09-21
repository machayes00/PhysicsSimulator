# import the pygame module, so you can use it
import pygame



# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()

    #set window title
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 300 x 200
    (width, height) = (1000, 600)
    screen = pygame.display.set_mode((width, height))

    #set a background color
    background_color = (255,255,255) #white
    screen.fill(background_color)
     
    # define a variable to control the main loop
    running = True

    pygame.display.flip()

    clock = pygame.time.Clock()

    # Game FPS
    FPS = 60

    # Set circle position and velocity
    circle_x_pos = 250
    circle_y_pos = 250
    circle_x_vel = 150
    circle_y_vel = 20
    circle_radius = 50
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        clock.tick(FPS)

        screen.fill(background_color)

        if(circle_x_pos+circle_radius >= width or circle_x_pos-circle_radius <=0):
            circle_x_vel *= -1
        if(circle_y_pos+circle_radius >= height):
            circle_y_vel *= -.5
        # Update circle position
        circle_x_pos += circle_x_vel / FPS
        circle_y_pos += circle_y_vel / FPS
        circle_y_vel+=2

        pygame.draw.circle(screen, (255,0,0), (int(circle_x_pos), int(circle_y_pos)), int(circle_radius))
        

        pygame.display.update()

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
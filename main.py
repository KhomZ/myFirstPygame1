#/*
# Introduction to PyGame

# Welcome to the introduction to PyGame and Python 3 video gaming programming!
# Suggested Requirements for this series
# You may wish to be familiar with the basics of the Python 3 programming
# language, or at least the basics of Programming in general

# That said, this course begins at a slowish pace, and I do my best to explain
# everything at least the first time it shows up. PyGame can actually be a wonderful
# starting place for your journey in Python.

# First, you're going to need PyGame!

# @author khom
# @ikhomkodes

import pygame

pygame.init()
# Above, we've imported PyGame, which is obviously necessary to make use of the
# module! Then, we run pygame.init(), which is integral to every single PyGame
# application that you will ever write. This will initiate PyGame, and allows you to
# then make various commands with PyGame and our game.


display_width = 800
display_height = 600


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
# Next, we define our game's display, which is the main "display" for our game. You
# may also see this referred to as a "surface", as this is basically our canvas that
# we will draw things to, and the function literally returns a pygame. Surface object. We
# are saying right now that we want the resolution of our game to be 800 px wide
# and 600 px tall. Take note that this is a tuple as a function argument. If you do not
# make this a tuple with parenthesis, then 600 and 800 will be treated as separate
# parameters and the function will blow up. It's a big deal.

# After that, we define our display's "caption". To me, it's more like a title, and is the
# title of the window. We've decided to call our game "A bit Racey".(tm!)


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()
# Simple enough, this is our game clock. We use this to track time within the
# game, and this is mostly used for FPS, or "frames per second". While somewhat
# trivial seeming, FPS is very important, and can be tweaked as we will see later.
# For the most part, the average human eye can see ~30 FPS. It's important to note,
# however, that this is only a very general statement, since every human eye is
# slightly different, and the human eye does not process things in "frames". The
# better way to put it is that after about 30 FPS, people generally cannot tell the
# difference.

# Take that 60 FPS YouTube. Anyway, we can increase FPS to literally speed up the
# game, or slow them down to slow down the game. This isn't ideal, especially
# when speeding up FPS, as the entire game loop is run per frame, and might be a
# massive waste of processing. More on this later though!
#

carImg = pygame.image.load('racecar.png')

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

x = (display_width * 0.45)
y = (display_height * 0.8)


crashed = False


while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    car(x, y)

    pygame.display.update()
    clock.tick(60)
#
# Okay, a bit more here. I don't like to separate loops and functions it I don't have to,
# since it can cause people to get indentation wrong. So, first, we've got a crashed = False
# statement, which is just a variable that we set initially. Then, we run out
# "game loop", which will run until we crash. Currently, the only way we're saying
# crashed = True is if the user exits out of the window, however.

# You'll notice here that we have a for loop within this while loop. This is going to be
# present in most PyGame scripts, where events are constantly being logged. It is
# shown in the video, but not here, but you can still try it: Try adding "print event"
# above the if statement. You will see in your console everything you do within the
# PyGame window. Pretty neat!

# After our if statement. you'll see that we run a pygame.display.update. It's
# important to note the difference between display.update and display.flip.
# Display.flip will update the entire surface. Basically the entire screen.
# Display.update can just update specific areas of the screen. That said, if you do
# not pass a parameter, then update will update the entire surface as well, basically
# making flip() pointless for our interests. There might come times when you want
# to use flip for very specific tasks, however.

# The last thing within this while loop is clock.tick(60). Basically, this is how many
# frames per second we are running. In this case, we are running 60 FPS.
#


pygame.quit()
quit()
# Once we have broken our game loop, we want to run a pygame.quit(). This will
# end our pygame instance. Then we can run a simple quit(), which exit Python
# and the application.

#
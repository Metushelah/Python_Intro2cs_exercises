# FILE: circleTorpedo.py
# WRITER : konstantin, guybrush, 30888377
# EXERCISE : intro2cs ex8 2014-2015
# DESCRIPTION:
# This file holds the CircleTorpedo Class
# a torpedo that moves in circles

import math
from baseObject import BaseObject
from objectShapes import TORPEDO_SHAPE

class CircleTorpedo(BaseObject):
    """
    This class creates a new torpedo type object similar to the normal torpedo
    but that moves in a circle around an origin point in a radius dependent
    on the speed.
    It recieves the screen size from the calling program (Runner) inorder to
    make the movement "pass through screens" like in moveObject method
    """
    SIZE = 4
    TORPEDO_LIFESPAN = 200

    def __init__(self,canvas,x,y,dx,dy,direction,scr_xmin,scr_xmax,
                                                            scr_ymin,scr_ymax):
        """
        This creates a torpedo object similar to the normal torpedo only it 
        adds an axis attribute to move around it, a radius of movement
        depending on speed and saves the screen size to allow flowing movement
        """
        super().__init__(canvas,x,y,dx,dy,TORPEDO_SHAPE,direction,
                                                            CircleTorpedo.SIZE)
        self.circle_radius = (math.sqrt(dx ** 2 + dy ** 2) * \
                                    self.TORPEDO_LIFESPAN / (2 * math.pi))
        self.axis = (x+self.circle_radius * math.cos(math.radians(direction)),
                     y+self.circle_radius * math.sin(math.radians(direction)))
        self.set_color("Blue")
        self.lifespan = CircleTorpedo.TORPEDO_LIFESPAN
        self.scr_xmin = scr_xmin
        self.scr_xmax = scr_xmax
        self.scr_ymin = scr_ymin
        self.scr_ymax = scr_ymax
        

    def get_life_span(self):
        """
        return the torpedoes lifespan attribute
        """
        return self.lifespan

    def move(self):
        """
        This method updates the torpedos movement around its original axis
        """
        self.lifespan = self.lifespan - 1
        self.increase_angle()
        delta_x = self.scr_xmax - self.scr_xmin
        delta_y = self.scr_ymax - self.scr_ymin
        cord_x = (self.scr_xmin + ((self.axis[0] + self.circle_radius *\
         math.cos(math.radians(self.get_angle()))) + self.scr_xmin) % delta_x)
        cord_y = (self.scr_ymin + ((self.axis[1] + self.circle_radius *\
         math.sin(math.radians(self.get_angle()))) + self.scr_ymin) % delta_y)
        super().move(cord_x, cord_y)


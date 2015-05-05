# FILE: -----------.py
# WRITER : konstantin, guybrush, 30888377
# EXERCISE : intro2cs ---------- 2014-2015
# DESCRIPTION:
# ------------------------
# ------------------------

from torpedo import *
from asteroid import *
from spaceship import *
from gameMaster import *

from math import radians, sin, cos, sqrt
import sys
from circleTorpedo import *


class GameRunner:
    """
    This class holds the game runner functions to play the asteroids game
    """
    TORPEDO_MAX = 20
    TOR_SPD_INCRS_COEF = 2
    DEFAULT_SCORES = [100, 50, 20]  # this list holds the default scores for 
    MIN_AST_SIZE = 1                # the astroids and should be the same len
                                    # as the sizes of astroids in game to
                                    # function properly. We assume difference
                                    # between astroids is 1 otherwise DEFAULT
                                    # SCORES list and the function 
                                    #_astroid_boom should be updated


    def __init__(self, amnt = 3):
        """
        Same as the init before only it initializes a new binding to key e
        inorder to shot the special torpedos
        """
        self.game = GameMaster()
        self.screenMaxX = self.game.get_screen_max_x()
        self.screenMaxY = self.game.get_screen_max_y()
        self.screenMinX = self.game.get_screen_min_x()
        self.screenMinY = self.game.get_screen_min_y()
        shipStartX = (self.screenMaxX-self.screenMinX)/2 + self.screenMinX
        shipStartY = (self.screenMaxY-self.screenMinY)/2 + self.screenMinY
        self.game.set_initial_ship_cords( shipStartX, shipStartY )
        self.game.add_initial_astroids(amnt)
        self._bind_key_e()

    
    def run(self):
        self._do_loop()
        self.game.start_game()


    def _do_loop(self):
        self.game.update_screen()
        self.game_loop()
        # Set the timer to go off again
        self.game.ontimer(self._do_loop,5)


    def _bind_key_e(self):
        """
        This method bind the w key as the key to fire the special torpedo
        """
        self.game.get_original_game_handler().bind_key("e",
                                                     self._fire_circle_torpedo)
        
        
    def _fire_circle_torpedo(self):
        """
        This method add a new circular torpedo to the torpedo list
        """
        if len(self.torpedo_list) < self.TORPEDO_MAX:
            tor_cord_x = self.ship.get_x_cor()
            tor_cord_y = self.ship.get_y_cor()
            tor_spd_x = self.ship.get_speed_x()
            tor_spd_y = self.ship.get_speed_y()
            tor_direction = self.ship.get_angle()
            torpedo = CircleTorpedo(self.game._cv, tor_cord_x, tor_cord_y,
                                         tor_spd_x, tor_spd_y, tor_direction,
                                         self.screenMinX, self.screenMaxX,
                                         self.screenMinY, self.screenMaxY )
            self.game.get_original_game_handler().add_original_torpedo(torpedo)
    
    
    def _get_primaries(self):
        """
        This method acts as an initialization for the values to use before
        each loop iteration so to avoid unnecessary repeated calls.
        :return: None
        """
        self.torpedo_list = self.game.get_torpedos()
        self.asteroid_list = self.game.get_asteroids()
        self.ship = self.game.get_ship()
        self.torpedoes_to_remove = []
        self.asteroids_to_remove = []


    def _moveObject(self, object):
        """
        This method receives an object and uses it's move function to pass
        to it a new coordinate to move to keeping sure it's not going out of
        the screen on the game. This function assumes the object has the move
        command as it is working inside the whole of the game and the user
        cannot access it.
        :param object: will be a type of baseObject (ship, asteroids, torpedo)
        :return: None
        """
        current_x = object.get_x_cor()              #init
        current_y = object.get_y_cor()
        old_speed_x = object.get_speed_x()
        old_speed_y = object.get_speed_y()
        x_delta = self.screenMaxX - self.screenMinX
        y_delta = self.screenMaxY - self.screenMinY

        new_x_cord = (self.screenMinX + (old_speed_x + current_x -
                                         self.screenMinX) % x_delta)

        new_y_cord = (self.screenMinY + (old_speed_y + current_y -
                                         self.screenMinY) % y_delta)

        object.move(new_x_cord, new_y_cord)


    def _move_asteroids(self):
        """
        This method updates the position of the asteroids. It makes them look
        like moving.
        :return: None
        """
        for asteroid in self.asteroid_list:
           self._moveObject(asteroid)


    def _move_ship(self):
        """
        This method updates the ships position each iteration according to its
        initial values and the keys pressed by the User.
        :return: None
        """
        if self.game.is_right_pressed():
            self.ship.increase_angle()
        elif self.game.is_left_pressed():
            self.ship.decrease_angle()
        elif self.game.is_up_pressed():
            new_speed_x = self.ship.get_speed_x() + \
                                        cos(radians(self.ship.get_angle()))
            new_speed_y = self.ship.get_speed_y() + \
                                        sin(radians(self.ship.get_angle()))
            self.ship.set_speed_x(new_speed_x)
            self.ship.set_speed_y(new_speed_y)

        self._moveObject(self.ship)


    def _shot_torpedo(self):
        """
        This method creates a torpedo object if the User pressed the fire key.
        :return: None
        """
        if self.game.is_fire_pressed() and\
                                    len(self.torpedo_list) < self.TORPEDO_MAX:
            tr_speed_x = self.ship.get_speed_x() + \
                  self.TOR_SPD_INCRS_COEF * cos(radians(self.ship.get_angle()))
            tr_speed_y = self.ship.get_speed_y() + \
                  self.TOR_SPD_INCRS_COEF * sin(radians(self.ship.get_angle()))

            self.game.add_torpedo(self.ship.get_x_cor(),
                                  self.ship.get_y_cor(),
                                  tr_speed_x,
                                  tr_speed_y,
                                  self.ship.get_angle())


    def _update_torpedoes(self):
        """
        This method updates the position of the torpedoes existing in the game
        and marks them for removal when their life span is up
        :return: None
        """
        for torpedo in self.torpedo_list:
            if torpedo.get_life_span() <= 0:
                self.torpedoes_to_remove.append(torpedo)
            elif type(torpedo) == PhotonTorpedo:
                self._moveObject(torpedo)
            else:
                torpedo.move() #Circle Torpedo move command


    def _asteroid_boom(self):
        """
        This method checks if our asteroids have been hit by a torpedo and
        if so it creates 2 new asteroids in its place and adds it to be removed
        from the game.
        
        This method assumes the sizes of the astroids are 3,2,1 and nothing
        else, therfore the numbers used are to deal with this 
        :return: None
        """
        
        for torpedo in self.torpedo_list:
            for asteroid in self.asteroid_list:
                if self.game.intersect(torpedo, asteroid):
                    self.torpedoes_to_remove.append(torpedo)
                    self.asteroids_to_remove.append(asteroid)
                    size = asteroid.get_size()
                    score_to_add = self.DEFAULT_SCORES[size - 1]
                    if size > self.MIN_AST_SIZE:
                        cord_x = asteroid.get_x_cor()
                        cord_y = asteroid.get_y_cor()
                        x_speed = ((torpedo.get_speed_x() +
                                   asteroid.get_speed_x()) /
                                           sqrt(asteroid.get_speed_x()**2 +
                                                asteroid.get_speed_y()**2))
                        y_speed = ((torpedo.get_speed_y() +
                                   asteroid.get_speed_y()) /
                                           sqrt(asteroid.get_speed_x()**2 +
                                                asteroid.get_speed_y()**2))
                        
                        new_size = size - 1   #assumes difference between
                                              #asteroid sizes is 1 as explained
                                              #above
                        self.game.add_asteroid(cord_x, cord_y, x_speed,
                                                         y_speed, new_size)
                        self.game.add_asteroid(cord_x, cord_y, -x_speed,
                                                        -y_speed, new_size)

                    self.game.add_to_score(score_to_add)


    def _remove_destroyed(self):
        """
        This method removes objects in the game that were marked for removal
        :return: None
        """
        self.game.remove_torpedos(self.torpedoes_to_remove)
        for asteroid in self.asteroids_to_remove:
            self.game.remove_asteroid(asteroid)


    def _ship_hit_asteroid(self):
        """
        This method checks if our ship has hit an asteroid and prints a
        message if it did
        :return: None
        """
        show_message = False
        for asteroid in self.asteroid_list:
            if self.game.intersect(self.ship, asteroid):
                self.asteroids_to_remove.append(asteroid)
                self.game.ship_down()
                show_message = True

        if show_message:
            self.game.show_message("Mayday Mayday", "An astroid has hit "
                                "our ship, need to be more careful next time")


    def _check_if_end(self):
        """
        This method checks if any of the conditions for ending the game have
        been met (quit button, no more lives, asteroids destroyed)
        :return: None (exits the game)
        """
        show = False
        if self.game.should_end():
            show = True
            title, msg = "Exiting the Game", "See you next time tiger!"
        elif self.game.get_num_lives() < 1:
            show = True
            title, msg = "This was our last Ship!", "Back to training for"\
                                                            " you soldier!"
        elif len(self.asteroid_list) == 0:
            show = True
            title, msg = "Earth is Saved!", "Great job kid, All asteroids"\
                                                    " are destroyed! Hooza!"
        if show:
            self.game.show_message(title,msg)
            self.game.end_game()


    def game_loop(self):
        """
        This method iterates and updates the game
        :return: None
        """
        #This is where your code goes!
        # "It starts !" - Lion King the game
        self._get_primaries()
        self._move_asteroids()
        self._move_ship()
        self._shot_torpedo()
        self._update_torpedoes()
        self._asteroid_boom()
        self._ship_hit_asteroid()
        self._remove_destroyed()
        self._check_if_end()


def main():
    """
    The main function that runs the game
    :return: None
    """
    DEFAULT_ASTEROID_AMOUNT = 3

    asteroid_amount = DEFAULT_ASTEROID_AMOUNT
    if len(sys.argv) == 2:
        asteroid_amount = int(sys.argv[1])
    runner = GameRunner(asteroid_amount)
    runner.run()

if __name__ == "__main__":
    main()

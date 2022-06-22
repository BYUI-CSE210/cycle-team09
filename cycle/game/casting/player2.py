import constants
from game.casting.actor import Actor
from game.shared.point import Point

class Player2(Actor):
    """
    A player that leaves a trail behind it.

    The responsibility of player 1 is to move itself.

    Attributes:
        _trail (list): The number of points the food is worth.
    """

    def __init__(self):
        """construct a new instace of the player 1"""
        
        super().__init__()
        self._trail = []
        self.player_color = constants.RED
        self._is_game_over = False
        self._prepare_player()
    
    def get_trail(self):
        """returns the trail created by the player 1"""

        return self._trail[1:]

    def get_player(self):
        """gets the player or the first element in the trail list"""

        return self._trail[0]

    def turn_player(self, velocity):
        """moves the player to the velocity passed
        
        Args: 
            Velocity (int): new velocity to move the player to
        """

        self._trail[0].set_velocity(velocity)
    
    def _prepare_player(self):
        """Prepares the player and the initial trail to be drawn"""

        x = int((constants.MAX_X / 2) + ((constants.MAX_X / 2) / 2))
        y = int(constants.MAX_Y / 2)

        for i in range(constants.TRAIL_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(constants.CELL_SIZE, 0)
            text = "@" if i == 0 else "#"

            trail = Actor()
            trail.set_position(position)
            trail.set_velocity(velocity)
            trail.set_text(text)
            trail.set_color(self.player_color)
            self._trail.append(trail)
    
    def move_next(self):
        """moves the player"""

        self._trail[0].move_next()
    
    def grow_trail(self):
        """grows the trail of the player"""

        player = self._trail[0]
        velocity = player.get_velocity()
        position = player.get_position()

        trail = Actor()
        trail.set_position(position)
        trail.set_velocity(velocity)
        trail.set_text("#")
        trail.set_color(self.player_color)
        self._trail.append(trail)
        
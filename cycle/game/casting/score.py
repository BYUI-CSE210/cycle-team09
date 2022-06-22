from game.casting.actor import Actor

class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by forcing 
    a colission with the oponent.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """

    def __init__(self, player):
        """creates new instance of the actor score"""

        super().__init__()
        self._points = 0
        self._player = player
        self._is_game_over = False
        self.add_points(0)
        
    def add_points(self, points):
        """Adds the points to the total score for player 1
        
        Args:
            points (int): The points earned after a colission
        """

        if not self._is_game_over:
            self._points += points
        
        self.set_text(f"{self._player} Score: {self._points}")
    
    def set_game_over(self, game_over):
        """Sets the game over value to true
        
        Args:
            game_over (bool) = defines when the game is over"""

        self._is_game_over = game_over
    
    def get_score(self):
        """gets the value of the score"""

        return self._points

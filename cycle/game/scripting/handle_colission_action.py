import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when a snake collides
    with the other snake, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """
    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
        
            self._handle_segment_collision(cast)
            self.handle_snakes_collition(cast)
            self._handle_game_over(cast)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        """P1"""
        player = cast.get_first_actor("snakes")
        player1 = player[0]
        player2 = player[1]
        head_p1 = player1.get_segments()[0]
        head_p2 = player2.get_segments()[0]
        segments_p1 = player.get_segments()[1:]
        segments_p2 = player2.get_segments()[1:]
       
        

        for segment in segments_p1:
            if head_p1.get_position().equals(segment.get_position()):
                self._is_game_over = True

        for segment in segments_p2:
            if head_p2.get_position().equals(segment.get_position()):
                self._is_game_over = True

    def handle_snakes_collition(self, cast):
        """Sets the game over flag if the snake collides with a segment of the other snake 
        or with the head of the other snake
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player = cast.get_first_actor("snakes")
        player1 = player[0]
        player2 = player[1]
        head_p1 = player1.get_segments()[0]
        head_p2 = player2.get_segments()[0]
        segments_p1 = player1.get_segments()[1:]
        segments_p2 = player2.get_segments()[1:]

        for segment in segments_p2:
            if head_p1.get_position().equals(segment.get_position()):
                self._is_game_over = True
                
        for segment in segments_p1:
            if head_p2.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
        
        if head_p1.get_position().equals(head_p2.get_position()):
                self._is_game_over = True   
        


    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snakes  white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            player = cast.get_first_actor("snakes")
            player1 = player[0]
            player2 = player[1]
            segments_p1 = player1.get_segments()
            segments_p2 = player2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments_p1:
                segment.set_color(constants.WHITE)

            for segment in segments_p2:
                segment.set_color(constants.WHITE)
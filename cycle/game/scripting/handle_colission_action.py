import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when a player collides
    with the other player's trail, and vice versa, or the game is over.

    Attributes:
        is_game_over (boolean): Whether or not the game is over.
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
            self._handle_trail_collision(cast)
            self.handle_player_collition(cast)
            self._handle_game_over(cast)

    def _handle_trail_collision(self, cast):
        """Sets the game over flag if the player collides with its own trail.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        
        #get both players
        players = cast.get_actors("players")
        player1 = players[0]
        player2 = players[1]
        head_p1 = player1.get_player()
        head_p2 = player2.get_player()
        trail_p1 = player1.get_trail()
        trail_p2 = player2.get_trail()
       #get the scores
        scores = cast.get_actors("scores")
        score_p1 = scores[0]
        score_p2 = scores[1]

        #if player one collides with its own trail
        for trail in trail_p1:
            if head_p1.get_position().equals(trail.get_position()):
                self._is_game_over = True
                #add points to the other player
                score_p2.add_points(100)
                #stop adding points to the score
                score_p1.set_game_over(True)
                score_p2.set_game_over(True)

        #if player two collides with its own trail
        for trail in trail_p2:
            if head_p2.get_position().equals(trail.get_position()):
                self._is_game_over = True
                #add points to the other player
                score_p1.add_points(100)
                #stop adding points to the score
                score_p1.set_game_over(True)
                score_p2.set_game_over(True)

    def handle_player_collition(self, cast):
        """Sets the game over flag if the player collides with the trail of the other player 
        or with the head of the other player
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        #get both players
        player = cast.get_actors("players")
        player1 = player[0]
        player2 = player[1]
        head_p1 = player1.get_player()
        head_p2 = player2.get_player()
        trail_p1 = player1.get_trail()
        trail_p2 = player2.get_trail()
        #get the scores
        scores = cast.get_actors("scores")
        score_p1 = scores[0]
        score_p2 = scores[1]

        #if player one collides with player two trail
        for trail in trail_p2:
            if head_p1.get_position().equals(trail.get_position()):
                self._is_game_over = True
                #add points to the other player
                score_p2.add_points(100)
                #stop adding points to the scores
                score_p1.set_game_over(True)
                score_p2.set_game_over(True)

        #if player two collides with player one trail      
        for trail in trail_p1:
            if head_p2.get_position().equals(trail.get_position()):
                self._is_game_over = True
                #add points to the other player 
                score_p1.add_points(100)
                #stop adding points to the scores
                score_p1.set_game_over(True)
                score_p2.set_game_over(True)
        
        #if both players collide at the same time
        if head_p1.get_position().equals(head_p2.get_position()):
                self._is_game_over = True 
                #stop adding points to the scores (draw)
                score_p1.set_game_over(True)
                score_p2.set_game_over(True)  

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the players and trails white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        if self._is_game_over:
            #get the players
            player = cast.get_actors("players")
            player1 = player[0]
            player2 = player[1]
            #get both trails
            trail_p1 = player1.get_trail()
            trail_p2 = player2.get_trail()

            #get the scores
            scores = cast.get_actors("scores")
            score_p1 = scores[0].get_score()
            score_p2 = scores[1].get_score()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            if score_p1 > score_p2:
                message = Actor()
                message.set_text("Game Over!\nPlayer 1 Wins")
                message.set_position(position)
                message.set_color(constants.BLUE)
                cast.add_actor("messages", message)
            
            elif score_p1 < score_p2:
                message = Actor()
                message.set_text("Game Over!\nPlayer 2 Wins")
                message.set_position(position)
                message.set_color(constants.BLUE)
                cast.add_actor("messages", message)
            
            else: 
                message = Actor()
                message.set_text("Game Over!\nDraw!")
                message.set_position(position)
                message.set_color(constants.BLUE)
                cast.add_actor("messages", message)

            player1.player_color = constants.WHITE
            player2.player_color = constants.WHITE

            for trail in trail_p1:
                trail.set_color(constants.WHITE)

            for trail in trail_p2:
                trail.set_color(constants.WHITE)
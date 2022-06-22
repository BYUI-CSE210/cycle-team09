import constants

from game.casting.cast import Cast
from game.casting.player1 import Player1 
from game.casting.player2 import Player2
from game.casting.score import Score
from game.scripting.script import Script
from game.scripting.control_player1_action import ControlPlayer1Action
from game.scripting.control_player2_action import ControlPlayer2Action
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_colission_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():

    #create scores
    #Player 1
    p1_score = Score("P1")
    #Player 2 / move the position of the score to the right
    p2_score = Score("P2")
    p2_score.set_position(Point(((15 * constants.CELL_SIZE) + (35 * constants.CELL_SIZE)), 0 * constants.CELL_SIZE))

    # create the cast
    cast = Cast()
    cast.add_actor("players", Player1())
    cast.add_actor("players", Player2())
    cast.add_actor("scores", p1_score)
    cast.add_actor("scores", p2_score)

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    #create the script
    script = Script()
    script.add_action("input", ControlPlayer1Action(keyboard_service))
    script.add_action("input", ControlPlayer2Action(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()
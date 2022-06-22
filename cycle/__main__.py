import constants

from game.casting.cast import Cast
from game.casting.player1 import Player1
from game.casting.player2 import Player2
from game.casting.p1_score import P1Score
from game.casting.p2_score import P2Score
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

    # create the cast
    cast = Cast()
    cast.add_actor("players", Player1())
    cast.add_actor("players", Player2())
    cast.add_actor("scores", P1Score())
    cast.add_actor("scores", P2Score())

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

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
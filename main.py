"""
Add-ons for Anki 2.1+ to support learning chess using Anki.

There is only one add-on at the moment, namely **replace_fen_with_svg**.
It replaces a Forsyth–Edwards Notation (FEN) of a chess position
with an SVG. The FEN string must be enclosed by a FEN tag pair.
The opening FEN tag is `[fen]` ;the closing FEN tag is `[/fen]`.

There are a few options to configure the svg output.
The default values of the options are in config.json and the schema is in
config.schema.json.
"""
import chess
import chess.svg

import re
from random import randrange

import anki
from aqt import gui_hooks
from aqt import mw

__version__ = '0.1.0'


config = mw.addonManager.getConfig(__name__)


def get_status_string(status: chess.Status) -> str:
    """Error in position and state obtained from fen."""
    problems = []
    if (status & chess.STATUS_NO_BLACK_KING or
            status & chess.STATUS_NO_WHITE_KING or
            status & chess.STATUS_TOO_MANY_KINGS):
        problems.append("Bad King")
    if (status & chess.STATUS_BAD_CASTLING_RIGHTS):
        problems.append("Bad castling rights")
    if (status & chess.STATUS_OPPOSITE_CHECK or
            status & chess.STATUS_RACE_CHECK or
            status & chess.STATUS_TOO_MANY_CHECKERS):
        problems.append("Bad check")
    if (status & chess.STATUS_TOO_MANY_BLACK_PAWNS or
            status & chess.STATUS_TOO_MANY_WHITE_PAWNS or
            status & chess.STATUS_PAWNS_ON_BACKRANK):
        problems.append("Bad pawns")
    if (status & chess.STATUS_TOO_MANY_BLACK_PIECES or
            status & chess.STATUS_TOO_MANY_WHITE_PIECES):
        problems.append("Bad pieces")
    if status & chess.STATUS_INVALID_EP_SQUARE:
        problems.append("Invalid e.p. square")

    return "<ul align='left'>" + "".join(["<li>" + p + "</li>" for p in problems]) + "</ul>"


def get_orientation(board: chess.Board) -> chess.Color:
    """Determine board image orientation from config option _orientation_."""
    side = config["orientation"]
    if side == "auto":
        if board.turn == chess.WHITE:
            orientation = chess.WHITE
        else:
            orientation = chess.BLACK
    elif side == "random":
        orientation = chess.WHITE if randrange(2) else chess.BLACK
    else:
        orientation = chess.WHITE if side == "white" else chess.BLACK
    return orientation


def replace_fen_with_svg(text: str, card: anki.cards.Card, kind: str) -> str:
    """Replace FEN string of a chess position with an svg of the position."""
    fen_pattern = re.compile(r"\[fen\](.+?)\[/fen\]", re.DOTALL | re.IGNORECASE)
    match = fen_pattern.search(text)
    if match:
        fen = match.group(1)
        try:
            board = chess.Board(fen)

            if not board.is_valid():
                status_string = get_status_string(board.status)
                return text + "<br><p align='left'>Invalid FEN:</p>" + status_string

            size = config["size"]
            orientation = get_orientation(board)

            if config["move"]:
                piece_size = size / 10
                move_piece = chess.PAWN
                if board.turn == chess.WHITE:
                    piece = chess.Piece(move_piece, chess.WHITE)
                else:
                    piece = chess.Piece(move_piece, chess.BLACK)
                move_svg = chess.svg.piece(piece, piece_size)
            else:
                move_svg = ""

            svg = chess.svg.board(board, orientation=orientation,
                                  coordinates=config["coordinate"], size=size)
            return re.sub(fen_pattern, svg + move_svg, text)

        except Exception as error:
            return text + "<br><p>Error: " + str(error) + "</p>"
    else:
        return text + "<br><p>FEN not found.</p>"


gui_hooks.card_will_show.append(replace_fen_with_svg)

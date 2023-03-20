
from app.lib.board import Board
import json

def test_get_index_of_square_1(snapshot):
    board = Board()
    pgn = """
    1. e4 Nc6 2. d4 e6 3. Nf3 d5 4. e5 b6 5. Bb5 Bd7 6. Bg5 Qc8 7. Bxc6 Bxc6 8. O-O
Qd7 9. Nbd2 Be7 10. Bf4 g6 11. c3 O-O-O 12. b4 f6 13. a4 fxe5 14. Bxe5 Nf6 15.
b5 Bb7 16. h3 Rhf8 17. Bxf6 Bxf6 18. Re1 h5 19. h4 Qf7 20. a5 bxa5 21. Rxa5 Kd7
22. Rxa7 Ba8 23. b6 Rc8 24. Qa4+ Ke7 25. Rxc7+ Rxc7 26. bxc7 Bxh4 27. Nxh4 Qxf2+
28. Kh2 Qxh4+ 29. Kg1 Qf2+ 30. Kh1 Qxe1+ 31. Kh2 Qxd2 32. Qb4+ Kf7 33. Qxf8+
Kxf8 34. c8=Q+ Kf7 35. Qxa8 Kf6 36. Qf8+ Kg5 37. Kh3 Qe3+ 38. g3 h4 39. Qe7+ Kh5
40. Qxh4# 1-0
    """

    result = board.pgn2fen(pgn)
    snapshot.assert_match(json.dumps(result, indent=2), "pgn2fen_test_output_1.json")

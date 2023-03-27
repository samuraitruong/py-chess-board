
"""Test module"""
import json
from app.lib.board import Board


def test_pgn2fen_1(snapshot):
    """Test get_index_of_square"""
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
    snapshot.assert_match(json.dumps(result, indent=2),
                          "pgn2fen_test_output_1.json")


def test_pgn2fen_2(snapshot):
    """Test get_index_of_square"""
    board = Board()
    pgn = """
      1. d4 d5 2. f3 Nf6 3. Nc3 c6 4. h3 e6 5. b4 Bxb4 6. Bd2 c5 7. Nb1 Bxd2+ 8. Qxd2 c4 9. e4 dxe4 10. Bxc4 O-O 11. Qe2 exf3 12. gxf3 Nc6 13. Nc3 Nxd4 14. Qd3 e5 15. O-O-O Qa5 16. h4 b5 17. Bxb5 Ba6 18. Bxa6 Qxa2 19. Nxa2 Rfd8 20. Bb7 Rab8 21. Bd5 Rxd5 22. Nb4 Rxb4 23. c3 Nb3+ 24. Kc2 Rxd3 25. Rxd3 Na1+ 26. Kd2 Rb2+ 27. Ke3 Nc2+ 28. Kd2 Nb4+ 29. Ke3 Nfd5+ 30. Rxd5 Nxd5+ 31. Ke4 Nxc3+ 32. Kxe5 a5 33. Nh3 f6+ 34. Kf5 Rb5+ 35. Kg4 g6 36. Kg3 Ne2+ 37. Kf2 Nd4 38. Rg1 Rb2+ 39. Kg3 Nf5+ 40. Kg4 Nh6+ 41. Kg3 f5 42. f4 Rb3+ 43. Kh2 Ng4+ 44. Kg2 Rc3 45. Ng5 Rc2+ 46. Kh1 Nf2+ 47. Kh2 Nd3+ 48. Rg2 Rxg2+ 49. Kxg2 a4 50. Nf3 a3 51. Nd2 a2 52. Nb3 Nxf4+ 53. Kf3 Nd3 54. Ke3 Nc1 55. Nxc1 a1=Q 56. Nb3 Qe1+ 57. Kd3 Qe4+ 58. Kc3 Qf3+ 59. Kc2 Qe4+ 60. Kc3 Qxh4 61. Kc2 Qg4 62. Nd2 h5 63. Kd3 Qg3+ 64. Ke2 h4 65. Nf3 h3 66. Kf1 Qg2+ 0-1
    """

    result = board.pgn2fen(pgn)
    snapshot.assert_match(json.dumps(result, indent=2),
                          "pgn2fen_test_output_2.json")

## Introduction

This is the python API to render the chessboard as images from FEN input, it supports various piece sets and themes.  The most popular use of this may be  the website that displays puzzle
## Development
```sh
python3 -m venv .venv
 . .venv/bin/activate
 ./start.sh
```

If you prefer development with docker just simply run

```sh
docker compose up

```

To debug the board with the cell index, just need to set DEBUG=1 when running the application

```sh
DEBUG=1 ./start.sh

```

The live demo deployed on: https://chess-board.fly.dev

For a quick test please visit http://localhost:8080/playground or https://chess-board.fly.dev/playground. it contains a simple html page allows changes in the input and seeing the image in the live demo

<img width="900" alt="image" src="https://user-images.githubusercontent.com/1183138/226876151-198f8614-adb9-4d18-971f-8c2b76bd47f9.png">


## API params
### Generate board image from FEN
- **fen**: the valid FEN string of the board
- **size**: the size of the output image
- **theme**: color theme of the board support (orange, green, bw and default)
- **piece**: the piece set name, please refer below to see the full list
- **viewer**: b or w to
- **frame**: true|false or 0:1 if false, the board border will be trimmed
example
```
curl https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&theme=orange&size=500
```

### Generate gif from PGN
- **pgn**: the valid FEN string of the board
- **size**: the size of the output image
- **theme**: color theme of the board support (orange, green, bw and default)
- **piece**: the piece set name, please refer below to see the full list
- **duration**: the duration between 2 move default 1000ms
- **total_duration**: the animation length of the gif, this will overwrite the duration parameter if provided
- **arrow**: true|false or 0:1 to draw the move arrow indicating the start and end square
- **frame**: true|false or 0:1 if false, the board border will be trimmed

Some PGN examples (you can get more from unit tests)

```
1. e4 Nc6 2. d4 e6 3. Nf3 d5 4. e5 b6 5. Bb5 Bd7 6. Bg5 Qc8 7. Bxc6 Bxc6 8. O-O Qd7 9. Nbd2 Be7 10. Bf4 g6 11. c3 O-O-O 12. b4 f6 13. a4 fxe5 14. Bxe5 Nf6 15. b5 Bb7 16. h3 Rhf8 17. Bxf6 Bxf6 18. Re1 h5 19. h4 Qf7 20. a5 bxa5 21. Rxa5 Kd7 22. Rxa7 Ba8 23. b6 Rc8 24. Qa4+ Ke7 25. Rxc7+ Rxc7 26. bxc7 Bxh4 27. Nxh4 Qxf2+ 28. Kh2 Qxh4+ 29. Kg1 Qf2+ 30. Kh1 Qxe1+ 31. Kh2 Qxd2 32. Qb4+ Kf7 33. Qxf8+ Kxf8 34. c8=Q+ Kf7 35. Qxa8 Kf6 36. Qf8+ Kg5 37. Kh3 Qe3+ 38. g3 h4 39. Qe7+ Kh5 40. Qxh4# 1-0
```

```

1. e4 Nc6 2. d4 e6 3. Nf3 d5 4. e5 b6 5. Bb5 Bd7 6. Bg5 Qc8 7. Bxc6 Bxc6 8. O-O
Qd7 9. Nbd2 Be7 10. Bf4 g6 11. c3 O-O-O 12. b4 f6 13. a4 fxe5 14. Bxe5 Nf6 15.
b5 Bb7 16. h3 Rhf8 17. Bxf6 Bxf6 18. Re1 h5 19. h4 Qf7 20. a5 bxa5 21. Rxa5 Kd7
22. Rxa7 Ba8 23. b6 Rc8 24. Qa4+ Ke7 25. Rxc7+ Rxc7 26. bxc7 Bxh4 27. Nxh4 Qxf2+
28. Kh2 Qxh4+ 29. Kg1 Qf2+ 30. Kh1 Qxe1+ 31. Kh2 Qxd2 32. Qb4+ Kf7 33. Qxf8+
Kxf8 34. c8=Q+ Kf7 35. Qxa8 Kf6 36. Qf8+ Kg5 37. Kh3 Qe3+ 38. g3 h4 39. Qe7+ Kh5
40. Qxh4# 1-0


1. f4 e6 2. Nf3 d5 3. e3 Nf6 4. d4 Bb4+ 5. Bd2 Bxd2+ 6. Qxd2 Ne4 7. Qb4 Nc6 8. Qb3 O-O 9. Bd3 b6 10. O-O a5 11. a4 Ba6 12. c4 Nb4 13. Ng5 Nxg5 14. fxg5 Nxd3 15. Qxd3 Bxc4 16. Qc2 Bxf1 17. Kxf1 Qxg5 18. Qf2 Rac8 19. h4 Qh5 20. Nd2 c5 21. Rc1 c4 22. Nb1 Rb8  3. b3 b5 24. axb5 cxb3 25. Na3 a4 26. Rc7 Qf5 27. Rc1 Qxf2+ 28. Kxf2 Rfc8 29. Rc5 g6 30. g4 h5 31. gxh5 gxh5 32. Kf3 f5 33. Nb1 Kf8 34. Nc3 a3 35. Rc6 a2 36. Na4 a1=Q 37. Kf4 Qxa4 38. Ra6 Qxb5 39. Rxe6 Qf1+ 40. Ke5 Re8 41. Kxd5 Rxe6 42. Kxe6 Qe2 43. d5 Qxe3+ 44. Kf6 Qf4 45. d6 Rb6 46. Kg6 Rxd6+ 47. Kh7 Qxh4 48. Kh8 Qg4 49. Kh7 Qg7# 0-1


1. b4 d5 2. b5 c5 3. bxc6 a5 4. cxb7 f6 5. bxa8=Q e6 6. c4 g5 7. c5 h6 8. c6 Bd6 9. c7 Ne7 10. cxb8=Q g4 11. f4 e5 12. Nf3 d4 13. Nxe5 Qb6 14. Nxg4 Rf8 15. Qa4+ Kf7 16. Qxb6 Bxg4 17. Qbb3+ Kg6 18. Qc2+ Kh5 19. Q8xa5+ Nd5 20. Qxd5+ f5 21. Qxd6 Rf6 22. Qxf6 d3 23. Qc5 dxe2 24. Bxe2 Bxe2 25. g4+ Kxg4 26. Qcxf5+ Kf3 27. Rf1+ Kg2 28. Rf2+ Kg1 29. Q5g5+ Kh1 30. h4 hxg5 31. Qxg5 Bf1 32. Rxf1+ Kh2 33. f5 Kh3 34. h5 Kh2 35. h6 Kh3 36. h7 Kh2 37. h8=Q# 1-0

```
Test URL for above PGN

```
http://localhost:8080/gif?duration=500&pgn=e4%20Nc6%202.%20d4%20e6%203.%20Nf3%20d5%204.%20e5%20b6%205.%20Bb5%20Bd7%206.%20Bg5%20Qc8%207.%20Bxc6%20Bxc6%208.%20O-O%20Qd7%209.%20Nbd2%20Be7%2010.%20Bf4%20g6%2011.%20c3%20O-O-O%2012.%20b4%20f6%2013.%20a4%20fxe5%2014.%20Bxe5%20Nf6%2015.%20b5%20Bb7%2016.%20h3%20Rhf8%2017.%20Bxf6%20Bxf6%2018.%20Re1%20h5%2019.%20h4%20Qf7%2020.%20a5%20bxa5%2021.%20Rxa5%20Kd7%2022.%20Rxa7%20Ba8%2023.%20b6%20Rc8%2024.%20Qa4+%20Ke7%2025.%20Rxc7+%20Rxc7%2026.%20bxc7%20Bxh4%2027.%20Nxh4%20Qxf2+%2028.%20Kh2%20Qxh4+%2029.%20Kg1%20Qf2+%2030.%20Kh1%20Qxe1+%2031.%20Kh2%20Qxd2%2032.%20Qb4+%20Kf7%2033.%20Qxf8+%20Kxf8%2034.%20c8=Q+%20Kf7%2035.%20Qxa8%20Kf6%2036.%20Qf8+%20Kg5%2037.%20Kh3%20Qe3+%2038.%20g3%20h4%2039.%20Qe7+%20Kh5%2040.%20Qxh4#%201-0


http://localhost:8080/gif?duration=500&pgn=1. f4 e6 2. Nf3 d5 3. e3 Nf6 4. d4 Bb4+ 5. Bd2 Bxd2+ 6. Qxd2 Ne4 7. Qb4 Nc6 8. Qb3 O-O 9. Bd3 b6 10. O-O a5 11. a4 Ba6 12. c4 Nb4 13. Ng5 Nxg5 14. fxg5 Nxd3 15. Qxd3 Bxc4 16. Qc2 Bxf1 17. Kxf1 Qxg5 18. Qf2 Rac8 19. h4 Qh5 20. Nd2 c5 21. Rc1 c4 22. Nb1 Rb8  3. b3 b5 24. axb5 cxb3 25. Na3 a4 26. Rc7 Qf5 27. Rc1 Qxf2+ 28. Kxf2 Rfc8 29. Rc5 g6 30. g4 h5 31. gxh5 gxh5 32. Kf3 f5 33. Nb1 Kf8 34. Nc3 a3 35. Rc6 a2 36. Na4 a1=Q 37. Kf4 Qxa4 38. Ra6 Qxb5 39. Rxe6 Qf1+ 40. Ke5 Re8 41. Kxd5 Rxe6 42. Kxe6 Qe2 43. d5 Qxe3+ 44. Kf6 Qf4 45. d6 Rb6 46. Kg6 Rxd6+ 47. Kh7 Qxh4 48. Kh8 Qg4 49. Kh7 Qg7# 0-1

```

## Lint code before commit
```sh

pylint **/*.py


```
Format code

```sh

autopep8 --in-place --recursive .

```
## Request with custom FEN

```

http://localhost:8080/?fen=4k3/8/8/8/8/8/4P3/4K3%20w%20-%20-%205%2039

or

http://localhost:8080/?fen=1b1q1Bn1/2pPrN1b/4Qp2/P1k5/1p1N1Rn1/1P1p4/1R1P4/4K2B
```

Custom theme:
```
http://localhost:8080/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3&piece=chessmonk&theme=green
```

## Piece set

### default
![default](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=default&size=400 "default")
### spatial
![spatial](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=spatial&size=400 "spatial")
### skulls
![skulls](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=skulls&size=400 "skulls")
### sittuyin
![sittuyin](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=sittuyin&size=400 "sittuyin")
### regular
![regular](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=regular&size=400 "regular")
### prmi
![prmi](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=prmi&size=400 "prmi")
### pirouetti
![pirouetti](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=pirouetti&size=400 "pirouetti")
### libra
![libra](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=libra&size=400 "libra")
### letter
![letter](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=letter&size=400 "letter")
### freak
![freak](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=freak&size=400 "freak")
### fantasy_alt
![fantasy_alt](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=fantasy_alt&size=400 "fantasy_alt")
### fantasy
![fantasy](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=fantasy&size=400 "fantasy")
### eyes
![eyes](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=eyes&size=400 "eyes")
### chessicons
![chessicons](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessicons&size=400 "chessicons")
### celtic
![celtic](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=celtic&size=400 "celtic")
### set1
![set1](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=set1&size=400 "set1")
### alila
![alila](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=alila&size=400 "alila")
### chess7
![chess7](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chess7&size=400 "chess7")
### horsey
![horsey](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=horsey&size=400 "horsey")
### gioco
![gioco](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=gioco&size=400 "gioco")
### kosal
![kosal](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=kosal&size=400 "kosal")
### pixel
![pixel](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=pixel&size=400 "pixel")
### magnetic
![magnetic](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=magnetic&size=400 "magnetic")
### riohacha
![riohacha](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=riohacha&size=400 "riohacha")
### pirat
![pirat](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=pirat&size=400 "pirat")
### california
![california](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=california&size=400 "california")
### alpha
![alpha](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=alpha&size=400 "alpha")
### cardinal
![cardinal](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=cardinal&size=400 "cardinal")
### companion
![companion](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=companion&size=400 "companion")
### chessnut
![chessnut](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessnut&size=400 "chessnut")
### atopdown
![atopdown](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=atopdown&size=400 "atopdown")
### alfonso
![alfonso](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=alfonso&size=400 "alfonso")
### cburnett
![cburnett](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=cburnett&size=400 "cburnett")
### dubrovny
![dubrovny](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=dubrovny&size=400 "dubrovny")
### freestaunton
![freestaunton](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=freestaunton&size=400 "freestaunton")
### fresca
![fresca](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=fresca&size=400 "fresca")
### governor
![governor](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=governor&size=400 "governor")
### icpieces
![icpieces](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=icpieces&size=400 "icpieces")
### kilfiger
![kilfiger](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=kilfiger&size=400 "kilfiger")
### leipzig
![leipzig](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=leipzig&size=400 "leipzig")
### makruk
![makruk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=makruk&size=400 "makruk")
### maya
![maya](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=maya&size=400 "maya")
### metaltops
![metaltops](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=metaltops&size=400 "metaltops")
### shapes
![shapes](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=shapes&size=400 "shapes")
### reillycraig
![reillycraig](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=reillycraig&size=400 "reillycraig")
### tatiana
![tatiana](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=tatiana&size=400 "tatiana")
### staunty
![staunty](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=staunty&size=400 "staunty")
### maestro
![maestro](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=maestro&size=400 "maestro")
### merida
![merida](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=merida&size=400 "merida")
### merida_new
![merida_new](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=merida_new&size=400 "merida_new")
### chessmonk
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")

## Theme

### Default Theme -https://chess-board.fly.dev?theme=default
![Default](https://chess-board.fly.dev "default")


### Green Theme - https://chess-board.fly.dev?theme=green
![Default](https://chess-board.fly.dev?theme=green "default")

### Orange - https://chess-board.fly.dev?theme=orange
![Orange theme](https://chess-board.fly.dev?theme=orange "Orange")



### Black and White - https://chess-board.fly.dev?theme=bw
![BW](https://chess-board.fly.dev?theme=bw "default")


### Black and White - https://chess-board.fly.dev?theme=blue
![Blue](https://chess-board.fly.dev?theme=bw "blue")



## Credit

The project using multiple icons is licensed under the `Creative Commons Attribution` from flaticon.io
Most of the piece set come from lichess.org
- https://github.com/lichess-org/lila/tree/master/public/piece
- some board images and pieces come from chess.com

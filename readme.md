## Introduction

This is the python API to render the chessboard as image from FEN input, it supports various different piece set and themes.  The most popular use of this maybe  the website that display puzzle
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
The live demo deployed on: https://chess-board.fly.dev

## API params
### Draw chessboard with FEN input
- **fen**: the valid FEN string of the board
- **size**: the size of output image
- **theme**: color theme of the board support (orange, green, bw and default)
- **piece**: the piece set name, please refer below to see the full list

example
```
curl https://chess-board.fly.dev/??fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&theme=orange&size=500

### generate gif from pgn

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

```
## Lint code before commit
```

pylint $(git ls-files '*.py')

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


## Credit

The project using multiple icons is licensed under the `Creative Commons Attribution` from flaticon.io
Most of the piece set come from lichess
- https://github.com/lichess-org/lila/tree/master/public/piece
-

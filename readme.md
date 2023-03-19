## Development
```sh
python3 -m venv .venv
 . .venv/bin/activate
 ./start.sh
```
The live demo deployed on : https://chess-board.fly.dev
## Lint code before commit
```

pylint $(git ls-files '*.py')

```

## Request with custom FEN

```

http://localhost:8888/?fen=4k3/8/8/8/8/8/4P3/4K3%20w%20-%20-%205%2039

or

http://localhost:8888/?fen=1b1q1Bn1/2pPrN1b/4Qp2/P1k5/1p1N1Rn1/1P1p4/1R1P4/4K2B
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
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
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
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### chessnut
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### atopdown
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### alfonso
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### cburnett
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### dubrovny
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### freestaunton
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### fresca
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### governor
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### icpieces
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### kilfiger
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### leipzig
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### makruk
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### maya
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### metaltops
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### shapes
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### reillycraig
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### tatiana
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### staunty
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### maestro
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### merida
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### merida_new
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")
### chessmonk
![chessmonk](https://chess-board.fly.dev/?fen=8/4Kn2/1p1P2p1/Q1B2kp1/1P1r4/3P1N1P/4N1n1/1B2b3%20w%20-%20-%20a5%20&piece=chessmonk&size=400 "chessmonk")



## Credit

The project using multiple icons is licensed under the `Creative Commons Attribution` from flaticon.io
Most of the piece set come from lichess
- https://github.com/lichess-org/lila/tree/master/public/piece
-

## Development
```sh
python3 -m venv .venv
 . .venv/bin/activate
 ./start.sh
```
The live demo deployed on: https://chess-board.fly.dev
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

rr1 = float(input())
batsman1,batsman2 = list(map(int,input().split()))
scoreBoard = input().split()
rr2 = float(input())
ballsInInterval = 0
scoreInInterval = 0
for i in range(len(scoreBoard)):
    try:
        ballsInInterval +=1
        scoreBoard[i] = int(scoreBoard[i])
        scoreInInterval += scoreBoard[i]
    except:
        pass
balls = (6*scoreInInterval - len(scoreBoard)*rr2)//(rr2-rr1)
scoreInitial = balls*rr1/6
ballNumber = balls % 6
batsman1Strike = True
batsman2Strike = False
for i in range(len(scoreBoard)):
    if batsman1Strike and type(scoreBoard[i])==int:
        ballNumber += 1
        batsman1 += scoreBoard[i]
        if scoreBoard[i] % 2 != 0:
            batsman1Strike = False
            batsman2Strike = True
    elif batsman2Strike and type(scoreBoard[i])==int:
        ballNumber += 1
        batsman2 += scoreBoard[i]
        if scoreBoard[i] % 2 != 0:
            batsman2Strike = False
            batsman1Strike = True
    else:
        ballNumber += 1
        if batsman1Strike:
            batsman1 = 0
        else:
            batsman2 = 0
    if ballNumber == 6:
        batsman1Strike = not batsman1Strike
        batsman2Strike = not batsman2Strike
        ballNumber = 0
if batsman1Strike:
    print(int(scoreInitial + scoreInInterval), batsman1, batsman2)
else:
    print(int(scoreInitial + scoreInInterval), batsman2, batsman1)

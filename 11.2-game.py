import random
NumOfTry = 10
NumToGuess =random.randint(1,99)
LimitLow = 1
LimitHigh = 100
while NumOfTry != 0:
        try:
            print (NumToGuess)
            HumanAnswer  = input()
            if HumanAnswer == 'k':
                LimitHigh = NumToGuess
                NumOfTry = NumOfTry - 1
                NumToGuess = int (((LimitHigh - LimitLow)/2) + LimitLow)
                if NumToGuess <= LimitLow:
                    NumToGuess = NumToGuess + 1
                if LimitHigh - LimitLow == 2:
                    NumToGuess = LimitLow + 1
            elif HumanAnswer == 'b':
                LimitLow = NumToGuess
                NumOfTry = NumOfTry - 1
                NumToGuess = int (((LimitHigh - LimitLow)/2) + LimitLow)
                if NumToGuess <= LimitLow:
                    NumToGuess = NumToGuess + 1
                if LimitHigh - LimitLow == 2:
                    NumToGuess = LimitLow + 1
            elif HumanAnswer == 'd':
                NumOfTry = 0
        except:
            break
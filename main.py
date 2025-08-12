x = []
y = []
predY = []
datapoints = int(input("Number of data points: "))
print("Enter values for x")
for i in range(datapoints):
    userin = input("# ")
    x.append(float(userin))

print("Enter values for y")
for i in range(datapoints):
    userin = input("# ")
    y.append(float(userin))

print(x)
print(y)

epochs = int(input("Number of epoch u want: "))
alpha = float(input("Prefered alpha value: "))

for i in range(datapoints):
    predY.append(0.0)

def MSE(y, predY):
    length = len(y)
    difSum = 0.0
    for i in range(length):
        dif = y[i] - predY[i]
        sqdDif = dif*dif
        difSum = difSum + sqdDif
        MSEval = difSum * (1/length)
    print("MSE is", MSEval)


def findBetaNote(y, alpha, betaNote):
    length = len(y)
    difSum = 0.0
    for i in range(length):
        dif = y[i] - predY[i]
        print("y", y[i], "predY", predY[i])
        difSum = difSum + dif*2
    multipliedByLength = difSum / length
    multipliedByAlpha = multipliedByLength * alpha
    betaNote = betaNote + multipliedByAlpha

    print("Beta Note is ", betaNote)
    return betaNote

def findBetaOne(y, x, alpha, betaOne):
    length = len(y)
    difXSum = 0
    for i in range(length):
        dif = y[i] - predY[i]
        difMultipliedByX = -1 * dif * x[i] * 2
        difXSum = difXSum + difMultipliedByX
    multipliedByLength = difXSum/length
    multipliedByNegativeAlpha = multipliedByLength * alpha * -1
    betaOne = betaOne + multipliedByNegativeAlpha

    print("Beta one is: ", betaOne)
    return betaOne


def predict(betaNote, betaOne, xd):
    length = len(xd)
    for i in range(length):
        prediction = (betaOne * xd[i]) + betaNote
        predY[i] = prediction
    print("predictions: ", predY)

##MSE(y, predY)
##bn = findBetaNote(y, 0.01)
##bo = findBetaOne(y, x, 0.01)
##predict(bn, bo, x)
bn = 0.0
bo = 0.0
for i in range(epochs):
    MSE(y, predY)
    print("epoch: ", i)
    if i == 0:
        bn = findBetaNote(y, alpha, 0.0)
        bo = findBetaOne(y, x, alpha, 0.0)
        predict(bn, bo, x)
    else:
        bn = findBetaNote(y, alpha, bn)
        bo = findBetaOne(y, x, alpha, bo)
        predict(bn, bo, x)



    MSE(y, predY)

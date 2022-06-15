problemHeader = "The Problem"
problem = "A sheet of cardboard is rectangular, 25 cm long and 15 cm wide.\nCongruent squares are to be cut from their four corners.\nThe resulting piece of cardboard is to be folded and its edges taped to\nform an open-topped box.\nHow should this be done to get a box of the largest possible volume?"
b1t = "25cm x 15cm cardboard sheet"
b2t = "Congruent squares with side length x"
b3t = "Crease lines equal to SIDE - 2x"
at = "Box after folding"

optFuncL = ('V(x)=lwh')
optFuncX = ('V(x)=(25-2x)(15-2x)(x)')
optFuncSimp = ('V(x)=4x^3-80x^2+375x')
optFuncLabel = 'Optimization Function'

rangeOfX = 'Find the Range of X'
rangeFact1 = 'You cannot cut something negative'
rangeFact2 = 'The width of the box cannot be negative'
rf1eq = ('x\ge 0')
rf2eqA = ('15-2x\ge 0')
rf2eqB = ('15\ge 2x')
rf2eqC = ('\\frac{15}{2}\ge x')
rf2eqD = ('7.5\ge x')
finalRange = ('0\le x\le 7.5')

derivativeOfFunc = 'Derivative of the Optimization Function'
dxOfVx = ("V'(x)=12x^2-160x+375")

criticalPoint = 'Find the Critical Values'
cvPrompt = ("V'(x)=0")
equateTo0 = ("12x^2-160x+375=0")
xValues = ("x_1=3.03425; x_2=10.29908")
removeX2 = r'$x_2$ is out of range'
x1 = ("x=3.03425")

valueOfX = 'Value of X'
finalXValue = ('x=3.034')
finalXValueMeaning = 'To get the largest possible volume for the box,\nyou will need to cut 4 congruent squares in each corner of the cardboard\nwith a side length of 3.034cm'

maxVolume = 'Find the Max Volume'
maxVolume1 = 'V(x)=4x^3-80x^2+375x'
maxVolume2 = 'V(3.034)=4(3.034)^3-80(3.034)^2+375(3.034)'
maxVolumeValue = 'V(3.034)=513.05'

voiceover = 'Voiceover by:\nMariano, Eunice Reign\nChua, Arliyah Carmen\nDayao, Sophia Nicole'
script = 'Script by:\nDayao, Sophia Nicole'
videoEditor = 'Computation,\nVideo Editing,\nand Animation by:\nTabamo, Euan Jed S.'

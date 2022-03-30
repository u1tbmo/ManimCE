from manim import *
import numpy as np

#TEXT1
Ques1Prompt = Tex('How many pastry box sets do Giselle and Mark have to prepare to last all week if the formula of these boxes is:')
#Ques1Prompt.scale(0.5)
Ques1Eq = MathTex(r'b=\frac{x^4}{4^2+2^2+x}')
#Ques1Eq.scale(0.6)

Ques1 = VGroup(Ques1Prompt,Ques1Eq).arrange(DOWN).scale(0.6)
Ques1.to_edge(UP)

label1 = MathTex(r'\lim_{x\to7}{\frac{x^4}{4^2+2^2+x}}\ \approx 89')

#MATH1
plane1a = NumberPlane(
    x_range=[-8,8,1],
    y_range=[-2,8,1],
    x_length=14.22,
    y_length=8,
    background_line_style={
        "stroke_opacity":0.4
    }
)
graph1a = plane1a.plot(lambda x: np.divide(np.power(x,4),np.power(4,2)+np.power(2,2)+x),color=PURPLE)

plane1b = NumberPlane(
    x_range=[-1,14,1],
    y_range=[85,94,1],
    x_length=14.22,
    y_length=8,
    background_line_style={
        "stroke_opacity":0.4
    }
)

graph1b = plane1b.plot(lambda x: np.divide(np.power(x,4),np.power(4,2)+np.power(2,2)+x),color=PURPLE)
line1bX = DashedLine(plane1b.c2p(7,85),plane1b.c2p(7,94),color=RED)
line1bY = DashedLine(plane1b.c2p(-1,88.926),plane1b.c2p(14,88.926),color=GREEN)
point1b = Dot(plane1b.c2p(7,88.926),color=PURPLE)
point1bLabel = Tex(r'(x, b)=(7, 88.926)').next_to(point1b,(UP+LEFT)*0.4).scale(0.5)

#TEXT2
Ques2Prompt = Tex('What is the future value of Dray’s investment after 7 years?')
Ques2Prompt.scale(0.5)
Ques2Eq = MathTex(r'FV\left(t\right)=PV\left(1+\frac{r}{n}\right)^{nt}')
Ques2EqCopy = Ques2Eq.copy()
Ques2FinalEq = MathTex(r'FV\left(t\right)=50000\left(1+\frac{0.015}{4}\right)^{4t}')
Ques2FinalEqCopy = Ques2FinalEq.copy()
Ques2Eq.scale(0.6)

GivenPrompt = Tex('Given:')
pv = Tex('$PV$ = Php 50,000')
r = Tex("r = 0.015")
n = MathTex('n = 4')

Given = VGroup(GivenPrompt,pv,r,n).arrange(DOWN).scale(0.7)

Ques2 = VGroup(Ques2Prompt,Ques2Eq).arrange(DOWN)
Ques2.to_edge(UP)

label2 = MathTex(r'\lim_{t\to7}{50,000\cdot(1+\frac{0.015}{4})^{4t} }\approx55,524.63 \ ')

#MATH2
plane2a = NumberPlane(
    x_range=[-560,-460,10],
    y_range=[-20,60,15],
    x_length=14.22,
    y_length=8,
    background_line_style={
        "stroke_opacity":0.4
    }
)

graph2a = plane2a.plot(
    lambda t: 50000*(1+np.divide(0.015,4))**(4*t),
    color=TEAL
    )

plane2b = NumberPlane(
    x_range=[-20,20,8],
    y_range=[55400,55600,50],
    x_length=14.22,
    y_length=8,
    background_line_style={
        "stroke_opacity":0.4
    }
)

graph2b = plane2b.plot(
    lambda t: 50000*(1+np.divide(0.015,4))**(4*t),
    color=TEAL
    )

line2bX = DashedLine(
    plane2b.c2p(7,55400),
    plane2b.c2p(7,55600),
    color=RED
)
line2bY = DashedLine(
    plane2b.c2p(-20,55524.63),
    plane2b.c2p(20,55524.63),
    color=GREEN
)
point2b = Dot(plane2b.c2p(7,55524.63),color=TEAL)
point2bLabel = Tex('(x, t)=(7, 55,524.63)').next_to(point2b,(UP+RIGHT)*0.4).scale(0.5)
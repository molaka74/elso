'''Rajzol egy 150 pontos
egyenlő szárú háromszőget a képernyő közepére
A szine legyen piros
A rajzolás induljon a h betüre
Kilépés legyen q betüre
'''
import turtle

def haromszog():
    turtle.clear()
    turtle.hideturtle()
    turtle.penup()
    oldal = 150
    turtle.goto(-oldal / 2, -oldal / 3)
    turtle.pendown()
    for _ in range(3):
        turtle.forward(oldal)
        turtle.left(120)


#app
ablak = turtle.Screen()
turtle.hideturtle()
#turtle.bgcolor("lightgrey")
turtle.bgcolor("grey")
turtle.pensize(5)
turtle.pencolor("red")
turtle.listen()
turtle.onkey(haromszog, key="h")
turtle.onkey(turtle.bye, key= "q")

turtle.mainloop()

# Egy tetszőleges alakzat (nem háromszög és nem négyzet)
# rajzolása a turtle modul felhasználásával.

import turtle

def rajzol():
    turtle.clear()
    turtle.penup()
    sugar = 100
    turtle.goto( 0,  -sugar )
    turtle.pendown()
    turtle.circle(sugar)


#app
ablak = turtle.Screen()
turtle.hideturtle()
turtle.bgcolor("white")
turtle.title("kör rajzolás = k, kilépés = q")
turtle.pensize(5)
turtle.pencolor("blue")
turtle.listen()
turtle.onkey(rajzol, key="k")
turtle.onkey(turtle.bye, key= "q")

turtle.mainloop()

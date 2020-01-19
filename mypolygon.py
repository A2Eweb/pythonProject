import turtle
bob = turtle.Turtle()
print(bob)

def square(t):
    for i in range(4):
        bob.fd(100)
        bob.lt(90)
square(bob)
turtle.mainloop()
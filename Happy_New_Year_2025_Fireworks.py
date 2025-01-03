import turtle
import random
import time

def draw_firework(turtle_obj, x, y, size, colors):
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    for _ in range(36):
        turtle_obj.color(random.choice(colors))
        turtle_obj.forward(size)
        turtle_obj.backward(size)
        turtle_obj.right(10)

def display_message_stepwise(turtle_obj, screen, message, colors):
    turtle_obj.penup()
    turtle_obj.goto(0, 50)
    for i, char in enumerate(message, start=1):
        turtle_obj.color(random.choice(colors))
        turtle_obj.write(message[:i], align="center", font=("Comic Sans MS", 45, "bold"))
        screen.update()
        time.sleep(0.3)
        turtle_obj.clear()
    turtle_obj.color("white")
    turtle_obj.write(message, align="center", font=("Comic Sans MS", 40, "bold"))

def show_big_fireworks(turtle_obj, screen, colors):
    for _ in range(10):
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        size = random.randint(100, 200)
        draw_firework(turtle_obj, x, y, size, colors)
        screen.update()
        time.sleep(0.5)
        turtle_obj.clear()

def show_small_fireworks(turtle_obj, screen, colors):
    for _ in range(20):
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        size = random.randint(30, 80)
        draw_firework(turtle_obj, x, y, size, colors)
        screen.update()
        time.sleep(0.2)
        turtle_obj.clear()

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Happy New Year 2025 Fireworks")
    screen.tracer(0)
    
    colors = ["red", "yellow", "blue", "green", "orange", "purple", "pink"]
    firework_turtle = turtle.Turtle()
    firework_turtle.hideturtle()
    firework_turtle.speed(0)
    
    show_big_fireworks(firework_turtle, screen, colors)
    
    message_turtle = turtle.Turtle()
    message_turtle.hideturtle()
    display_message_stepwise(message_turtle, screen, "🎉 Happy New Year 2025! 🎉", colors)
    
    show_small_fireworks(firework_turtle, screen, colors)
    
    time.sleep(5)
    screen.bye()

if __name__ == "__main__":
    main()

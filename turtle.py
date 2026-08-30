import turtle

# Configure the window
screen = turtle.Screen()
screen.bgcolor("black")

# Create a fast-moving turtle
artist = turtle.Turtle()
artist.speed(0)  # 0 is the fastest animation speed
colors = ["red", "purple", "blue", "green", "orange", "yellow"]

# Generate a multi-colored geometric spiral
for x in range(120):
    artist.color(colors[x % 6])  # Cycle through colors
    artist.forward(x * 2)        # Move further out each iteration
    artist.left(59)              # Turn slightly less than 60 degrees

# Keep window open
turtle.done()
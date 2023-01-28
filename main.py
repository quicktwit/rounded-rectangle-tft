import math

class TFTDisplay:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[0 for x in range(width)] for y in range(height)]

    def pixel(self, x, y, color):
        self.pixels[y][x] = color

def draw_rounded_rectangle(x1, y1, x2, y2, r, color):
    # Draw top and bottom horizontal lines
    for x in range(x1+r, x2-r):
        display.pixel(x, y1, color)
        display.pixel(x, y2, color)
    # Draw left and right vertical lines
    for y in range(y1+r, y2-r):
        display.pixel(x1, y, color)
        display.pixel(x2, y, color)
    # Draw rounded corners
    for x in range(x1, x1+r):
        for y in range(y1, y1+r):
            if (math.sqrt((x-x1-r+0.5)**2 + (y-y1-r+0.5)**2) <= r-0.5):
                display.pixel(x, y, color)
    for x in range(x1, x1+r):
        for y in range(y2-r, y2):
            if (math.sqrt((x-x1-r+0.5)**2 + (y-y2+r-0.5)**2) <= r-0.5):
                display.pixel(x, y, color)
    for x in range(x2-r, x2):
        for y in range(y1, y1+r):
            if (math.sqrt((x-x2+r-0.5)**2 + (y-y1-r+0.5)**2) <= r-0.5):
                display.pixel(x, y, color)
    for x in range(x2-r, x2):
        for y in range(y2-r, y2):
            if (math.sqrt((x-x2+r-0.5)**2 + (y-y2+r-0.5)**2) <= r-0.5):
                display.pixel(x, y, color)


# Example usage:
display = TFTDisplay(128, 64)
draw_rounded_rectangle(10, 10, 100, 50, 5, 1)

#print the display
for row in display.pixels:
    for pixel in row:
        if pixel:
            print("#", end = " ")
        else:
            print(".", end = " ")
    print()

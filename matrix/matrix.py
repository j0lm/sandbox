#!/usr/bin/env python3

import random
import time
import sys
import os

def main():
    display = init_display()
    count = 0
    while(True):
        print_display(display)
        display = update_display(display)


def init_display():
    # get width and height
    try:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
    except IndexError:
        #sys.exit("ERROR: use correct format: ./matrix.py width height")
        width = 317
        height = 81
    if width <= 0 or height <= 0:
        sys.exit(f"ERROR: width and height must be greater than 0")
    print(f"Width: {width}\nHeight: {height}")
    return [[" " for i in range (width)] for j in range(height)]

    
def print_display(display):
    hz = 64
    period = 1 / hz
    os.system('clear')
    width = len(display[1])
    height = len(display)
    if width > 11:
        print(" " * int((width / 2) - 9), end="")
        print("T H E   M A T R I X")
    print("-" * width)
    for y in display:
        for x in y:
            print(x, end="")
        print()
    print("-" * width)
    time.sleep(period)

def update_display(display):
    gradient = ['@', '$', '#', '*', '!', '=', ';', ':', '~', '-', ',', '.']
    prob = 0.02
    width = len(display[1])
    height = len(display)
    new_display = []
    # update display
    new_display = list(display)
    new_display.pop()
    new_display.insert(0, [" "] * width)
    for char in range(width):
        if display[0][char] == gradient[len(gradient)-1] or display[0][char] == " ":
            new_display[0][char] = " "
        else:
            new_display[0][char] = gradient[gradient.index(display[0][char])+1]
    # get new gradients
    new_gradient = []
    for pixel in range(width):
        new_gradient.append(random.random() < prob)
    for i in range(width):
        if new_gradient[i]:
            new_display[0][i] = gradient[0]
    return new_display


if __name__ == "__main__":
    main()

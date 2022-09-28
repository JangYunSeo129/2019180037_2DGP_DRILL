from pico2d import *
import math
math.sin(270 /360 * 2 * math.pi)
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while (1):
    t = 0
    while (t < 7):
        clear_canvas_now()
        grass.draw_now(400,30)
        x = 400 + 200*math.sin((t -2.25) + 270/360 * 2 * math.pi)
        y = 290 + 200*math.cos((t- 2.25) + 270/360 * 2 * math.pi)
        character.draw_now(x,y)
        t = t + 0.01
        delay(0.01)
    while (x < 770):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        x = x+ 2
        delay(0.01)
    while (y < 540):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        y = y + 2
        delay(0.01)
    while (x > 30):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        x = x - 2
        delay(0.01)
    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        y = y - 2
        delay(0.01)
    while (x < 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.01)
close_canvas()

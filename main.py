def green():
    pins.analog_write_pin(AnalogPin.P0, 0)
    pins.analog_write_pin(AnalogPin.P1, 1023)
    pins.analog_write_pin(AnalogPin.P2, 0)

def on_button_pressed_a():
    global POCITADLO, RED, GREEN, BLUE
    if POINTER == 0:
        POCITADLO = RED
    if POINTER == 1:
        POCITADLO = GREEN
    if POINTER == 2:
        POCITADLO = BLUE
    POCITADLO += KROKMINUS
    if POCITADLO < 0:
        POCITADLO = 0
    if POINTER == 0:
        RED = POCITADLO
    if POINTER == 1:
        GREEN = POCITADLO
    if POINTER == 2:
        BLUE = POCITADLO
    prepis_displej()
input.on_button_pressed(Button.A, on_button_pressed_a)

def prepis_displej():
    Kitronik_VIEWTEXT32.display_single_line_string(Kitronik_VIEWTEXT32.DisplayLine.TOP,
        "R: " + str(RED) + " G: " + str(GREEN))
    Kitronik_VIEWTEXT32.display_single_line_string(Kitronik_VIEWTEXT32.DisplayLine.BOTTOM, "B: " + str(BLUE))

def on_button_pressed_b():
    global POCITADLO, RED, GREEN, BLUE
    if POINTER == 0:
        POCITADLO = RED
    if POINTER == 1:
        POCITADLO = GREEN
    if POINTER == 2:
        POCITADLO = BLUE
    POCITADLO += KROKPLUS
    if POCITADLO > 1023:
        POCITADLO = 1023
    if POINTER == 0:
        RED = POCITADLO
    if POINTER == 1:
        GREEN = POCITADLO
    if POINTER == 2:
        BLUE = POCITADLO
    prepis_displej()
input.on_button_pressed(Button.B, on_button_pressed_b)

def zhasni():
    pins.analog_write_pin(AnalogPin.P0, 0)
    pins.analog_write_pin(AnalogPin.P1, 0)
    pins.analog_write_pin(AnalogPin.P2, 0)
def blue():
    pins.analog_write_pin(AnalogPin.P0, 0)
    pins.analog_write_pin(AnalogPin.P1, 0)
    pins.analog_write_pin(AnalogPin.P2, 1023)
def red():
    pins.analog_write_pin(AnalogPin.P0, 1023)
    pins.analog_write_pin(AnalogPin.P1, 0)
    pins.analog_write_pin(AnalogPin.P2, 0)

def on_logo_pressed():
    global POINTER
    if POINTER < 2:
        POINTER += 1
    else:
        POINTER = 0
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def michacka():
    pins.analog_write_pin(AnalogPin.P0, RED)
    pins.analog_write_pin(AnalogPin.P1, GREEN)
    pins.analog_write_pin(AnalogPin.P2, BLUE)
KROKPLUS = 0
KROKMINUS = 0
POCITADLO = 0
POINTER = 0
RED = 0
GREEN = 0
BLUE = 0
basic.show_icon(IconNames.HAPPY)
basic.pause(200)
game.add_score(1)
BLUE = 0
GREEN = 0
RED = 0
POINTER = 0
POCITADLO = 0
KROKMINUS = -50
KROKPLUS = 50
Kitronik_VIEWTEXT32.display_single_line_string(Kitronik_VIEWTEXT32.DisplayLine.TOP, "RGB - Tonda")
basic.pause(2000)

def on_forever():
    if POINTER == 0:
        basic.show_string("R")
    if POINTER == 1:
        basic.show_string("G")
    if POINTER == 2:
        basic.show_string("B")
    michacka()
basic.forever(on_forever)

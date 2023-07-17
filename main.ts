function green () {
    pins.analogWritePin(AnalogPin.P0, 0)
    pins.analogWritePin(AnalogPin.P1, 1023)
    pins.analogWritePin(AnalogPin.P2, 0)
}
input.onButtonPressed(Button.A, function () {
    if (POINTER == 0) {
        POCITADLO = RED
    }
    if (POINTER == 1) {
        POCITADLO = GREEN
    }
    if (POINTER == 2) {
        POCITADLO = BLUE
    }
    POCITADLO += KROKMINUS
    if (POCITADLO < 0) {
        POCITADLO = 0
    }
    if (POINTER == 0) {
        RED = POCITADLO
    }
    if (POINTER == 1) {
        GREEN = POCITADLO
    }
    if (POINTER == 2) {
        BLUE = POCITADLO
    }
    prepis_displej()
})
function prepis_displej () {
    Kitronik_VIEWTEXT32.displaySingleLineString(Kitronik_VIEWTEXT32.DisplayLine.Top, "R: " + RED + " G: " + GREEN)
    Kitronik_VIEWTEXT32.displaySingleLineString(Kitronik_VIEWTEXT32.DisplayLine.Bottom, "B: " + BLUE)
}
input.onButtonPressed(Button.B, function () {
    if (POINTER == 0) {
        POCITADLO = RED
    }
    if (POINTER == 1) {
        POCITADLO = GREEN
    }
    if (POINTER == 2) {
        POCITADLO = BLUE
    }
    POCITADLO += KROKPLUS
    if (POCITADLO > 1023) {
        POCITADLO = 1023
    }
    if (POINTER == 0) {
        RED = POCITADLO
    }
    if (POINTER == 1) {
        GREEN = POCITADLO
    }
    if (POINTER == 2) {
        BLUE = POCITADLO
    }
    prepis_displej()
})
function zhasni () {
    pins.analogWritePin(AnalogPin.P0, 0)
    pins.analogWritePin(AnalogPin.P1, 0)
    pins.analogWritePin(AnalogPin.P2, 0)
}
function blue () {
    pins.analogWritePin(AnalogPin.P0, 0)
    pins.analogWritePin(AnalogPin.P1, 0)
    pins.analogWritePin(AnalogPin.P2, 1023)
}
function red () {
    pins.analogWritePin(AnalogPin.P0, 1023)
    pins.analogWritePin(AnalogPin.P1, 0)
    pins.analogWritePin(AnalogPin.P2, 0)
}
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (POINTER < 2) {
        POINTER += 1
    } else {
        POINTER = 0
    }
})
function michacka () {
    pins.analogWritePin(AnalogPin.P0, RED)
    pins.analogWritePin(AnalogPin.P1, GREEN)
    pins.analogWritePin(AnalogPin.P2, BLUE)
}
let KROKPLUS = 0
let KROKMINUS = 0
let POCITADLO = 0
let POINTER = 0
let RED = 0
let GREEN = 0
let BLUE = 0
basic.showIcon(IconNames.Happy)
basic.pause(200)
game.addScore(1)
BLUE = 0
GREEN = 0
RED = 0
POINTER = 0
POCITADLO = 0
KROKMINUS = -50
KROKPLUS = 50
Kitronik_VIEWTEXT32.displaySingleLineString(Kitronik_VIEWTEXT32.DisplayLine.Top, "RGB - Tonda")
basic.pause(2000)
basic.forever(function () {
    if (POINTER == 0) {
        basic.showString("R")
    }
    if (POINTER == 1) {
        basic.showString("G")
    }
    if (POINTER == 2) {
        basic.showString("B")
    }
    michacka()
})

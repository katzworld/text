from kb import KMKKeyboard
from kmk.keys import KC
from kmk.handlers.sequences import simple_key_sequence
from kmk.handlers.sequences import send_string
from kmk.modules.tapdance import TapDance

keyboard = KMKKeyboard()
tapdance = TapDance()
tapdance.tap_time = 750
keyboard.modules.append(tapdance)

import time
import board
import neopixel
import digitalio

led = digitalio.DigitalInOut(board.D9)
led.direction = digitalio.Direction.OUTPUT
led.value = True

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel.brightness = 1
pixel.fill((255,0, 255))
    
whoami = "321" #my Number 

authme = "jack" #lower case


LEFT_ARR = KC.TD(
    #1
    KC.LALT(KC.LEFT),
    #2
    KC.LEFT,
    )

RIGHT_ARR = KC.TD(
    #1
    KC.LALT(KC.RIGHT),
    #2
    KC.RIGHT,
    )

UP_ARR = KC.TD(
    #1
    KC.UP,
    #2
    KC.PGUP,
    #3
    KC.HOME,
    )

DOWN_ARR = KC.TD(
    #1
    KC.DOWN,
    #2
    KC.PGDN,
    #3
    KC.END,
    )
#auth is set
JACK = simple_key_sequence(
    (
    KC.APPLICATION,
    KC.A,
    KC.TAB,
    send_string(authme),
    KC.ENTER,
    KC.LCTL(KC.T)
    )
) 

RO_PRINT = simple_key_sequence(
    (
    KC.LALT(KC.LCTL(KC.F)),
    KC.HOME,
    KC.LSFT(KC.LCTL(KC.P)),  
    )
)


DEF_REC = simple_key_sequence(
    (
    KC.LALT(KC.R),
    KC.F9,
    KC.DOWN,
    KC.DOWN,
    KC.TAB,
    send_string(whoami),
    KC.TAB,
    KC.TAB,
    KC.TAB,
    KC.TAB,
    send_string("%C%"),
    KC.TAB,
    KC.TAB,
    KC.TAB,
    KC.LCTL(KC.D),
    KC.ENTER,
    )
   )
   
DEF_RECA = simple_key_sequence(
    (
    KC.LALT(KC.R),
    KC.F9,
    KC.DOWN,
    KC.DOWN,
    KC.TAB,
    send_string(whoami),
    KC.TAB,
    KC.TAB,
    KC.TAB,
    KC.TAB,
    send_string("%C%"),
    KC.ENTER,
    )
   )

DEF_RECALL = simple_key_sequence(
    (
    KC.LALT(KC.R),
    KC.F9,
    KC.DOWN,
    KC.DOWN,
    KC.TAB,
    KC.TAB,
    KC.TAB,
    KC.TAB,
    KC.TAB,
    send_string("%C%"),
    KC.ENTER,
    )
   )

DEF_REQ = simple_key_sequence(
    (
    KC.LALT(KC.R),
    KC.F9,
    KC.DOWN,
    KC.DOWN,
    KC.TAB,
    send_string(whoami), #WHO >?
    KC.TAB,
    KC.TAB,
    KC.TAB,
    KC.TAB,
    send_string("%Q%"),
    KC.ENTER,
    )
   )


DEF_TDD = KC.TD(
    DEF_REC, #my open tickets today
    DEF_REQ, #my quotes
    DEF_RECA, #all my ticket
    DEF_RECALL, #all open everyone
)

PICK_EM = simple_key_sequence( 
    (
    KC.LALT(KC.LCTL(KC.F)),
    KC.END,
    KC.UP,
    KC.UP,
    KC.UP,
    KC.UP,
    KC.LSFT(KC.LCTL(KC.P)),
    )
)

QUOTE = simple_key_sequence (
    (
    KC.LSFT(KC.LCTL(KC.P)), #call to print
    KC.MACRO_SLEEP_MS(1000), #zzzz
    KC.LSFT(KC.LCTL(KC.S)), #call to save
    )
)

RRO_TDD = KC.TD(
    PICK_EM, #pick em RO
    RO_PRINT, #full Ticket RO
    )


# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

keyboard.keymap = [
    [  #Nav Keys
        QUOTE,  DEF_TDD,    RRO_TDD,
        KC.LCTL(KC.P),  JACK,     KC.LCTL(KC.T),
        XXXXXXX,    UP_ARR,      XXXXXXX,
        LEFT_ARR,    DOWN_ARR,    RIGHT_ARR
    ]
]

if __name__ == '__main__':
    keyboard.go()

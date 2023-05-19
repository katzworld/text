from kb import KMKKeyboard 
from kmk.keys import KC
from kmk.handlers.sequences import simple_key_sequence
from kmk.handlers.sequences import send_string
from kmk.modules.tapdance import TapDance

keyboard = KMKKeyboard()
tapdance = TapDance()
tapdance.tap_time = 500
keyboard.modules.append(tapdance)

whoami = "321" #my Number 

authme = "JACK" #lower case

##keycode KEY
#keyboard.keymap = [
#    [  #Nav Keys
#        BB_TDD, => tapdance 1 copy name over ticket "setup", 2 copy name field to PO "quote", 3 save quote to desktop     
#        DEF_TDD, => tapdance  DEFAULT FILTER SETUP 1 - MY OPEN TICKETS TODAY C, OPEN QUOTES TODAY ,3- ALL MY OPEN TICKET , 4 -ALL OPEN TICKETS  
#        RRO_TDD, => tapdance  1 pick em ro ticket, 2 full pick ticket RO
#        KC.LCTL(KC.P), =>  print ticket 
#        JACK, => run auth script 
#        BILL_IT, =>post ticket , post 0 ticket with YES option 
#        XXXXXXX,    
#        UP_ARR, TAP DANCE=> 1 UP, 2 PAGEUP, 3 HOME "top"
#        LEFT_ARR, => tap dance 1 press drill out of ticket , 2 press left arrow only 
#        DOWN_ARR, => tap dance 1 down , 2 pagedown , 3 END "bottom"
#        RIGHT_ARR, => tap dance as above but drill into ticket , 1 right press
#    ]

POST = simple_key_sequence ( 
    (
    KC.LCTL(KC.T),
    )
)


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

JACK = simple_key_sequence( #auth
    (
    KC.APPLICATION,
    KC.A,
    KC.TAB,
    send_string(authme),
    KC.ENTER,
    POST,
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
    KC.LALT(KC.O),
    send_string("%C%"),
    KC.LALT(KC.F),
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
    KC.LALT(KC.O),
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
    KC.LALT(KC.O),
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
    KC.LALT(KC.O),
    send_string("%Q%"),
    KC.ENTER,
    )
   )


DEF_TDD = KC.TD(
    DEF_RECALL, #all open everyone
    DEF_REC, #my open tickets today
    DEF_REQ, #my quotes 
    DEF_RECA, #all my ticket
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

TICK_SET = simple_key_sequence (
    (
        KC.ENTER,
        KC.TAB,
        KC.LSFT(KC.DEL),
        KC.LSFT(KC.INS),
        KC.LALT(KC.N),
        KC.LSFT(KC.INS),
        KC.ENTER,
    )
)

QUOT_SET = simple_key_sequence (
    (
        KC.ENTER,
        KC.TAB,
        KC.LSFT(KC.DEL),
        KC.LSFT(KC.INS),
        KC.LALT(KC.P),
        KC.LSFT(KC.INS),
        KC.LALT(KC.N),
        KC.LSFT(KC.INS),
        KC.ENTER,
    )
)

QUOTE = simple_key_sequence (
    (
    KC.LSFT(KC.LCTL(KC.P)), #call to print
    KC.MACRO_SLEEP_MS(1000), #zzzz
    KC.LSFT(KC.LCTL(KC.S)), #call to save
    KC.MACRO_SLEEP_MS(1000), #zzzz 
    KC.ENTER, 
    KC.MACRO_SLEEP_MS(500), #zzzz
    KC.LALT(KC.F4),
    )
)


BB_TDD = KC.TD(
    TICK_SET,
    QUOT_SET,
    QUOTE, 
)



POST_PLUS = simple_key_sequence ( 
    (
    POST,
    KC.MACRO_SLEEP_MS(250), #zzzz
    KC.Y,
    )
)

BILL_IT = KC.TD(
    POST,
    POST_PLUS,
    )

PRINT_TICKET = simple_key_sequence (
    (   
    KC.LCTL(KC.P),
    )
)

PRINT_IT = KC.TD(
    PRINT_TICKET,
    QUOTE,
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
        BB_TDD,  DEF_TDD,    RRO_TDD,
        PRINT_IT,  JACK,     BILL_IT,
        XXXXXXX,    UP_ARR,      XXXXXXX,
        LEFT_ARR,    DOWN_ARR,    RIGHT_ARR
    ]
]

if __name__ == '__main__':
    keyboard.go()

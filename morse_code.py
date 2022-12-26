from machine import Pin
import time

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'
}

DELAYS = {"-":0.75, ".":0.25}

word = input("Enter word: ").upper()

led = Pin(15, Pin.OUT)

for letter in word:
    if letter not in MORSE_CODE_DICT:
        continue
    
    print(letter, MORSE_CODE_DICT[letter])
    morse_pattern = MORSE_CODE_DICT[letter]
    for symbol in morse_pattern:
        delay = DELAYS[symbol]
        #led control
        led.value(0)
        time.sleep(delay)
        led.value(1)
        time.sleep(delay)
    #next character
    led.value(0)
    time.sleep(1.5)        
        

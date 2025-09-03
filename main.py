'''
Builds an emote pyramid in Twitch chat.
Run this script and switch to the Twitch chat window within 5 seconds.
It will type out a pyramid of the specified emote.

Make sure to have the `pynput` library installed:
pip install pynput
'''

from time import sleep
from pynput.keyboard import Key, Controller

def emote_pyramid(emote, height, speed):
    keyboard = Controller()

    # Top half of the pyramid
    for i in range(height):
        keyboard.type(f"{emote} "* (i + 1))
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        sleep(speed) # Pause between lines

    # Bottom half of the pyramid
    for i in range(height - 1):
        keyboard.type(f"{emote} " * (height - i - 1))
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        sleep(speed) # Pause between lines


if __name__ == '__main__':

    wait = 5  # Time to switch to the chat window (seconds)

    # Set the parameters for the emote pyramid
    emote = 'Kappa'
    pyramid_height = 10
    speed = 1

    print(f"The {pyramid_height}-height pyramid will take {pyramid_height * 2 - 1} seconds to build.")
    print(f"You have {wait} seconds to place your cursor in the chat box.")
    sleep(wait)
    print("Starting pyramid...")
    emote_pyramid(emote, pyramid_height, speed)
    print("Pyramid completed!")

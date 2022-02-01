import pyautogui as pt
from time import sleep
import pyperclip as pc
from pynput.mouse import Controller, Button
from whatsapp_responses import response

mouse = Controller()

class whatsApp:

    #defines the stating values
    def __init__(self, speed=.5, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''

    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen('mm.png',confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-100, 0, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_green_dot): ', e)

    # Navigate to our message input box
    def nav_input_box(self):
        try:
            position = pt.locateOnScreen('aaa.png',confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(100, 10, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_green_box): ', e)

    # Navigate to the message we want to respond to
    def nav_message(self):
        try:
            position = pt.locateOnScreen('aaa.png',confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(100, -50, duration=self.speed)
        except Exception as e:
            print('Exception (nav_message): ', e)

    #copies the message that we want to pocess
    def get_message(self):
        mouse.click(Button.left, 3)
        sleep(self.speed)
        mouse.click(Button.right, 1)
        sleep(self.speed)
        pt.moveRel(10, 10, duration=self.speed)
        mouse.click(Button.left, 1)
        sleep(1)

        self.message = pc.paste()
        print('User says: ', self.message)

    # Sends the message to the user
    def send_message(self):
        try:
            # Checks whether the last message was the same
            if self.message != self.last_message:
                bot_response = response(self.message)
                print('You say:', bot_response)
                pt.typewrite(bot_response, interval=.1)
                pt.typewrite('\n')

                # Assign them the same message
                self.last_message = self.message
            else:
                print('No new messages..')

        except Exception as e:
            print('Exception (send_message):', e)

    # Close response box
    def nav_x(self):
        try:
            position = pt.locateOnScreen('x.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(10, 10, duration=self.speed)
            mouse.click(Button.left, 1)
        except Exception as e:
            print('Exception (nav_x): ', e)
wa_bot = whatsApp(speed=.5,click_speed=.4)
sleep(4)

while True:
    wa_bot.nav_green_dot()
    wa_bot.nav_x()
    wa_bot.nav_message()
    wa_bot.get_message()
    wa_bot.nav_input_box()
    wa_bot.send_message()

    sleep(7)

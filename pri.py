from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from plyer import battery
from threading import Thread
from plyer import sms
import threading
import time
import os

class boxapp(App):
    global email
    global x
    def build(self):
        def chek_t(instance):
            print(threading.active_count())

        def on_text(instance, value):
            global email
            email = value
            print(email)

        def pros():
            while True:
                global x
                global email
                if x == 0:
                    break
                old = battery.status['isCharging']
                time.sleep(0.1)
                new = battery.status['isCharging']
                if new != old:
                    recipient = email
                    message = 'the phone Charging: ' + str(new)
                    sms.send(recipient=recipient, message=message)
                    print('sendet to: ' + str(email) + ' inf:' + str(message))

        def callback(instance):
            global x
            global email
            global pross
            x = x + 1
            if x == 2:
                x = 0
            if x == 1:
                Thread(target=pros).start()
                instance.text = 'on'
            if x == 0:
                instance.text = 'off'
            print(email)
            print(x)

        global x
        global email
        global pross
        email = 'fack'
        x = 0
        bl = BoxLayout(orientation='vertical')
        blin = BoxLayout(orientation='vertical')
        start = Button(text='off')
        # chek = Button(text='чек')
        # blin.add_widget(chek)
        # chek.bind(on_press=chek_t)
        start.bind(on_press=callback)
        inputemail = TextInput(text='namber')
        inputemail.bind(text=on_text)
        blin.add_widget(inputemail)
        bl.add_widget(blin)
        bl.add_widget(start)
        return bl

if __name__ == '__main__':
    os.environ["KIVY_NO_CONSOLELOG"] = "True"
    __version__ = '0.0.1'
    boxapp().run()

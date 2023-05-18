# Adding some designs in the program
from pyfiglet import Figlet
from termcolor import colored

# Importing class TV from ClassTV.py
from ClassTV import TV

f = Figlet(font='serifcap', width = 140)
print(colored(f.renderText("Program output: "), 'light_green'))

def test_tv():
    # Creating the first TV object
    tv1 = TV()
    tv1.turn_on()
    tv1.get_channel()
    tv1.set_channel(30)
    tv1.get_volume()
    tv1.set_volume(3)
    tv1.channel_up()
    tv1.channel_down()
    tv1.volume_up()
    tv1.volume_down()

    # Creating the second TV object
    tv2 = TV()
    tv2.turn_on()
    tv2.get_channel()
    tv2.set_channel(3)
    tv2.get_volume()
    tv2.set_volume(2)
    tv2.channel_up()
    tv2.channel_down()
    tv2.volume_up()
    tv2.volume_down()

    # Display TV information
    print("\033[92m>>>>>>", "\033[m",f"TV1's channel is {tv1.get_channel()} and volume level is {tv1.get_volume()}")
    print("\033[92m>>>>>>", "\033[m",f"TV2's channel is {tv2.get_channel()} and volume level is {tv2.get_volume()}")
    print('\033[92m=' * 66 , "END", '\033[92m=' * 66 )

# Run the test_tv function
test_tv()

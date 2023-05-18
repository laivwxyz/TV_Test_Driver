# Importing class TV from ClassTV.py
from ClassTV import TV

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

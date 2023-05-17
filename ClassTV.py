# Creating the class named TV
class TV:
    def __init__(self, channel=1, volume_level=1):
        # creating the class instances
        self.channel = channel
        self.volume_level = volume_level
        self.tv_on = True 

    def turn_on(self):
        # Turns on the Tv
        self.tv_on = True

    def turn_off(self):
        # Turns off the TV
        self.turn_on = False
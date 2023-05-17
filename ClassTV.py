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

    def get_channel(self):
        # Returns the current channel of the TV
        return self.channel
    
    def set_channel(self, channel : int):
        # Sets a new channel for the TV
        if channel < 1 or channel > 120: 
            raise ValueError("Invalid channel number")
        self.channel = channel
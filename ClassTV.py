# Adding some designs in the program
from pyfiglet import Figlet
from termcolor import colored

f = Figlet(font='isometric2', width = 140)
print(colored(f.renderText("Television"), 'light_green'))
print(colored(("=" * 137), color='light_green'))
print("\033[92mProgram by: \033[0mLailanie E. Dela Cruz BSCPE 1-4")
print ("\033[92mExercise: \033[0mAssignment #6")
print(colored(("=" * 137), color= 'light_green'))

# Creating the class named TV
class TV:
    def __init__(self, channel = 1, volume_level = 1, tv_on = True):
        # creating the class instances
        self.channel = channel
        self.volume_level = volume_level
        self.tv_on = tv_on

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
            raise ValueError("\033[91mInvalid channel number")
        self.channel = channel

    def get_volume(self):
        # Returns the current volume level of the TV 
        return self.volume_level
    
    def set_volume(self, volume_level : int):
        # Sets new volume level for the TV
        if volume_level < 1 or volume_level > 7:
            raise ValueError("\033[91mInvalid volume level")
        self.volume_level = volume_level

    def channel_up(self):
        # Increases the channel number by 1
        if self.channel < 120:
            self.channel += 1

    def channel_down(self):
        # Decreases the channel number by 1
        if self.channel > 1:
            self.channel -= 1
    
    def volume_up(self):
        # Increases the volume level by 1
        if self.volume_level < 7:
            self.volume_level += 1

    def volume_down(self):
        # Decreases the volume level by 1
        if self.volume_level > 1:
            self.volume_level -= 1

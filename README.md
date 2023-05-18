![Screenshot (394)](https://github.com/laivwxyz/TV_Test_Driver/assets/129714181/acd85eef-6e32-445c-afac-7a39c242340c)
#### This Python program implements a TV class based on the provided UML class diagram. It also includes a test driver program, `TestTV.py`, that creates two TV objects and produces the specified output.

## UML Class Diagram

TV
- channel: int
- volumeLevel: int
- on: bool
_______
- TV()
- turnOn(): None
- turnOff(): None
- getChannel(): int
- setChannel(channel: int): None
- getVolume(): int
- setVolume(volumeLevel: int): None
- channelUp(): None
- channelDown(): None
- volumeUp(): None
- volumeDown(): None

## Class Description
### Attributes
`channel:` An integer representing the current channel of the TV (ranging from 1 to 120).

`volumeLevel:` An integer representing the current volume level of the TV (ranging from 1 to 7).

`on:` A boolean indicating whether the TV is on or off.

### Methods
`TV():` Constructs a default TV object.

`turnOn():` Turns on the TV.

`turnOff():` Turns off the TV.

`getChannel() -> int:` Returns the current channel of the TV.

`setChannel(channel: int) -> None:` Sets a new channel for the TV.

`getVolume() -> int:` Returns the current volume level of the TV.

`setVolume(volumeLevel: int) -> None:` Sets a new volume level for the TV.

`channelUp() -> None:` Increases the channel number by 1.

`channelDown() -> None:` Decreases the channel number by 1.

`volumeUp() -> None:` Increases the volume level by 1.

`volumeDown() -> None:` Decreases the volume level by 1.

## Test Driver Program
The test driver program, `TestTV,py`, creates two TV objects, `tv1` and `tv2`, and verifies their functionality by printing their channel and volume level.

### Sample Output
![Screenshot (395)](https://github.com/laivwxyz/TV_Test_Driver/assets/129714181/96463f7f-1db8-41e3-9acc-6fcc6e35402a)

## Running the Program
1. Clone the repository or download the files `ClassTV.py` and `TestTV.py`.

2. Make sure you have Python installed on your system.

3. Open your terminal or command prompt and navigate to the directory where the files are located.

4. Run the test driver program by executing the command: python TestTV.py.

5. The output will be displayed in the terminal.

## Contibute

Contributions are always welcome! Please read the [contribution guidelines](https://github.com/matiassingers/awesome-readme/blob/master/contributing.md) first.

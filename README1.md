GAME 2048
# DESCRIPTION
Game made in python sublime text 3 , run in windows command prompt

## HOW THE GAME WORKS

The game consists of a N-by-N board starting all zeros .As the player uses the WASD keys to move, 2 is randomly spawned in any empty index of the board. When two same values are adjacent to each other and a key is pressed in that direction the numbers add up to give a single number. The player has to use the WASD keys that shift all the existing numbers in the resp direction to finally bring the winning value. The player must try to use as less filled index positions as possibles

## MOVEMENTS
W: shifts all values **upwards** and merges similar adjacent values in that     direction

A: shifts all values **leftwards** and merges similar adjacent values in that  direction

S: shifts all values **downwards** and merges similar adjacent values in that   direction

D: shifts all values **rightwards** and merges similar adjacent values in that   direction

## RULES FOR GAME END
1. If the player is able to make the winning value ...he wins.
2. If the player is left with no blank places(indexes with zeros) and has no merges left in any direction , before gaining winning value ...he loses. 

## PLAYER CHOICES
The player has two choices before the start of game.
Tese must be defined in the command line before game starts:

1. He can choose the size of the game ..for example if size= 3 then a board of 3-by-3 is made.
2. He can choose the winning value.

### Rules for choosing game size
The game size entered must be a positive integer. If a negative integer value or 0 is chosen or no game size is defined then game size is set to default of 5-by-5.

### Rules for choosing  winning value
The player is expect to enter a power of 2 as winning value

1. If no value is entered a default value of 2048 is chosen.
2. If the value is less than or equal to 0 default value is taken.
3. If the value is a positive integer and not a power of 2 then the first power of 2 greater than the integer is chosen.
4. Else enter value is chosen 

### How to define choices in command line.
for game size, in command line enter --w (int)
for winning value, in command line enter --n (int) 

## TO PLAY
TO play use W/A/S/D + Enter
Any other input is invalid .

# GAMEBOARD IMAGE
![demo_image](https://user-images.githubusercontent.com/64795135/82245898-6bf02880-9961-11ea-83af-d4b1105c8acd.jpg)

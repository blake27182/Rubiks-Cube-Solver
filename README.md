# Rubiks-Cube-Solver
This project is still in progress

This is a program that solves a virtual rubik's cube, then pushes the instructions to stepper motors to solve the real thing.

To use the Software in its current stage, simply run main.py as a script.

This is a work in progress. The finished project should function roughly as follows: A user scrambles a rubik's cube by hand, then inserts it into a machine where it is suspended by rotating rods controlled by stepper motors. Two cameras take pictures of the cube and determine what color each square tile is. This information is then used to create a virtual representation of the cube as an object of type Cube as declared in the file Cube. The object is then passed to several master functions in the main file that perform solving algorithms on the object. Each move is recorded in the Cube data member history until the virtual cube is solved. Once this step is complete, the move history is passed through a compression phase, where some combinations of moves may be compressed to fewer ones to make the solve more efficient. The move history is then accessed by a script that reads each move one at a time and manifests that move in the machine by turning one of the rods.

Future versions of this software might include the ability to turn two motors at once, or more efficient solving algorithms.

The hardware I've chosen to use are:
a raspberry pi 3.
2 Pi Cameras.
6 DRV-8825 stepper motor drivers.
6 NEMA 17 stepper motors.
a variable bench power supply.
a prototyping breadboard.
walnut wood.

Currently, this software is fully functional besides interfacing with hardware such as cameras and motors. It can scramble a virtual cube and solve it, compress the moves, and read them out to the console. Based on about 2000 tests of varying moves to scramble, the average number of moves to solve is 178.

# Rubiks-Cube-Solver
This project is still in progress

I used a Raspberry Pi to control my robot, but if you choose to use something else, be sure to change the 
Piper.py to accomidate your operating system and hardware

Configuring the GPIO pins:
Make sure that the pins connected to each stepper chip are entered into the Piper.py file correctly
Be sure to enter the convention you are using to refer to the pins in the G.setmode()

Configuring the Power Supply:
Make sure the voltage is at 12V and the maximum current limit is set to 1.5A

Configuring the DRV8825:
Turn the power supply on
Run the sleep disabler to turn all the chips on
Reading the voltage between ground and the pot, adjust the pot between 0.7-0.9 volts

Configuring the Stepper Motors:
Plug the pins into the breadboard so that the black wire is in pin B2 (nearest the ground next to vmot)
This is not super critical, since reversing the plug simply reverses the direction of the motor

###########

Since there is no camera connected yet, to solve the cube, you must enter the faces into the main.py manually
After that, you can run the main and it will solve the cube.

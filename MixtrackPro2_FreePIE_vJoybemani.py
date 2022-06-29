# This is a work in progress and to hell with your warranty!
# I wanted to use a Korg nanoKontrol2 as a joystick. Why? 'Cause buttons, dials & sliders for cheaper ($80 CDN).
# This: http://www.korg.com/caen/products/computergear/nanokontrol2/
# To make this work we need to monitor the midi from the nanoKontrol2 and convert them in real time to a joystick output.
# We can do that with FreePIE (Programmable Input Emulator): http://andersmalmgren.github.io/FreePIE/
# FreePIE converts that to an output for a virtual joystick.
# For this we're using vJoy: http://vjoystick.sourceforge.net/site/
# vJoy only supports a limited number of axis which we want to use as sliders/dials and other inputs to games.
# To make this all work, we're going to have to split layout of the nanoKontrol2 into multiple virtual joysticks.
# 4 dials and 4 sliders on the left as a joystick (with some buttons?), 4 dials and 4 sliders on the right as a second joystick (with some buttons?).
# A 3rd joystick could be used for all the "transport" buttons (forward, back, play, record, next track, etc).
# All of this was coded in a brute force way because I am a noob at this.

# Install vJoy.
# Install FreePIE.
# Install Korg Kontrol Editor. https://www.korg.com/us/support/download/software/0/159/1354/
# Starting with Korg Kontrol Editor. Run it and see if you can connect to the nanoKontrol2. This should bring up a "map" of the nanoKontrol2 and the Control Channels (CC#)'s.
# Open vJoyConf. Create 2 joysticks. 1 has all the axis enables with 36 buttons. 2 has all the exis enabled with any number of buttons since they won't be used.
# Open vJoy Monitor.
# Copy/paste or open this code in/into FreePIE. Save it as a script, then press run. If it all works, you should be able to monitor the joystick outuput with vJoy's monitor program.

def update():
   diagnostics.watch(midi[0].data.channel)
   diagnostics.watch(midi[0].data.status)
   diagnostics.watch(midi[0].data.buffer[0])
   diagnostics.watch(midi[0].data.buffer[1])


# Sliders and Dials and buttons on the left side of the nanoKontrol2
# Change the value after == to the Control Channel (CC#) you want as input from the nanoKontrol2
# Change the value after vJoy[0]. you want to be the button on your virtual joystick.
# Change the value after vJoy[ for the virtual joystick you want to use [0] or [1] for example.

#R_LoopOrange1 CC#86 Cross
if (midi[0].data.buffer[0] == 86) and (midi[0].data.buffer[1] > 0): 
	vJoy[1].setButton(1,True)  
if (midi[0].data.buffer[0] == 86) and (midi[0].data.buffer[1] < 127):
	vJoy[1].setButton(1,False)
#R_ CC#93 Square
if (midi[0].data.buffer[0] == 93) and (midi[0].data.buffer[1] > 0): 
	vJoy[1].setButton(0,True)  
if (midi[0].data.buffer[0] == 93) and (midi[0].data.buffer[1] < 127):
	vJoy[1].setButton(0,False)
#R_ CC#88 R1
if (midi[0].data.buffer[0] == 88) and (midi[0].data.buffer[1] > 0): 
	vJoy[1].setButton(5,True)  
if (midi[0].data.buffer[0] == 88) and (midi[0].data.buffer[1] < 127):
	vJoy[1].setButton(5,False)
#R_LoopOrange3 CC#95 Circle
if (midi[0].data.buffer[0] == 95) and (midi[0].data.buffer[1] > 0): 
	vJoy[1].setButton(3,True)  
if (midi[0].data.buffer[0] == 95) and (midi[0].data.buffer[1] < 127):
	vJoy[1].setButton(3,False)
if starting:
	midi[0].update += update
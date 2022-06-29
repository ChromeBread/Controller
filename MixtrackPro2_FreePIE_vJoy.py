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

#R_LoopOrange1 CC#86 Triangle
if (midi[0].data.buffer[0] == 86) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(3,True)  
if (midi[0].data.buffer[0] == 86) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(3,False)
#R_LoopOrange2 CC#87 Square
if (midi[0].data.buffer[0] == 87) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(0,True)  
if (midi[0].data.buffer[0] == 87) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(0,False)
#R_LoopOrange3 CC#88 Cross
if (midi[0].data.buffer[0] == 88) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(1,True)  
if (midi[0].data.buffer[0] == 88) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(1,False)
#R_LoopOrange4 CC#100 Circle
if (midi[0].data.buffer[0] == 100) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(2,True)  
if (midi[0].data.buffer[0] == 100) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(2,False)
#dial_L_MID
if midi[0].data.buffer[0] == 18:#CC18
	dial_r2 = midi[0].data.buffer[0] == 18 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[0].rz = dial_r2;
#dial_R_TREBLE
if midi[0].data.buffer[0] == 17:#CC17
	dial_r1 = midi[0].data.buffer[0] == 17 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[0].x = dial_r1;
#dial_R_BASS
if midi[0].data.buffer[0] == 21:#CC21
	dial_r3 = midi[0].data.buffer[0] == 21 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[0].slider = dial_r3;
#dial_CUE_GAIN
if midi[0].data.buffer[0] == 11:#CC11
	dial_cg = midi[0].data.buffer[0] == 11 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[0].ry  = dial_cg;
#dial_R_MID
if midi[0].data.buffer[0] == 19:#CC19
	dial_r2 = midi[0].data.buffer[0] == 19 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[0].y = dial_r2;
#slider_L_TREBLE
if midi[0].data.buffer[0] == 16:#CC16	
	slide_l1 = midi[0].data.buffer[0] == 16 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[0].z = slide_l1;
#slider_L_BASS
if midi[0].data.buffer[0] == 20:#CC20	
	slide_l3 = midi[0].data.buffer[0] == 20 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[0].rx = slide_l3;
#slider_CUE_MIX
if midi[0].data.buffer[0] == 12:#CC12	
	slide_cm = midi[0].data.buffer[0] == 12 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[0].dial = slide_cm;
if starting:
	midi[0].update += update
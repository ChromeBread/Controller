def update():
	yaw = filters.mapRange(trackIR.yaw, -180, 180, -vJoy[0].axisMax, vJoy[0].axisMax)
	pitch = filters.mapRange(trackIR.pitch, -180, 180, -vJoy[0].axisMax, vJoy[0].axisMax)
	vJoy[0].z = yaw
	vJoy[0].rz = pitch

if starting:
	trackIR.update += update
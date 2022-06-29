#Use Z to toggle on/off and right mouse to activate head tracking
#(Good for games like Battlefield 3)
def update():
    yaw = trackIR.yaw
    pitch = trackIR.pitch

    deltaYaw = filters.delta(yaw)
    deltaPitch = filters.delta(pitch)

    if (enabled and hotkey):
        mouse.deltaX = deltaYaw*multiply
        mouse.deltaY = -deltaPitch*multiply

if starting:
    enabled = False
    multiply = 20
    trackIR.update += update

hotkey = mouse.rightButton
toggle = keyboard.getPressed(Key.Z)

if toggle:
    enabled = not enabled
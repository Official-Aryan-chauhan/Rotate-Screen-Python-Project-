import rotatescreen
import keyboard
import time
# A prank project using python
display_info = rotatescreen.get_primary_display() # for primary display only

def rotate_screen(df):
    df.rotate_to(90)
    df.rotate_to(180)
    df.rotate_to(270)
    df.rotate_to(0)

while True:
    if keyboard.is_pressed('e'):
        print("Made By Aryan Chauhan !","\n","Exitting")
        time.sleep(5)
        break
    else:
        rotate_screen(display_info)
        time.sleep(0.25) # TO prevent from Instant "CPU Spike"
    
import pyb,time
#Switching the inbuilt LEDs based on the value of Internal Accelerometer (based on y-axis only)
acc = pyb.Accel()
while (1):
    acc_y = acc.y()
    print(acc_y)
    if(acc_y<0):
        pyb.LED(2).on()
        pyb.LED(3).off()
        pyb.LED(4).off()
    elif ((acc_y>=0)&(acc_y<12)):
        pyb.LED(2).off()
        pyb.LED(3).on()
        pyb.LED(4).off()
    elif (acc_y>=12):
    	pyb.LED(2).off()
        pyb.LED(3).off()
        pyb.LED(4).on()
    time.sleep(0.5)

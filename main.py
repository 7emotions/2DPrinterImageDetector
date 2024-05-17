
import sensor
import time
import image
import struct
import pyb

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)
sensor.set_gainceiling(8)
clock = time.clock()
i = 0
uart = pyb.UART(1, 115200)

def send(data):
    if len(data) != 0:
        # 0xaf -> start flag
        # i    -> image index
        # len  -> size of data
        # data -> data body
        # 0xfa -> end flag
        pack = [0xaf,i,len(data)] + data + [0xfa]
        uart.wrtie(struct.pack(pack))

threshold = 4 # cluster threshold

while True:
    clock.tick()
    img = sensor.snapshot()
    img.lens_corr()
    img.rotation_corr()
    img.binary([(20, 80)])

    for x in range(img.width()):
        ps=[]
        for y in range(img.height()):
            if img.get_pixel(x,y) == 255:
                if len(ps) == 0 or ps[-1][1] - y <= threshold:
                        ps.append((x,y))
        send(ps)

    print(clock.fps())

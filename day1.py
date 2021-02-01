from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
import random

x,y,z = mc.player.getTilePos()

while True:
    r = random.randrange(0,16)
    mc.setBlocks(x+5,y,z+5,x-5,y,z-5,35,r)
    time.sleep(0.5)
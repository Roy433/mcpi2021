from mcpi.minecraft import Minecraft
mc=Minecraft.create()


x,y,z = mc.player.getTilePos()
mc.setBlocks(x,y,z,x+49,y+49,z+49,57)
mc.setBlocks(x+1,y+1,z+1,x+48,y+48,z+48,0)

import time

while True:
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,38)
    time.sleep(0.5)
    
    
    
    
    
while True:
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,8)
    mc.setBlock(x,y-1,z,19)
    time.sleep(10)
    
    
    
    
    
while True:
    x,y,z = mc.player.getTilePos()  
    a=mc.setBlock(x+1,y-1,z)
    b=mc.setBlock(x-1,y-1,z)
    c=mc.setBlock(x,y-1,z+1)
    c=mc.setBlock(x,y-1,z-1)
    
#    if a==8ora==9orb==8orb==9orc==8orc==9ord==8ord==9or
    
    
     x,y,z = mc.player.getTilePos()
     
a=0
while a<5:
    mc.setBlock(x+10,y-1,z,x-5,y-5,z,46)
    z=z+5
    a=a+1
    
    
    
x,y,z = mc.player.getTilePos()
a=int(input("想放甚麼方塊?"))
mc.setBlock(x,y,z,a)
    
    
    




name=input("enter your name:")
message=input("enter your message:")
mc.postToChat('<'+ name +'> '+message)






    
x,y,z = mc.player.getTilePos()  
mc.setSign(x,y,z,68,"hi")    
    


while True:
    x,y,z = mc.player.getTilePos()
    
    a=mc.getBlockWithData(x,y-1,z)
    if a.data == 15:
        mc.postToChat('死路')
        
    if a.data == 11:
        mc.postToChat('右轉
                      
                      
                      
                      
                      
                      
while True:      
    hits = mc.events.pollBlockHits()

    if len(hits) > 0:
        
        hit = hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        block=mc.getBlock(x,y,z)
        
        if block == 1:
            mc.setBlock(x,y,z,41)
                      
                      
                      
                      
x,y,z = mc.player.getTilePos()                      
mc.spawnEntity(x,y,z,92)                      
                      
                      
                      
                      ')







    
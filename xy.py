import mcpi.minecraft as minecraft
ms = minecraft.Minecraft.create()
import time
while True:
    time.sleep(1)
    pos  = ms.player.getTilePos()
    if pos.x==-216 and pos.z==435:
        ms.postToChat("Welcom Home")

import mcpi.minecraft as minecraft
ms = minecraft.Minecraft.create()
pos  = ms.player.getTilePos()
print (pos.x)
print (pos.y)
print (pos.z)

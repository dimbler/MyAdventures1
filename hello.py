import mcpi.minecraft as minecraft
ms = minecraft.Minecraft.create()
ms.postToChat("Hello Minecraft World")
pos  = ms.player.getTilePos()
print (pos)

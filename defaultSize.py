import maya.cmds as mc;

def create_shapes(size=4):
    cube1 = mc.polyCube(w=size, h=size, d=size, name="box")
    sphere1 = mc.polySphere(r=size/2,name="ball")
    cylinder1 = mc.polyCylinder(r=size, h=size, name="can")
shapes()
    
     
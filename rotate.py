import maya.cmds;
pSphere = maya.cmds.polySphere()[0];
pCube = maya.cmds.polyCube()[0];

maya.cmds.connectAttr(pCube1+' .ry' ,pSphere1+' .ty');
maya.cmds.select(pCube1);
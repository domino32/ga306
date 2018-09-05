import maya.cmds;
pSphere = maya.cmds.polySphere()[0];

pCube = maya.cmds.polyCube()[0];

maya.cmds.connectAttr(pCube1+' .rz' ,pSphere1+' .t-z' ,pSpere2+' .tz');

maya.cmds.select(pCube1);
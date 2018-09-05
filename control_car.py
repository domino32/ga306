import maya.cmds as mc;
pCube1 = maya.cmds.polyCube()[0];

mc.connectAttr(pCube1+' .tz', 'test_car'+' .tz');
mc.connectAttr(pCube1+' .rz', 'test_car'+' .rz');

mc.connectAttr(pCube1+' .tx', 'test_car'+' .tx');
mc.connectAttr(pCube1+' .rx', 'test_car'+' .rx');
mc.select(pCube1);


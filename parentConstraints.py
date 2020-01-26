import maya.cmds as cmds

for x in rane (1,126):
	xStr = str(x)
	cmds.parentConstraint('geo_jnt' + xStr, 'CH:CH_' + xStr, w = 1, mo = True)
	cmds.parentConstraint('ik_jnt' + xStr, 'geo_jnt' + xStr, w = 1, mo = True)
	cmds.parentConstraint('dyn_jnt' + xStr, 'geo_jnt' + xStr, w = 0, mo = True)
	
cmds.parentConstraint('geo_jnt126', 'CH:CH_125', w = 1, mo = True)
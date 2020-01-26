import maya.cmds as cmds
cmds.setAttr('dyn_ctrl.DynamicWeight', 0)
for x in range (1,127):
    xStr = str(x)
    geo = 'geo_jnt' + xStr + '_parentConstraint1'
    ikCtrl = geo + '.ik_jnt' + xStr + 'W0'
    cmds.setAttr(ikCtrl, 1 )
    dynCtrl = geo + '.dyn_jnt' + xStr + 'W1'
    cmds.setAttr(dynCtrl, 0)
    cmds.setDrivenKeyframe( attribute = ikCtrl, currentDriver = 'dyn_ctrl.DynamicWeight')
    cmds.setDrivenKeyframe( attribute = dynCtrl, currentDriver = 'dyn_ctrl.DynamicWeight')
    
    

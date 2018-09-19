import maya.cmds as mc
# what i want to do here is turn on the light in the middle
# of the frame range and then have it turn off when the user presses stop.

mc.select( 'Light', visible=True )
mc.ambientLight( 'Light', e=True, intensity=0 )
mc.select( 'bladeJoint', visible=True )
mc.select( 'Light', toggle=True,  )

mc.cutKey( 'ceilingConnecter', time=(0, 360), attribute='rotateY' )        
mc.setKeyframe( 'ceilingConnecter', time=0, attribute='rotateY', value=0 )        
mc.setKeyframe( 'ceilingConnecter', time=360, attribute='rotateY', value=360 )    
mc.keyTangent( 'bladeJoint', inTangentType='linear', outTangentType='linear' )       
mc.select ( 'bladeJoint', clear=True )
mc.setKeyframe( 'Light', time=0, attribute='intensity', value=0 )
mc.setKeyframe( 'Light', time=179, attribute='intensity', value=0 )
mc.setKeyframe( 'Light', time=180, attribute='intensity', value=10 )
mc.select( 'Light', clear=True )
mc.ambientLight( 'Light', e=True, intensity=10 )    
mc.play( forward=True )
#wait

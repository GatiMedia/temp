### DEALING W KNOBS ###

# https://github.com/tianlunjiang/NukeModdingGuide/blob/master/_python/NukeModule.md

# https://learn.foundry.com/nuke/developers/120/pythonreference/nuke.KnobType-class.html

# https://gist.github.com/plasmax/bde3bd503fb6f496c7bb6aea4652e3ef

node = nuke.toNode('NoOp3')
knob = nuke.LookupCurves_Knob('lookup', 'lookup') 
#knob.setRange(1,10)
node.addKnob(knob)




index = nuke.tcl('knob', '-t', knob.node().name() + '.' + knob.name() )

nuke.knob(knobname, type = True) # Returns an int with the knob ID


knob = nuke.toNode('NoOp3').knob('functions').KnobType()
print(knob)




#1
knob = nuke.String_Knob('fRange', 'Track Range')

#3
knob = nuke.Int_Knob('pointNumber', 'Point Number')

#4
knob = nuke.Enumeration_Knob('element', 'element', ['Shapes', 'Strokes'])

#6
knob = nuke.Boolean_Knob('Boolean', '6_Boolean')

#7
knob = nuke.nuke.Double_Knob('Double', '7_Double') 
#knob.setRange(1,10)

#11
knob = nuke.nuke.Channel_Knob('Channel', '11_Channel') 

#15
knob = nuke.BBox_Knob('BBox','15_BBox')

#19
knob = nuke.AColor_Knob('AColor','19_AColor')

#20
knob = nuke.Tab_Knob('custom_tab', 'Custom Tab')

#22
knob = nuke.PyScript_Knob('update', 'Update')

#26
knob = nuke.Text_Knob('warning', '<span style="color:red">invalid index</span>')

#31
knob = nuke.nuke.Box3_Knob('Box3', '31_Box3') 

#40
knob = nuke.ColorChip_Knob('ColorChip','10_ColorChip')

#41
knob = nuke.Link_Knob('test')
knob.setLink( 'root.Blur1.size' )

#43
knob = nuke.Multiline_Eval_String_Knob('info', 'Found')

#68
knob = nuke.nuke.CascadingEnumeration_Knob('CascadingEnum', '68_CascadingEnum', range(3))

#78
knob = nuke.Array_Knob('Array','78_Array')


CTrans['scale'].setSingleValue(False)
CTrans['scale'].setExpression(('Trans_COPY1.scale.w'),0)
CTrans['scale'].setExpression(('Trans_COPY1.scale.h'),1)

typeKnob.value()



# all knobs' name
node = nuke.selectedNode()
for i in range(node.numKnobs()):
    knob = node.knob(i)
    print knob.name()




knob = nuke.toNode('NoOp3').knob('BBox').KnobType()

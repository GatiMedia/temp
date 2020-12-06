### DEALING W KNOBS ###

# https://github.com/tianlunjiang/NukeModdingGuide/blob/master/_python/NukeModule.md

node = nuke.toNode('NoOp3')
knob = nuke.nuke.CascadingEnumeration_Knob('CascadingEl', 'CascadingEl', [A, A/1]]) 
#knob.setRange(1,10)
node.addKnob(knob)


OneView_Knob, Pulldown_Knob, Radio_Knob, CascadingEnumeration_Knob

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
knob = nuke.nuke.Channel_Knob('Channel', 11_'Channel') 

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

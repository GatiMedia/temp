### DEALING W KNOBS ###

# https://github.com/tianlunjiang/NukeModdingGuide/blob/master/_python/NukeModule.md

# https://learn.foundry.com/nuke/developers/120/pythonreference/nuke.KnobType-class.html

# https://gist.github.com/plasmax/bde3bd503fb6f496c7bb6aea4652e3ef

# https://community.foundry.com/discuss/topic/102536/some-knobs-not-returning-the-correct-class

# https://community.foundry.com/discuss/topic/103357/re-mystery-knobs-that-don-t-take-animation


index = nuke.tcl('knob', '-t', knob.node().name() + '.' + knob.name() )


nuke.knob(knobname, type = True) # Returns an int with the knob ID


knob = nuke.toNode('NoOp3').knob('functions')
print(knob)


#0
#nuke.Obsolete_Knob

#1
node = nuke.createNode('NoOp')
knob = nuke.String_Knob('Text', '1_String_Knob')
knob.setText('NewVal')
node.addKnob(knob)

# OR 

node = nuke.createNode('NoOp')
knob = nuke.EvalString_Knob('EvalString', '1_EvalString')
knob.setText('NewVal')
node.addKnob(knob)
# subclass of String_Knob

#2
node = nuke.createNode('NoOp')
knob = nuke.File_Knob('File', '2_File_Knob')
node.addKnob(knob)
knob.fromUserText('/newPath.####.png')
print (knob.getEvaluatedValue())

#3
node = nuke.createNode('NoOp')
knob = nuke.Int_Knob('Int', '3_Int_Knob')
node.addKnob(knob)

#4
node = nuke.createNode('NoOp')
knob = nuke.Enumeration_Knob('Enumeration', '4_Enumeration_Knob', ['A', 'B', 'C'])
node.addKnob(knob)
print (knob.enumName(0))
print (knob.numValues())


#5
node = nuke.createNode('NoOp')
knob = nuke.Bitmask_Knob('Bitmask', '5_Bitmask', ['Opt. 1', 'Opt. 2', 'Opt. 3'])
node.addKnob(knob)
# series of checkbox to pulldown when copied
# ID is 4 - Enumeration_Knob

#6
node = nuke.createNode('NoOp')
knob = nuke.Boolean_Knob('Boolean', '6_Boolean')
node.addKnob(knob)

#7
node = nuke.createNode('NoOp')
knob = nuke.Double_Knob('Double', '7_Double') 
knob.setRange(1,10)
knob.setValue(1)
node.addKnob(knob)

#8
#Float_Knob - "'module' object has no attribute 'Float_Knob'"

#9
node = nuke.createNode('NoOp')
knob = nuke.Array_Knob('Array', '9_Array', 4)
node.addKnob(knob)
knob.setValue(1, 0)
knob.setValue(2, 1)
knob.setValue(3, 2)
knob.setValue(4, 3)
print (knob.arraySize())
# ID is 78 - IArray_Knob

#10
node = nuke.createNode('NoOp')
knob = nuke.ChannelMask_Knob('ChannelMask', '10_ChannelMask')
node.addKnob(knob)
# Doesn't save setting

#11
node = nuke.createNode('NoOp')
knob = nuke.Channel_Knob('Channel', '11_Channel')
node.addKnob(knob)

#12
node = nuke.createNode('NoOp')
knob = nuke.nuke.XY_Knob('XY', '12_XY') 
node.addKnob(knob)
knob.setValue(10, 0)
knob.setValue(20, 1)
print ("""X value is %d and Y is %d.""" % (knob.x(), knob.y()))


#13
node = nuke.createNode('NoOp')
knob = nuke.nuke.XYZ_Knob('XYZ', '13_XYZ') 
knob.setValue(10, 0)
knob.setValue(20, 1)
knob.setValue(30, 2)
node.addKnob(knob)
print ("""X value is %d, Y is %d and Z is %d.""" % (knob.x(), knob.y(), knob.z()))

#14
node = nuke.createNode('NoOp')
knob = nuke.nuke.WH_Knob('WH', '14_WH') 
node.addKnob(knob)
knob.setValue(10, 0)
knob.setValue(20, 1)
print ("""X value is %d and Y is %d.""" % (knob.x(), knob.y()))


#15
node = nuke.createNode('NoOp')
knob = nuke.BBox_Knob('BBox','15_BBox')
node.addKnob(knob)

#knob.fromDict({'x':10, 'y': 20, 'r': 30, 't': 40})

knob.setX(10)
knob.setY(20)
knob.setR(30)
knob.setT(40)
print ("""X value is %d, Y is %d, R is %d and T is %d.""" % (knob.x(), knob.y(), knob.r(), knob.t()))


#16
#Obsoleted by 17 - Was Size_knob ( You can create manually )

#17
node = nuke.createNode('NoOp')
knob = nuke.Format_Knob('Format','17_Format')
node.addKnob(knob)
knob.setValue('HD_1080')

#18
node = nuke.createNode('NoOp')
knob = nuke.Color_Knob('Color','18_Color')
node.addKnob(knob)
# https://support.foundry.com/hc/en-us/articles/360000036479-TP-352820-Panel-Dropped-knob-Duplicating-on-Copy-Paste

#19
node = nuke.createNode('NoOp')
knob = nuke.AColor_Knob('AColor','19_AColor')
node.addKnob(knob)
# https://support.foundry.com/hc/en-us/articles/360000036479-TP-352820-Panel-Dropped-knob-Duplicating-on-Copy-Paste

#20
node = nuke.createNode('NoOp')
knob = nuke.Tab_Knob('Tab', '20_Tab')
node.addKnob(knob)

#21
#Custom_Knob - not in the module

#22
node = nuke.createNode('NoOp')
knob = nuke.PyScript_Knob('PyScript', '22_PyScript', """nuke.message("This is a PyScript Button")""")
node.addKnob(knob)

#23
#Obsoleted by 28 - Was Text_editor_knob.

#24
#Transform2d_Knob - couldn't make it
node = nuke.createNode('NoOp')
knob = nuke.Transform2d_Knob('Transform2d' , '24_Transform2d')
node.addKnob(knob)


val = nuke.toNode('Matrix1')['matrix'].getValue()
print (val)

node = nuke.createNode('NoOp')
knob = nuke.Transform2d_Knob('Transform2d' , '24_Transform2d', val)
node.addKnob(knob)

#25
#Spacer_Knob - "'module' object has no attribute 'Spacer_Knob'"

#26
node = nuke.createNode('NoOp')
knob = nuke.Text_Knob('Text', '26_Text')
node.addKnob(knob)
knob.setValue('This is a Text_Knob')
# Same as a 'Divider Line' if you don't add value and label

#27
node = nuke.createNode('NoOp')
knob = nuke.Help_Knob('Help', '27_Help')
node.addKnob(knob)
# ID 0 - Obsolete - disappear

#28
#MultiLine_String_Knob - 'module' object has no attribute 'MultiLine_String_Knob'

#29
#Axis_knob - 'module' object has no attribute 'Axis_knob'

#30
#UV_knob - 'module' object has no attribute 'UV_knob'

#31
node = nuke.createNode('NoOp')
knob = nuke.Box3_Knob('Box3', '31_Box3') 
node.addKnob(knob)
knob.setX(1)
knob.setY(2)
knob.setN(3)
knob.setR(4)
knob.setT(5)
knob.setF(6)
print ("""X value is %d, Y is %d, N is %d, R is %d, T is %d and F is %d.""" % (knob.x(), knob.y(), knob.n(), knob.r(), knob.t(), knob.f()))

#32
script = """[knob tile_color [ expr { [value hide_input]? 16711935 : 4294902015 }]]"""
node = nuke.createNode('NoOp')
knob = nuke.nuke.Script_Knob('Script', '32_Script', script) 
node.addKnob(knob)

#33
node = nuke.createNode('NoOp')
knob = nuke.nuke.LookupCurves_Knob('LookupCurves', '33_LookupCurves') 
knob.addCurve('NewCurve', '(sin(2*pi*(frame)/.2))/2')
knob.delCurve('default')
node.addKnob(knob)
#Use toScript to get expression value
print (knob.toScript())
# ID 0 - Obsolete - disappear

#34
#n/a - Was Tooltip_knob.

#35
node = nuke.createNode('NoOp')
knob = nuke.Pulldown_Knob('Pulldown', '35_Pulldown', {'1':'nuke.message("Number 1")', '2':'nuke.message("Number 2")', '3':'nuke.message("Number 3")'})
node.addKnob(knob)
print ("Number of options are %d." % knob.numValues())
print ("""The second options`s command is "%s".""" % knob.commands(1))


#36
node = nuke.createNode('NoOp')
knob = nuke.Eyedropper_Knob('Eyedropper', '36_Eyedropper') 
node.addKnob(knob)
# ID 0 - Obsolete - disappear

#37
node = nuke.createNode('NoOp')
knob = nuke.Range_Knob('Range', '37_Range') 
knob.setRange(1,10)
knob.setValue(1)
node.addKnob(knob)
# slider dissappears when copied
# ID is 78 - IArray_Knob

#38
node = nuke.createNode('NoOp')
knob = nuke.Histogram_Knob('Histogram', '38_Histogram') 
node.addKnob(knob)
# ID 0 - Obsolete - disappear

#39
node = nuke.createNode('NoOp')
knob = nuke.Keyer_Knob('Keyer', '39_Keyer') 
node.addKnob(knob)
knob.setValue(1, 0)
knob.setValue(2, 1)
knob.setValue(3, 2)
knob.setValue(4, 3)
print (knob.lowSoft(), knob.lowTol(),knob.highTol(), knob.highSoft())
# UI dissappears when copied
#MJT onCreate trick - https://www.facebook.com/media/set/?set=a.421234635125030&type=3
# ID is 78 - IArray_Knob

#40
node = nuke.createNode('NoOp')
knob = nuke.ColorChip_Knob('ColorChip','40_ColorChip')
node.addKnob(knob)
# without start newline flag

#41
node = nuke.createNode('NoOp')
knob = nuke.Link_Knob('Link', '41_Link')
knob.setLink('root.Blur1.size')
node.addKnob(knob)

#42
node = nuke.createNode('NoOp')
knob = nuke.Scale_Knob('Scale','42_Scale')
node.addKnob(knob)
knob.setValue(1, 0)
knob.setValue(2, 1)
knob.setValue(3, 2)
print ("""X is {0}, Y is {1} and Z is {2}.""" .format(knob.x(), knob.y(), knob.z()))
# ID is 78 - IArray_Knob

#43
node = nuke.createNode('NoOp')
knob = nuke.Multiline_Eval_String_Knob('Multiline_Eval', '43_Multiline_Eval')
node.addKnob(knob)

#44
node = nuke.createNode('NoOp')
knob = nuke.OneView_Knob('OneView', '44_OneView', ['a','b','c'])
node.addKnob(knob)
# ID is 4 - Enumeration_Knob

#45
node = nuke.createNode('NoOp')
knob = nuke.MultiView_Knob('MultiView', '45_MultiView')
node.addKnob(knob)
knob.setValue('main')
print (knob.toScript())

#46
node = nuke.createNode('NoOp')
knob = nuke.ViewView_Knob('ViewView', '46_ViewView')
node.addKnob(knob)
# ID 0 - Obsolete - disappear

#47
#PyPulldown_knob - not in the module

#48
#GPUEngine_knob - not in the module

#49
#MultiArray_knob - Generally Table_knob is a better choice.

#50
#ViewPair_knob - not in the module

#51
#List_knob - not in the module

#52
node = nuke.createNode('NoOp')
knob = nuke.PythonKnob('PyScript', '52_PyScript')
node.addKnob(knob)
# ID is 1 - String_Knob

#53
#MetaData_knob - not in the module

#54
#PixelAspect_knob - not in the module

#55
#CP_knob - Obsolete. Do not use.

#56
#BeginToolbar/EndToolbar - not in the module

#57
node = nuke.createNode('NoOp')
knob1 = nuke.BeginTabGroup_Knob()
knob2 = nuke.EndTabGroup_Knob()
node.addKnob(knob1)
node.addKnob(knob2)
knob1.setLabel('57_TabGroup')
# Doesn't set name or label from argument

#58
#PluginPython_knob - donno what happened here

#59
#BeginExoGroup/EndExoGroup - not in the module

#60
#Menu_knob - not in the module

#61
node = nuke.createNode('NoOp')
knob = nuke.Password_Knob('Password', '61_Password')
node.addKnob(knob)

#62
#Toolbox_knob - DO not use

#63
#Table_knob - not in the module

#64
node = nuke.createNode('NoOp')
knob = nuke.GeoSelect_Knob('GeoSelect', '64_GeoSelect')
node.addKnob(knob)
#Didn't work

#65
#InputOnly_ChannelSet_knob - not in the module

#66
#InputOnly_Channel_knob - not in the module

#67
#ControlPointCollection_knob - DO no use

#68
node = nuke.createNode('NoOp')
knob = nuke.nuke.CascadingEnumeration_Knob('CascadingEnum', '68_CascadingEnum', ['1/A', '1/B', '1/C', '2', '3' ])
node.addKnob(knob)

#69
#Dynamic_Bitmask_knob - not in the module

#70
#MetaKeyFrame_knob - not in the module

#71
#PositionVector_knob - not in the module

#72
#Cached_File_knob - not in the module

#73
#TransformJack_knob - DO not use

#74
#Ripple_knob - not in the module

#75
node = nuke.createNode('NoOp')
knob = nuke.SceneView_Knob('SceneView','75_SceneView', nuke.views())
node.addKnob(knob)
knob.addItems(['new_item_1', 'new_item_1/A', 'new_item_1/B', 'new_item_2'])
print(knob.getAllItems())
knob.removeItems(['new_item_2'])
print(knob.getAllItems())
# Items disappear when copied

#76
#VSpacer_Knob - not in the module

#77
#CancelExecution_Knob - not in the module

#78
node = nuke.createNode('NoOp')
knob = nuke.IArray_Knob('Array', '78_Array', [3, 3])
node.addKnob(knob)
# 2 lines disappear and set animated when copied - seems broken

#79
#ResizableArray_Knob - not in the module

#80
node = nuke.createNode('NoOp')
knob = nuke.Disable_Knob('Disable', '80_Disable')
node.addKnob(knob)

#81
#Icon_Knob - not in the module

#82
#FrameExtent_Knob - not in the module

#83
node = nuke.createNode('NoOp')
knob = nuke.Radio_Knob('Radio', '83_Radio', ('red', 'green', 'blue', 'alpha'))
node.addKnob(knob)

#84
node = nuke.createNode('NoOp')
knob = nuke.FreeType_Knob('Font', '84_FreeType')
node.addKnob(knob)

node = nuke.createNode('NoOp')
knob = nuke.Font_Knob('Font', 'Font')
node.addKnob(knob)
# ID 0 - Obsolete - disappear - Use FreeType_Knob instead

#85
node = nuke.createNode('NoOp')
knob = nuke.EditableEnumeration_Knob('EditableEnumeration', 'EditableEnumeration', ['1','2','3','something'])
node.addKnob(knob)
print (knob.enumName(3))
print (knob.numValues())



# print knob's info
n = nuke.selectedNode()
a = n['size']
knob = (n.name() + '.' + a.name())
print ("""The knob`s class is {0}, name is "{1}" and ID is {2}.""" .format(a.Class(), a.name() , nuke.tcl('knob', '-t', knob)))


# all knobs' name
node = nuke.selectedNode()
for i in range(node.numKnobs()):
    knob = node.knob(i)
    print knob.name()

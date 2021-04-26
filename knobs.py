### DEALING W KNOBS ###

# https://github.com/tianlunjiang/NukeModdingGuide/blob/master/_python/NukeModule.md

# https://learn.foundry.com/nuke/developers/120/pythonreference/nuke.KnobType-class.html

# https://gist.github.com/plasmax/bde3bd503fb6f496c7bb6aea4652e3ef

# https://community.foundry.com/discuss/topic/102536/some-knobs-not-returning-the-correct-class

# https://community.foundry.com/discuss/topic/103357/re-mystery-knobs-that-don-t-take-animation

#https://www.facebook.com/media/set/?set=a.421234635125030&type=3


index = nuke.tcl('knob', '-t', knob.node().name() + '.' + knob.name() )


nuke.knob(knobname, type = True) # Returns an int with the knob ID


knob = nuke.toNode('NoOp3').knob('functions').KnobType()
print(knob)


#0
#nuke.Obsolete_Knob

#1
node = nuke.toNode('NoOp')
knob = nuke.String_Knob('Text', '1_String_Knob')
node.addKnob(knob)

# OR 

node = nuke.toNode('NoOp')
knob = nuke.EvalString_Knob('EvalString', 'EvalString')
node.addKnob(knob)

#2
node = nuke.toNode('NoOp')
knob = nuke.File_Knob('File', '2_File_Knob')
node.addKnob(knob)

#3
node = nuke.toNode('NoOp')
knob = nuke.Int_Knob('Int', '3_Int_Knob')
node.addKnob(knob)

#4
node = nuke.toNode('NoOp')
knob = nuke.Enumeration_Knob('Enumeration', '4_Enumeration_Knob', ['A', 'B', 'C'])
node.addKnob(knob)

#5
node = nuke.toNode('NoOp')
knob = nuke.Bitmask_Knob('Bitmask', '5_Bitmask', ['Opt. 1', 'Opt. 2', 'Opt. 3'])
node.addKnob(knob)
# checkbox to pulldown

#6
node = nuke.toNode('NoOp')
knob = nuke.Boolean_Knob('Boolean', '6_Boolean')
node.addKnob(knob)

#7
node = nuke.toNode('NoOp')
knob = nuke.nuke.Double_Knob('Double', '7_Double') 
knob.setRange(1,10)
knob.setValue(1)
node.addKnob(knob)

#8
#Float_Knob - "'module' object has no attribute 'Float_Knob'"

#9
node = nuke.toNode('NoOp')
knob = nuke.Array_Knob('Array', '9_Array', 3)
node.addKnob(knob)

#10
node = nuke.toNode('NoOp')
knob = nuke.ChannelMask_Knob('ChannelMask', '10_ChannelMask')
node.addKnob(knob)

#11
node = nuke.toNode('NoOp')
knob = nuke.Channel_Knob('Channel', '11_Channel') 
node.addKnob(knob)

#12
node = nuke.toNode('NoOp')
knob = nuke.nuke.XY_Knob('XY', '12_XY') 
node.addKnob(knob)

#13
node = nuke.toNode('NoOp')
knob = nuke.nuke.XYZ_Knob('XYZ', '13_XYZ') 
node.addKnob(knob)

#14
node = nuke.toNode('NoOp')
knob = nuke.nuke.WH_Knob('WH', '14_WH') 
node.addKnob(knob)

#15
node = nuke.toNode('NoOp')
knob = nuke.BBox_Knob('BBox','15_BBox')
node.addKnob(knob)

#16
#Obsoleted by 17 - Was Size_knob

#17
node = nuke.toNode('NoOp')
knob = nuke.Format_Knob('Format','17_Format')
node.addKnob(knob)

#18
node = nuke.toNode('NoOp')
knob = nuke.Color_Knob('Color','18_Color')
node.addKnob(knob)
# https://support.foundry.com/hc/en-us/articles/360000036479-TP-352820-Panel-Dropped-knob-Duplicating-on-Copy-Paste

#19
node = nuke.toNode('NoOp')
knob = nuke.AColor_Knob('AColor','19_AColor')
node.addKnob(knob)
# https://support.foundry.com/hc/en-us/articles/360000036479-TP-352820-Panel-Dropped-knob-Duplicating-on-Copy-Paste

#20
node = nuke.toNode('NoOp')
knob = nuke.Tab_Knob('custom_tab', '20_Custom Tab')
node.addKnob(knob)

#21
#Custom_Knob - not in the module

#22
node = nuke.toNode('NoOp')
knob = nuke.PyScript_Knob('PyScript', '22_PyScript', """nuke.message("This is a PyScript Button")""")
node.addKnob(knob)

#23
#Obsoleted by 28 - Was Text_editor_knob.

#24
#Transform2d_Knob - couldn't make it

node = nuke.toNode('NoOp')
knob = nuke.Transform2d_Knob('Text', '26_Text')
node.addKnob(knob)

#25
#Spacer_Knob - "'module' object has no attribute 'Spacer_Knob'"

#26
node = nuke.toNode('NoOp')
knob = nuke.Text_Knob('Text', '26_Text')
node.addKnob(knob)

#27
node = nuke.toNode('NoOp')
knob = nuke.Help_Knob('Help', '27_Help')
node.addKnob(knob)

#28
#MultiLine_String_Knob - 'module' object has no attribute 'MultiLine_String_Knob'

#29
#Axis_knob - 'module' object has no attribute 'Axis_knob'

#30
#UV_knob - 'module' object has no attribute 'UV_knob'

#31
node = nuke.toNode('NoOp')
knob = nuke.nuke.Box3_Knob('Box3', '31_Box3') 
node.addKnob(knob)

#32
node = nuke.toNode('NoOp')
knob = nuke.nuke.Script_Knob('Script', '32_Script') 
node.addKnob(knob)

#33
node = nuke.toNode('NoOp')
knob = nuke.nuke.LookupCurves_Knob('LookupCurves', '33_LookupCurves') 
knob.addCurve('NewCurve', '(sin(2*pi*(frame)/.2))/2')
knob.delCurve('default')
node.addKnob(knob)
#seems broken - doesn't add name and serial number, can't be copied

#34
#n/a - Was Tooltip_knob.

#35
node = nuke.toNode('NoOp')
knob = nuke.Pulldown_Knob('Pulldown', '35_Pulldown', {'1':'nuke.message("Number 1")', '2':'nuke.message("Number 2")', '3':'nuke.message("Number 3")'})
node.addKnob(knob)


#36
node = nuke.toNode('NoOp')
knob = nuke.Eyedropper_Knob('Eyedropper', '36_Eyedropper') 
node.addKnob(knob)
# dissappears if not linked

#37
node = nuke.toNode('NoOp')
knob = nuke.Range_Knob('Range', '37_Range') 
knob.setRange(1,10)
knob.setValue(1)
node.addKnob(knob)
# slider dissappears

#38
node = nuke.toNode('NoOp')
knob = nuke.Histogram_Knob('Histogram', '38_Histogram') 
node.addKnob(knob)
# dissappears if not linked

#39
node = nuke.toNode('NoOp')
knob = nuke.Keyer_Knob('Keyer', '39_Keyer') 
node.addKnob(knob)
# dissappears if not linked
#MJT onCreate trick - https://www.facebook.com/media/set/?set=a.421234635125030&type=3

#40
node = nuke.toNode('NoOp')
knob = nuke.ColorChip_Knob('ColorChip','40_ColorChip')
node.addKnob(knob)
# without start newline flag

#41
node = nuke.toNode('NoOp')
knob = nuke.Link_Knob('Link', '41_Link')
knob.setLink('root.Blur1.size')
node.addKnob(knob)

#42
node = nuke.toNode('NoOp')
knob = nuke.Scale_Knob('Scale','42_Scale')
node.addKnob(knob)

#43
node = nuke.toNode('NoOp')
knob = nuke.Multiline_Eval_String_Knob('Multiline_Eval', '43_Multiline_Eval')
node.addKnob(knob)

#44
node = nuke.toNode('NoOp')
knob = nuke.OneView_Knob('OneView', '44_OneView', ['a','b','c'])
node.addKnob(knob)

#45
node = nuke.toNode('NoOp')
knob = nuke.MultiView_Knob('MultiView', '45_MultiView')
node.addKnob(knob)

#46
node = nuke.toNode('NoOp')
knob = nuke.ViewView_Knob('ViewView', '46_ViewView')
node.addKnob(knob)

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
node = nuke.toNode('NoOp')
knob = nuke.PythonKnob('PyScript', '52_PyScript')
node.addKnob(knob)
# seems same as #1 String_Knob

#53
#MetaData_knob - not in the module

#54
#PixelAspect_knob - not in the module

#55
#CP_knob - Obsolete. Do not use.

#56
#BeginToolbar/EndToolbar - not in the module

#57
node = nuke.toNode('NoOp')
knob1 = nuke.BeginTabGroup_Knob('TabGroup1', '57_TabGroup')
knob2 = nuke.EndTabGroup_Knob('TabGroup2')
node.addKnob(knob1)
node.addKnob(knob2)

#58
#PluginPython_knob - donno what happened here

#59
#BeginExoGroup/EndExoGroup - not in the module

#60
#Menu_knob - not in the module

#61
node = nuke.toNode('NoOp')
knob = nuke.Password_Knob('Password', '61_Password')
node.addKnob(knob)

#62
#Toolbox_knob - DO not use

#63
#Table_knob - not in the module

#64
node = nuke.toNode('NoOp')
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
node = nuke.toNode('NoOp')
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
node = nuke.toNode('NoOp')
knob = nuke.SceneView_Knob('SceneView','75_SceneView', nuke.views())
node.addKnob(knob)

#76
#VSpacer_Knob - not in the module

#77
#CancelExecution_Knob - not in the module

#78
node = nuke.toNode('NoOp')
knob = nuke.IArray_Knob('Array', '78_Array', [3, 3])
node.addKnob(knob)
#dissappears

#79
#ResizableArray_Knob - not in the module

#80
node = nuke.toNode('NoOp')
knob = nuke.Disable_Knob('Disable', '80_Disable')
node.addKnob(knob)

#81
#Icon_Knob - not in the module

#82
#FrameExtent_Knob - not in the module

#83
node = nuke.toNode('NoOp')
knob = nuke.Radio_Knob('Radio', '83_Radio', ('red', 'green', 'blue', 'alpha'))
node.addKnob(knob)

#84
node = nuke.toNode('NoOp')
knob = nuke.FreeType_Knob('Font', '84_FreeType')
node.addKnob(knob)

#85
node = nuke.toNode('NoOp')
knob = nuke.EditableEnumeration_Knob('EditableEnumeration', 'EditableEnumeration', ['1','2','3'])
node.addKnob(knob)

node = nuke.toNode('NoOp')
knob = nuke.Font_Knob('Font', 'Font')
node.addKnob(knob)


nuke.PyCustom_Knob
nuke.PythonCustomKnob

# print knob's ID number
n = nuke.toNode("Text32")
a = n['font']
knob = (n.name() + '.' + a.name())
print nuke.tcl('knob', '-t', knob)


# all knobs' name
node = nuke.selectedNode()
for i in range(node.numKnobs()):
    knob = node.knob(i)
    print knob.name()

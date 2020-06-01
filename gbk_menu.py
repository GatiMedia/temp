# --------------------------------------------------------------
#  menu.py
#  Version: 1.0.10
#  Last Updated: June 1st, 2020
# --------------------------------------------------------------

# --------------------------------------------------------------
#  GLOBAL IMPORTS ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

import nuke
import platform

# --------------------------------------------------------------
#  PYCHARM CHEAT SHEET :::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

# Ctrl + '/' - shortcut for comment out and remove comment
# Ctrl + 'D' - duplicate line
# TAB - indent selected line(s)
# TAB + SHIFT - unindent selected line(s)

# --------------------------------------------------------------
#  KNOB DEFAULTS  ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

### labels ###
#image
nuke.knobDefault('Read.label', "Fr. range: [value first] - [value last]\nRes: [value width] * [value height]")
nuke.knobDefault('Write.label', "Channels: [string toupper [value channel]]")
nuke.knobDefault('Constant.label', "Res: [value width] * [value height]")
nuke.knobDefault('CheckerBoard2.label', "Res: [value width] * [value height]")

#draw

#time
nuke.knobDefault('TimeOffset.label', "Value: [value time_offset]")
nuke.knobDefault('Retime.label', "Out: [value output.first] - [value output.last]")

#channel
nuke.knobDefault('Shuffle.label', "[string toupper [value in]]")
nuke.knobDefault('ShuffleCopy.label', "[string toupper [value in]]")

#color
nuke.knobDefault('Colorspace.label', "[value colorspace_in] to [value colorspace_out]")
nuke.knobDefault('OCIOColorSpace.label', "[value in_colorspace] to [value out_colorspace]")
nuke.knobDefault('Saturation.label', "Value: [value saturation]")
nuke.knobDefault('Multiply.label', "Value: [value value]")

#filter
nuke.knobDefault('Blur.label', "Size: [value size]")
nuke.knobDefault('Defocus.label', "Size: [value defocus]")
nuke.knobDefault('ZDefocus2.label', "Size: [value size]")
nuke.knobDefault('EdgeBlur.label', "Size: [value size]")
nuke.knobDefault('Sharpen.label', "Size: [value size]")
nuke.knobDefault('Soften.label', "Size: [value size]")

#keyer

#merge
nuke.knobDefault('Switch.label', "Which: [value which]")
nuke.knobDefault('Dissolve.label', "Which: [value which]")

#transform
nuke.knobDefault('Crop.label', "Box: x:[value box.x]  y:[value box.y] r:[value box.r] t:[value box.t]")
nuke.knobDefault('IDistort.label', "Scale: [value uv_scale]")
nuke.knobDefault('SplineWarp3.label', "Out: [string toupper [value output_enum]]")
nuke.knobDefault('STMap.label', "UV: [value uv]")
nuke.knobDefault('VectorDistort.label', "[value referenceFrame]")

#3D
nuke.knobDefault('Camera2.label', "File: [file tail [value file]]")
nuke.knobDefault('ReadGeo2.label', "File: [file tail [value file]]\n[string toupper [value display]]\nRender: [string toupper [value render_mode]]")
nuke.knobDefault('Card2.label', "Display: [string toupper [value display]]\nRender: [string toupper [value render_mode]]")
nuke.knobDefault('Cube.label', "Display: [string toupper [value display]]\nRender: [string toupper [value render_mode]]")
nuke.knobDefault('Cylinder.label', "Display: [string toupper [value display]]\nRender: [string toupper [value render_mode]]")
nuke.knobDefault('Sphere.label', "Display: [string toupper [value display]]\nRender: [string toupper [value render_mode]]")
nuke.knobDefault('Scene.label', "Display: [string toupper [value display]]\nRender: [string toupper [value render_mode]]")

#other
nuke.knobDefault('nuke_dispatch.label', '''Range: [value framestart] - [value frameend]\nBatch: [value batch]\nLic. Rem.: [if {[value removelicense]==true} {return "On"} {return "Off"}]''')

#######

#image

#draw
nuke.knobDefault('Text2.xjustify', "center")
nuke.knobDefault('Text2.yjustify', "center")

#time

#channel

#color

#filter
nuke.knobDefault('Blur.size', "2")
nuke.knobDefault('DirBlurWrapper.BlurTye', "linear")
nuke.knobDefault('DirBlurWrapper.BlurLayer', "rgba")

#keyer

#merge
nuke.knobDefault('Merge.bbox', 'B')
nuke.knobDefault('Merge.also_merge', 'all')
nuke.knobDefault('ContactSheet.roworder', 'TopBottom')
nuke.knobDefault('ContactSheet.width', 'input.width*columns')
nuke.knobDefault('ContactSheet.height', 'input.height*rows')

#transform


#3D
nuke.knobDefault('Project3D.crop', "false")


#other
nuke.knobDefault('nuke_dispatch.batch', "1")
nuke.knobDefault('Dot.note_font_size', "72")
nuke.knobDefault('BackdropNode.note_font_size', "72")
nuke.knobDefault('StickyNote.note_font_size', "22")

# --------------------------------------------------------------
#  USEFUL SNIPPETS :::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

# From https://www.ftrack.com/en/2019/09/8-ways-to-increase-your-efficiency-with-foundrys-nuke.html

def close():
    for node in nuke.allNodes():
        node.hideControlPanel()

nuke.menu('Nodes').addCommand('close', 'close()' , 'shift+d')

# Tracker ref frame on current frame

nuke.addOnUserCreate( lambda :nuke.thisNode()[ 'reference_frame' ].setValue(nuke.frame()), nodeClass= 'Tracker4' )

# From http://www.lookinvfx.com/nuke-python-snippets/

def disconnectViewers():
    nuke.selectAll()
    nuke.invertSelection()

    for n in nuke.allNodes():
        if n.Class() == "Viewer":
            n['selected'].setValue(True)

    nuke.extractSelected()


nuke.addOnScriptLoad(disconnectViewers)

# based on Ben`s Foundry webinar

def RotoBlur_Shortcut():
    y_offset = 60
    r = nuke.createNode('Roto', 'output rgba')
    y = int(r.ypos() + y_offset)
    b = nuke.nodes.Blur()
    b['size'].setValue(2)
    b['xpos'].setValue(r.xpos())
    b['ypos'].setValue(y)
    b.setInput(0,r)
    b.hideControlPanel()

nuke.menu('Nodes').addMenu('Draw').addCommand('Create Roto and Blur node.', 'RotoBlur_Shortcut()', shortcut='o', icon='Roto.png')


# --------------------------------------------------------------
#  SHORTCUTS ::::::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

nuke.toolbar('Nodes').addCommand('Channel/ChannelMerge', 'nuke.createNode("ChannelMerge")', 'shift+c', shortcutContext=dagContext)

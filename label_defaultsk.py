# -------- LABEL ---------------

#image
nuke.knobDefault('Read.label', "Fr. range: [value first] - [value last]\nRes: [value width] * [value height]")
nuke.knobDefault('Constant.label', "Res: [value width] * [value height]")
nuke.knobDefault('CheckerBoard2.label', "Res: [value width] * [value height]")

#draw

#time
nuke.knobDefault('TimeOffset.label', "Value: [value time_offset]")
nuke.knobDefault('Retime.label', "Out: [value output.first] - [value output.last]")

#channel
nuke.knobDefault('Shuffle.label', "[string toupper [value in1]]")
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
nuke.knobDefault('Merge.label', "[knob tile_color [ expr { [value disable]? 4278190335 : 0 }]]")

#transform
nuke.knobDefault('Crop.label', "Box: x:[value box.x]  y:[value box.y] r:[value box.r] t:[value box.t]")
nuke.knobDefault('IDistort.label', "Scale: [value uv_scale]")
nuke.knobDefault('SplineWarp3.label', "Out: [string toupper [value output_enum]]")
nuke.knobDefault('STMap.label', "UV: [value uv]")
nuke.knobDefault('VectorDistort.label', "Ref fr.: [value reference_frame]\nOutput: [value output_mode]")
nuke.knobDefault('Reformat.label', '''[if {[value this.type]=="scale"} {return "Scale: [value this.scale]"} {return ""}]''')

#3D
nuke.knobDefault('Camera2.label', "File: [file tail [value file]]")
nuke.knobDefault('ReadGeo2.label', "File: [file tail [value file]]\n[string toupper [value display]]\nRender: [string toupper [value render_mode]]")
nuke.knobDefault('Card2.label', "Display: [string toupper [value display]]\nRender: [string toupper [value render_mode]]")
nuke.knobDefault('Cube.label', "Display: [string toupper [value display]]\nRender: [string toupper [value render_mode]]")
nuke.knobDefault('Cylinder.label', "Display: [string toupper [value display]]\nRender: [string toupper [value render_mode]]")
nuke.knobDefault('Sphere.label', "Display: [string toupper [value display]]\nRender: [string toupper [value render_mode]]")
nuke.knobDefault('Scene.label', "Display: [string toupper [value display]]\nRender: [string toupper [value render_mode]]")


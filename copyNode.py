########## COPY NODES ##########

## WIP code - doesn't work on Groups and need reverse function with keeping animation

if len(nuke.selectedNodes()) > 0:
    for node in nuke.selectedNodes():
        sel_node = node
        usual_knobs = ['name', 'help', 'onCreate', 'onDestroy', 'knobChanged', 'updateUI', 'autolabel', 'panel',
                       'tile_color', 'gl_color', 'label', 'note_font', 'note_font_size', 'note_font_color', 'selected',
                       'xpos', 'ypos', 'icon', 'indicators', 'hide_input', 'rootNodeUpdated', 'channel', 'layer', 'enable',
                       'cached', 'disable', 'dope_sheet', 'bookmark', 'postage_stamp', 'postage_stamp_frame',
                       'lifetimeStart', 'lifetimeEnd', 'useLifetime']

        new_knobs = []
        for knob in sel_node.knobs():
            new_knobs.append(knob)

        curr_knobs = [x for x in new_knobs if x not in usual_knobs]

        new_node = nuke.createNode(sel_node.Class())
        new_node['ypos'].setValue(sel_node['ypos'].value())
        new_node['xpos'].setValue(sel_node['xpos'].value() + 220)

        #new_node['label'].setValue(new_node['label'].value() + "\nChild")

        #if not sel_node['label'].value().endswith("Parent"):
            #sel_node['label'].setValue(sel_node['label'].value() + "\nParent")
        #else:
            #pass

        for knob in curr_knobs:
            new_node[knob].setExpression(sel_node.name() + "." + knob)
            
        new_node.setSelected(True)
        nukescripts.remove_inputs()
            
        new_node.setSelected(False)
        new_node.hideControlPanel()
else:
    nuke.message('Select a single node first!')

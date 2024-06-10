# --------------------------------------------------------------
#  copy_connected_node.py
#  Version: 1.0
#  Last Updated: 21/05/2024
#  Last updated by: Attila Gasparetz
# --------------------------------------------------------------
import nuke
import nukescripts
import shlex

def copy_connected_node():
    if len(nuke.selectedNodes()) > 0:
        sel_nodes = nuke.selectedNodes()
        new_nodes = []
        for node in sel_nodes:
            sel_node = node
            usual_knobs = ['name', 'help', 'onCreate', 'onDestroy', 'knobChanged', 'updateUI', 'autolabel', 'panel',
                           'tile_color', 'gl_color', 'label', 'note_font', 'note_font_size', 'note_font_color', 'selected',
                           'xpos', 'ypos', 'icon', 'indicators', 'hide_input', 'rootNodeUpdated', 'channel', 'layer',
                           'enable',
                           'cached', 'dope_sheet', 'bookmark', 'postage_stamp', 'postage_stamp_frame',
                           'lifetimeStart', 'lifetimeEnd', 'useLifetime', 'use_gpu', 'lock_connections']

            skip_knobs = ['PathExpression_Knob', 'SceneGraph_Knob', 'EditableEnumeration_Knob', 'Font_Knob', 'FreeType_Knob', 'SceneView_Knob', 'Password_Knob', 'ViewView_Knob', 'MultiView_Knob', 'Histogram_Knob', 'Eyedropper_Knob', 'LookupCurves_Knob', 'File_Knob', 'PyScript_Knob', 'PythonKnob', 'Script_Knob', 'Text_Knob', 'Tab_Knob', 'String_Knob', 'EvalString_Knob', 'Multiline_Eval_String_Knob', 'ColorChip_Knob', 'Obsolete_Knob']

            new_knobs = []
            for knob in sel_node.knobs():
                new_knobs.append(knob)

            for k in new_knobs:
                if k.endswith("_panelDropped"):
                    new_knobs.remove(k)

            curr_knobs = [x for x in new_knobs if x not in usual_knobs]

            # selecting single node to copy
            nuke.selectAll()
            nuke.invertSelection()
            sel_node.setSelected(True)
            nuke.nodeCopy("%clipboard%")

            # making new node
            new_node = nuke.nodePaste("%clipboard%")
            new_node['ypos'].setValue(sel_node['ypos'].value())
            new_node['xpos'].setValue(sel_node['xpos'].value() + 220)

            # setting expression
            for knob in curr_knobs:
                try:
                    new_node[knob].setExpression(sel_node.name() + "." + knob)
                except:
                    continue

            # checking if any knobs erroring and need dofferent expression
            errorList = []
            error_knobs = []
            link_knobs = []
            for knob in new_node.allKnobs():
                if not any(x in str(knob) for x in skip_knobs):
                    # print(knob)
                    if "Link_Knob" in str(knob):
                        link_knobs.append(knob.fullyQualifiedName().split('.')[1])
                    if knob.hasExpression():
                        print(knob)
                        expression = shlex.split(knob.toScript().strip('{}').replace(" ", ""))
                        full_name = knob.fullyQualifiedName()
                        try:
                            nuke.tcl('in {} {{expression {}}}'.format(full_name, expression[0]))
                        except RuntimeError as tcl_error:
                            errorList.append('{}: {}'.format(full_name, tcl_error))
                            error_knobs.append(full_name.split('.')[1])
                else:
                    continue

            # if expression erroring, setting alternative expressions
            if "Nothing is named" in errorList:
                pass
            else:
                for knob in error_knobs:
                    new_node[knob].setExpression("parent." + sel_node.name() + "." + str(knob))
                for knob in link_knobs:
                    new_node[knob].setExpression("parent.parent." + sel_node.name() + "." + str(knob))

            new_node.setSelected(True)
            nukescripts.remove_inputs()
            new_node.setSelected(False)
            new_node.hideControlPanel()
            new_nodes.append(new_node.name())
        for n in new_nodes:
            nuke.toNode(n).setSelected(True)
    else:
        nuke.message('Select some node/nodes first!')

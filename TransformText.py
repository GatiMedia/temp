def TransformText():
    tr = nuke.createNode('Transform') #Create Transform node
    te = nuke.nodes.Text2() #Create Text node
    y_offset = 50 #Set up offset value
    y = int(tr.ypos() + y_offset) #Set up y offset value

    te['name'].setValue(tr['name'].value() + "_Text") #Set up Text's name

    #Adding callback to a Text node to be enabled only when Transform opened
    te['knobChanged'].setValue("""if nuke.thisNode().dependencies()[0].shown():
    nuke.thisNode()['disable'].setValue(0)
else:
    nuke.thisNode()['disable'].setValue(1)
""")

    #Setting up the transformation expressions on a Text node
    te.showControlPanel()
    animLayers = te['group_animations'].getAllItems()
    te['group_animations'].setSelectedItems(animLayers)
    te["translate"].setExpression("[value this.input.translate.x]", 0)
    te["translate"].setExpression("[value this.input.translate.y]", 1)
    te["rotate"].setExpression("[value this.input.rotate]")
    te["scale"].setExpression("[value this.input.scale.w]", 0)
    te["scale"].setExpression("[value this.input.scale.h]", 1)
    te["skewX"].setExpression("[value this.input.skewX]")
    te["skewY"].setExpression("[value this.input.skewY]")
    te["center"].setExpression("[value this.input.center.x]", 0)
    te["center"].setExpression("[value this.input.center.y]", 1)

    #Setting up a colors to be red
    te['color'].setSingleValue(False)
    te['color'].setValue(1, 0)
    te['color'].setValue(0.1, 1)
    te['color'].setValue(0.1, 2)

    #Setting up the position of the Text node
    te['xpos'].setValue(tr.xpos())
    te['ypos'].setValue(y)

    #Setting up the 'message' to show input's name and the size and text box
    te['message'].setValue('[value this.input.name]')
    te['global_font_scale'].setValue(0.4)
    te['box'].setValue(( te['box'].value()[3] - te['box'].value()[1] ) + tr['center'].value()[1], 3)
    te['box'].setValue(500 + tr['center'].value()[0], 2)
    te['box'].setValue(tr['center'].value()[1], 1)
    te['box'].setValue(tr['center'].value()[0], 0)

    te.hideControlPanel() #Closing Text node's control panel

    te.setInput(0, tr) #Setting Text node's input to be the Transform

    tr_name = tr['name'].value() #Storing Transform's name

    #Search/connect nodes that are connected to the created Transform
    for node in nuke.allNodes():
        try:
            if node.input(0).name() == tr_name:
                node.setInput(0, te)
        except Exception:
            pass

    #Selecting the Text node 
    te.setSelected(True)
        
#Adding the function to the Node's menu under Transform
nuke.menu('Nodes').addMenu('Transform').addCommand('Create Transform and Text node.', 'TransformText()', shortcut='t', icon='Transform.png')

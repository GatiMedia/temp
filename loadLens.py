### LOADLENS WIP ###

def loadLens():
    import os
    from os import listdir
    from os.path import isfile, join

    if nuke.selectedNodes('Read'):
        for n in nuke.selectedNodes('Read'):
            filepath = n['file'].value()
            filename = (os.path.basename(filepath)).split("_")
            newpath = "/jobs/050138_DISN_Nautilus/UNIT/vfx/"+filename[1]+"/"+filename[2]+"/"+filename[3]+"/matchmove/"
            def get_immediate_subdirectories(a_dir):
                return [name for name in os.listdir(a_dir)
                if os.path.isdir(os.path.join(a_dir, name))]
            dirs = get_immediate_subdirectories(newpath)
            dirs.sort()
            matchmove_path_files = dirs[-1]

            almost_final_path = newpath + matchmove_path_files + "/3DE Lens Distortion node/"
            if os.path.isdir(almost_final_path):
                lens_path_files = [f for f in listdir(almost_final_path)][-1]
                final_path = almost_final_path + lens_path_files

                # create undistort LD node on STMap
                nuke.nodePaste(final_path)
                ldNode = nuke.selectedNode()
                ldNode['direction'].setValue('undistort')
                ldNode['mode'].setValue('STMap')
                ldNode.setSelected(False)

                # create dot1
                dot1 = nuke.nodes.Dot()
                dot1['xpos'].setValue(int(n['xpos'].value()+(n.screenWidth()/2)))
                dot1['ypos'].setValue(int(n['ypos'].value())+200)
                dot1.setSelected(False)

                # set position for LD nodes
                ldNode['xpos'].setValue(int(dot1['xpos'].value()-n.screenWidth()/2))
                ldNode['ypos'].setValue(int(dot1['ypos'].value())+150)

                # create CropMain
                CropMain = nuke.nodes.Crop()
                CropMain['xpos'].setValue(int(n['xpos'].value()))
                CropMain['ypos'].setValue(int(ldNode['ypos'].value())+100)
                CropMain['box'].setExpression("input.bbox.x", 0)
                CropMain['box'].setExpression("input.bbox.y", 1)
                CropMain['box'].setExpression("input.bbox.r", 2)
                CropMain['box'].setExpression("input.bbox.t", 3)
                CropMain['reformat'].setValue(True)
                CropMain.setSelected(False)

                # create distort LD node on STMap
                nuke.nodePaste(final_path)
                ldNode2 = nuke.selectedNode()
                ldNode2['direction'].setValue('distort')
                ldNode2['mode'].setValue('STMap')
                ldNode2.setSelected(False)

                # create calculator
                calculator = nuke.nodes.NoOp()
                calculator['xpos'].setValue(int(CropMain['xpos'].value()))
                calculator['ypos'].setValue(int(CropMain['ypos'].value())+100)
                calculator['label'].setValue("just a calculator")

                # adding knobs to calculator
                topW = nuke.Double_Knob('topnodeWidth', 'topnodeWidth') 
                topW.setExpression("[lrange [split [value [topnode].format]  ] 0 0 ]")
                calculator.addKnob(topW)

                bboxW = nuke.Double_Knob('bboxWidth', 'bboxWidth') 
                bboxW.setExpression("(-input.box.x)*2")
                calculator.addKnob(bboxW)

                scaleW = nuke.Double_Knob('scaleWidth', 'scaleWidth') 
                scaleW.setExpression("(topnodeWidth+bboxWidth)/topnodeWidth")
                calculator.addKnob(scaleW)

                topH = nuke.Double_Knob('topnodeHeight', 'topnodeHeight') 
                topH.setExpression("[lrange [split [value [topnode].format]  ] 1 1 ]")
                calculator.addKnob(topH)

                bboxH = nuke.Double_Knob('bboxHeight', 'bboxHeight') 
                bboxH.setExpression("(-input.box.y)*2")
                calculator.addKnob(bboxH)

                scaleH = nuke.Double_Knob('scaleHeight', 'scaleHeight') 
                scaleH.setExpression("(topnodeHeight+bboxHeight)/topnodeHeight")
                calculator.addKnob(scaleH)
                calculator.setSelected(False)

                # set position for LD nodes
                ldNode2['xpos'].setValue(int(dot1['xpos'].value()-n.screenWidth()/2))
                ldNode2['ypos'].setValue(int(CropMain['ypos'].value())+250)

                # create dotSL
                dotSL = nuke.nodes.Dot()
                dotSL['xpos'].setValue(int(dot1['xpos'].value())-250)
                dotSL['ypos'].setValue(int(dot1['ypos'].value()))
                dotSL.setSelected(False)

                # create STDist
                STDist = nuke.nodes.STMap()
                STDist['xpos'].setValue(int(dotSL['xpos'].value())-STDist.screenWidth()/2)
                STDist['ypos'].setValue(int(dot1['ypos'].value())+250)
                STDist['uv'].setValue('rgb')
                STDist.setSelected(False)

                # create Transf
                Transf = nuke.nodes.Transform()
                Transf['xpos'].setValue(int(STDist['xpos'].value()))
                Transf['ypos'].setValue(int(STDist['ypos'].value())+150)
                Transf['center'].setExpression("input.width/2", 0)
                Transf['center'].setExpression("input.height/2", 1)
                Transf['scale'].setExpression(calculator.name() + ".scaleWidth")
                Transf.setSelected(False)

                # create STunDist
                STunDist = nuke.nodes.STMap()
                STunDist['xpos'].setValue(int(Transf['xpos'].value()))
                STunDist['ypos'].setValue(int(Transf['ypos'].value())+100)
                STunDist['uv'].setValue('rgb')
                STunDist.setSelected(False)

                # Connect inputs
                dot1.setInput(0,n)
                ldNode.setInput(0,dot1)
                CropMain.setInput(0,ldNode)
                calculator.setInput(0,CropMain)
                ldNode2.setInput(0,calculator)
                dotSL.setInput(0,dot1)
                STDist.setInput(0,dotSL)
                STDist.setInput(1,CropMain)
                Transf.setInput(0,STDist)
                STunDist.setInput(0,Transf)
                STunDist.setInput(1,ldNode2)
            else:
                nuke.message("<center><font color=orange>The folder wasn't created yet to open\nor has no Lens node!")
    else:
        nuke.message("<center><font color=orange>Select some Read nodes first!")

loadLens()

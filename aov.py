##############################
### AOV BEAUTY config test ###
##############################


lightList = nuke.toNode('AOV_Beauty1')['lightList'].value().split(",")

print (lightList)

node = nuke.createNode('NoOp')


for i in lightList:

    #create section name 
    knob = nuke.Text_Knob('tmp')
    knob.setName(i)
    knob.setLabel(' ')
    knob.setValue(i)
    node.addKnob(knob)

    # create exposure
    knobExpo = nuke.Color_Knob('tmp')
    knobExpo.setName(i+'_exposure')
    knobExpo.setLabel('exposure')
    node.addKnob(knobExpo)
    
    # create begin/endGroup
    #knobGroupBegin = nuke.BeginTabGroup_Knob()
    #knobGroupEnd = nuke.EndTabGroup_Knob()
    #node.addKnob(knobGroupBegin)
    
    #knobGroupBegin.setName(i+'_grade_Group')
    #knobGroupBegin.setLabel('grade')

    knob1 = nuke.Tab_Knob(i+'_tab', 'grade', nuke.TABBEGINCLOSEDGROUP)
    node.addKnob(knob1)

    # create multiply
    knobMult = nuke.Color_Knob('tmp')
    knobMult.setName(i+'_multiply')
    knobMult.setLabel('multiply')
    node.addKnob(knobMult)
    knobMult.setRange(0, 4)
    knobMult.setValue(1, 0)
    knobMult.setValue(1, 1)
    knobMult.setValue(1, 2)

    # create add
    knobAdd = nuke.Color_Knob('tmp')
    knobAdd.setName(i+'_add')
    knobAdd.setLabel('add')
    node.addKnob(knobAdd)
    knobAdd.setRange(-1, 1)

    # create gamma
    knobGamma = nuke.Color_Knob('tmp')
    knobGamma.setName(i+'_gamma')
    knobGamma.setLabel('gamma')
    node.addKnob(knobGamma)
    knobGamma.setRange(0.2, 5)
    knobGamma.setValue(1)

    # create saturation
    knobSat = nuke.Color_Knob('tmp')
    knobSat.setName(i+'_saturation')
    knobSat.setLabel('saturation')
    node.addKnob(knobSat)
    knobSat.setRange(0, 4)
    knobSat.setValue(1)



    # adding endGroup
    #knobGroupEnd = nuke.EndTabGroup_Knob()
    #node.addKnob(knobGroupEnd)

    end = nuke.Tab_Knob('', None, nuke.TABENDGROUP)
    node.addKnob(end)

    #begin = nuke.Tab_Knob('begin', 'My Group :', -1)


    # create disable cc
    knobDisCC = nuke.Boolean_Knob('tmp')
    knobDisCC.setName(i+'_isCcDisabled')
    knobDisCC.setLabel('disable cc')
    node.addKnob(knobDisCC)

    # create solo
    knobSolo = nuke.Boolean_Knob('tmp')
    knobSolo.setName(i+'_isSolo')
    knobSolo.setLabel('solo')
    node.addKnob(knobSolo)

    # create mute
    knobMute = nuke.Boolean_Knob('tmp')
    knobMute.setName(i+'_isMute')
    knobMute.setLabel('mute')
    node.addKnob(knobMute)

    #create dividing line
    knobLine = nuke.Text_Knob('tmp')
    knobLine.setName('')
    knobLine.setLabel('')
    node.addKnob(knobLine)


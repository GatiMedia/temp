##############################
### AOV BEAUTY config test ###
##############################

node = nuke.createNode('NoOp')

thisNode = nuke.toNode('AOV_Beauty1')

def addknobs():
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
   
    # create Group Begin
    knobGroupBegin = nuke.Tab_Knob(i+'_tab', 'grade', nuke.TABBEGINCLOSEDGROUP)
    node.addKnob(knobGroupBegin)

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

    # create Group End
    knobGroupEnd = nuke.Tab_Knob('', None, nuke.TABENDGROUP)
    node.addKnob(knobGroupEnd)

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


# create AOV_Beauty Tab
knob = nuke.Tab_Knob('shaderList', 'AOV_Beauty')
node.addKnob(knob)

for i in thisNode['shaderList'].value().split(","):
    addknobs()


# create lights Tab
knob = nuke.Tab_Knob('lightList', 'lights')
node.addKnob(knob)

for i in thisNode['lightList'].value().split(","):
    addknobs()


# create AOVs Tab
knob = nuke.Tab_Knob('aovList', 'AOVs')
node.addKnob(knob)

# create Group Begin EXTRAS
knobGroupBegin = nuke.Tab_Knob('groupStart', 'EXTRAS', nuke.TABBEGINCLOSEDGROUP)
node.addKnob(knobGroupBegin)

knob = nuke.Text_Knob('basecolor_txt', '• <b>basecolor</b>', " ")
node.addKnob(knob)

for i in thisNode['basecolourName'].value().split(","):
    addknobs()


knob = nuke.Text_Knob('leftovers_txt', '• <b>leftovers</b>', " ")
node.addKnob(knob)

for i in thisNode['leftoversName'].value().split(","):
    addknobs()


# create Group End EXTRAS
knobGroupEnd = nuke.Tab_Knob('', None, nuke.TABENDGROUP)
node.addKnob(knobGroupEnd)

#create dividing line after EXTRAS
knobLine = nuke.Text_Knob('tmp')
knobLine.setName('')
knobLine.setLabel('')
node.addKnob(knobLine)

for i in thisNode['aovList'].value().split(","):

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
   
    # create Group Begin
    knobGroupBegin = nuke.Tab_Knob(i+'_tab', 'grade', nuke.TABBEGINCLOSEDGROUP)
    node.addKnob(knobGroupBegin)

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

    # create Group End
    knobGroupEnd = nuke.Tab_Knob('', None, nuke.TABENDGROUP)
    node.addKnob(knobGroupEnd)

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

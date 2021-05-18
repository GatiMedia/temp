##############################
### AOV BEAUTY config test ###
##############################

node = nuke.thisNode()

lightList = node['lightList'].value().split(",")
channels = node.channels()
layers = node['aovList'].value().split(",")

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
    knobLine = nuke.Text_Knob('', '')
    node.addKnob(knobLine)


### CREATE AOV_Beauty TAB ###
knob = nuke.Tab_Knob('shaderList', 'AOV_Beauty')
node.addKnob(knob)

for i in node['shaderList'].value().split(","):
    addknobs()


### CREATE lights TAB ###
knob = nuke.Tab_Knob('lightList', 'lights')
node.addKnob(knob)

for i in lightList:
    addknobs()


### CREATE AOVs TAB ###
knob = nuke.Tab_Knob('aovList', 'AOVs')
node.addKnob(knob)

# create Group Begin EXTRAS
knobGroupBegin = nuke.Tab_Knob('groupStart', 'EXTRAS', nuke.TABBEGINCLOSEDGROUP)
node.addKnob(knobGroupBegin)

knob = nuke.Text_Knob('basecolor_txt', '• <b>basecolor</b>', " ")
node.addKnob(knob)

for i in node['basecolourName'].value().split(","):
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
    knobSolo.setFlag(nuke.INVISIBLE)

    # create mute
    knobMute = nuke.Boolean_Knob('tmp')
    knobMute.setName(i+'_isMute')
    knobMute.setLabel('mute')
    node.addKnob(knobMute)
    knobMute.setFlag(nuke.INVISIBLE)

    # create anyGrade
    knobanyGrade = nuke.Boolean_Knob('tmp')
    knobanyGrade.setName(i+'_isAnyGrade')
    knobanyGrade.setLabel('anyGrade')
    node.addKnob(knobanyGrade)
    knobanyGrade.setFlag(nuke.INVISIBLE)

    # create anyMute
    knobanyMute = nuke.Boolean_Knob('tmp')
    knobanyMute.setName(i+'_isAnyMute')
    knobanyMute.setLabel('anyMute')
    node.addKnob(knobanyMute)
    knobanyMute.setFlag(nuke.INVISIBLE)

    #create dividing line
    knobLine = nuke.Text_Knob('', '')
    node.addKnob(knobLine)


knob = nuke.Text_Knob('leftovers_txt', '• <b>leftovers</b>', " ")
node.addKnob(knob)

for i in node['leftoversName'].value().split(","):
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

    # create useLeftovers
    knobuseLeftovers = nuke.Boolean_Knob('tmp')
    knobuseLeftovers.setName(i+'_useLeftovers')
    knobuseLeftovers.setLabel('useLeftovers')
    node.addKnob(knobuseLeftovers)

    # create anyGrade
    knobanyGrade = nuke.Boolean_Knob('tmp')
    knobanyGrade.setName(i+'_isAnyGrade')
    knobanyGrade.setLabel('anyGrade')
    node.addKnob(knobanyGrade)
    knobanyGrade.setFlag(nuke.INVISIBLE)

    # create anyMute
    knobanyMute = nuke.Boolean_Knob('tmp')
    knobanyMute.setName(i+'_isAnyMute')
    knobanyMute.setLabel('anyMute')
    node.addKnob(knobanyMute)
    knobanyMute.setFlag(nuke.INVISIBLE)

    #create dividing line
    knobLine = nuke.Text_Knob('', '')
    node.addKnob(knobLine)


# create Group End EXTRAS
knobGroupEnd = nuke.Tab_Knob('', None, nuke.TABENDGROUP)
node.addKnob(knobGroupEnd)

#create dividing line after EXTRAS
knobLine = nuke.Text_Knob('', '')
node.addKnob(knobLine)

for i in lightList:
    # create Group Begin
    knobGroupBegin = nuke.Tab_Knob(i+'_group', i+'_GROUP', nuke.TABBEGINCLOSEDGROUP)
    node.addKnob(knobGroupBegin)

    matching = [s for s in layers if i in s]

    for t in matching:
        #create section name
        knob = nuke.Text_Knob(t+'_txt', '• <b>'+t+'</b>', " ")
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

        # create anyGrade
        knobanyGrade = nuke.Boolean_Knob('tmp')
        knobanyGrade.setName(i+'_isAnyGrade')
        knobanyGrade.setLabel('anyGrade')
        node.addKnob(knobanyGrade)
        knobanyGrade.setFlag(nuke.INVISIBLE)

        # create anyMute
        knobanyMute = nuke.Boolean_Knob('tmp')
        knobanyMute.setName(i+'_isAnyMute')
        knobanyMute.setLabel('anyMute')
        node.addKnob(knobanyMute)
        knobanyMute.setFlag(nuke.INVISIBLE)

        #create dividing line
        knobLine = nuke.Text_Knob('', '')
        node.addKnob(knobLine)

    # create Group End
    knobGroupEnd = nuke.Tab_Knob('', None, nuke.TABENDGROUP)
    node.addKnob(knobGroupEnd)

    #create dividing line
    knobLine = nuke.Text_Knob('', '')
    node.addKnob(knobLine)

### CREATE config TAB ###
knob = nuke.Tab_Knob('config', 'config')
node.addKnob(knob)

# create txt
knobTxt = nuke.Text_Knob('txt', '', 'Nothing to play with here. Best not to touch.')
node.addKnob(knobTxt)

# create dividing line
knobLine = nuke.Text_Knob('', '')
node.addKnob(knobLine)

# create shaderList stringKnob
knobshaderList = nuke.String_Knob('_shaderList', 'shaderList')
knobshaderList.setValue(str(node['shaderList'].value()))
node.addKnob(knobshaderList)

# create lightList stringKnob
knoblightList = nuke.String_Knob('_lightList', 'lightList')
knoblightList.setValue(str(node['lightList'].value())) 
node.addKnob(knoblightList)

# create aovList stringKnob
knobaovList = nuke.String_Knob('_aovList', 'aovList')
knobaovList.setValue(str(node['aovList'].value())) 
node.addKnob(knobaovList)

# create basecolourName stringKnob
knobbasecolourName = nuke.String_Knob('_basecolourName', 'basecolourName')
knobbasecolourName.setValue(str(node['basecolourName'].value())) 
node.addKnob(knobbasecolourName)

# create leftoversName stringKnob
knobleftoversName = nuke.String_Knob('_leftoversName', 'leftoversName')
knobleftoversName.setValue(str(node['leftoversName'].value()))
node.addKnob(knobleftoversName)

# create none_isAnyGrade
knobnone_isAnyGrade = nuke.Boolean_Knob('none_isAnyGrade', 'none_isAnyGrade')
node.addKnob(knobnone_isAnyGrade)
knobnone_isAnyGrade.setFlag(nuke.INVISIBLE)

# create none_isSolo
knobnone_isSolo = nuke.Boolean_Knob('none_isSolo', 'none_isSolo')
node.addKnob(knobnone_isSolo)
knobnone_isSolo.setFlag(nuke.INVISIBLE)

# create none_isMute
knobnone_isMute = nuke.Boolean_Knob('none_isMute', 'none_isMute')
node.addKnob(knobnone_isMute)
knobnone_isMute.setFlag(nuke.INVISIBLE)

# create none_isAnyMute
knobnone_isAnyMute = nuke.Boolean_Knob('none_isAnyMute', 'none_isAnyMute')
node.addKnob(knobnone_isAnyMute)
knobnone_isAnyMute.setFlag(nuke.INVISIBLE)

# create none_isCcDisabled
knobnone_isCcDisabled = nuke.Boolean_Knob('none_isCcDisabled', 'none_isCcDisabled')
node.addKnob(knobnone_isCcDisabled)
knobnone_isCcDisabled.setFlag(nuke.INVISIBLE)

### CREATE Info TAB ###
knob = nuke.Tab_Knob('Info', 'Info')
node.addKnob(knob)

# create version txt
knobVersion = nuke.Text_Knob('_version', 'Version', node['version'].value())
node.addKnob(knobVersion)

# create dividing line
knobLine = nuke.Text_Knob('', '')
node.addKnob(knobLine)

# create todo txt
knobVersion = nuke.Text_Knob('_todo', 'todo', node['todo'].value())
node.addKnob(knobVersion)

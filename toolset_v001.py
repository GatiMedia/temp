# --------------------------------------------------------------
#  GBK MENU ::::::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

#### Main Menu ####

xN = None

gbkMenu = nuke.menu('Nodes').addMenu('gbk_menu', icon="test_010.png")

gbkMeShow = gbkMenu.addMenu('Show', icon="test_017.png")
gbkMeNode = gbkMenu.addMenu('Nodes', icon="test_018.png")
gbkMeTemp = gbkMenu.addMenu('Templates', icon="test_016.png")
gbkMePy = gbkMenu.addMenu('Python', icon="test_014.png")
gbkMe3rd = gbkMenu.addMenu('3rdParty', icon="test_009.png")


### Show Menu ###

ShowPath = '/mnt/home/attila.gasparetz/AttilaG/GBKtoolbar_test/Shows'

shows = []

showPathes = []

# r=root, d=directories, f = files

for r, d, f in os.walk(ShowPath):
    for folder in d:
        shows.append(folder)
        showNum = (len(shows))

    for name in d:
        showPathes.append(os.path.join(r, name + "/"))

for i in showPathes:
    for ro, di, fi in os.walk(i):
        showMenu = gbkMeShow.addMenu(ro.split("/")[-2], icon="test_022.png")
        for Showgizmo in fi:
            menuEntry = Showgizmo.replace(".gizmo", "")
            showMenu.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="")


### Node Menu ###

gbkImage = gbkMeNode.addMenu('Image', icon="ToolbarImage.png")
gbkDraw = gbkMeNode.addMenu('Draw', icon="ToolbarDraw.png")
gbkTime = gbkMeNode.addMenu('Time', icon="ToolbarTime.png")
gbkChannel = gbkMeNode.addMenu('Channel', icon="ToolbarChannel.png")
gbkColor = gbkMeNode.addMenu('Color', icon="ToolbarColor.png")
gbkFilter = gbkMeNode.addMenu('Filter', icon="ToolbarFilter.png")
gbkKeyer = gbkMeNode.addMenu('Keyer', icon="ToolbarKeyer.png")
gbkTransform = gbkMeNode.addMenu('Transform', icon="ToolbarTransform.png")
gbk3D = gbkMeNode.addMenu('3D', icon="Toolbar3D.png")
gbkParticles = gbkMeNode.addMenu('Particles', icon="ToolbarParticles.png")
gbkDeep = gbkMeNode.addMenu('Deep', icon="ToolbarDeep.png")
gbkMetadata = gbkMeNode.addMenu('Metadata', icon="MetaData.png")
gbkOther = gbkMeNode.addMenu('Other', icon="ToolbarOther.png")

### SubMenus for Node ###

NodePath = '/mnt/home/attila.gasparetz/AttilaG/GBKtoolbar_test/Node/'

## Node / Image ##

pathImage = NodePath+'Image'

files = os.listdir(pathImage)
Imagegizmos = []
for f in files:
    Imagegizmos.append(f)

for g in sorted(Imagegizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkImage.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="ToolbarImage.png")

## Node / Draw ##

pathDraw = NodePath+'Draw'

files = os.listdir(pathDraw)
Drawgizmos = []
for f in files:
    Drawgizmos.append(f)

for g in sorted(Drawgizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkDraw.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="ToolbarDraw.png")

## Node / Channel ##

pathChannel = NodePath+'Channel'

files = os.listdir(pathChannel)
Channelgizmos = []
for f in files:
    Channelgizmos.append(f)

for g in sorted(Channelgizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkChannel.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="ToolbarChannel.png")

## Node / Color ##

pathColor = NodePath+'Color'

files = os.listdir(pathColor)
Colorgizmos = []
for f in files:
    Colorgizmos.append(f)

for g in sorted(Colorgizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkColor.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="ToolbarColor.png")

## Node / Filter ##

pathFilter = NodePath+'Filter'

files = os.listdir(pathFilter)
Filtergizmos = []
for f in files:
    Filtergizmos.append(f)

for g in sorted(Filtergizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkFilter.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="ToolbarFilter.png")

## Node / Keyer ##

pathKeyer = NodePath+'Keyer'

files = os.listdir(pathKeyer)
Keyergizmos = []
for f in files:
    Keyergizmos.append(f)

for g in sorted(Keyergizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkKeyer.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="ToolbarKeyer.png")

## Node / Transform ##

pathTransform = NodePath+'Transform'

files = os.listdir(pathTransform)
Transformgizmos = []
for f in files:
    Transformgizmos.append(f)

for g in sorted(Transformgizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkTransform.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="ToolbarTransform.png")

## Node / 3D ##

path3D = NodePath+'3D'

files = os.listdir(path3D)
ThreeDgizmos = []
for f in files:
    ThreeDgizmos.append(f)

for g in sorted(ThreeDgizmos):
    menuEntry = g.replace(".gizmo", "")
    gbk3D.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="Toolbar3D.png")

## Node / Particles ##

pathParticles = NodePath+'Particles'

files = os.listdir(pathParticles)
Particlesgizmos = []
for f in files:
    Particlesgizmos.append(f)

for g in sorted(Particlesgizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkParticles.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="ToolbarParticles.png")

## Node / Deep ##

pathDeep = NodePath+'Deep'

files = os.listdir(pathDeep)
Deepgizmos = []
for f in files:
    Deepgizmos.append(f)

for g in sorted(Deepgizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkDeep.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="ToolbarDeep.png")

## Node / MetaData ##

pathMetadata = NodePath+'Metadata'

files = os.listdir(pathMetadata)
Metadatagizmos = []
for f in files:
    Metadatagizmos.append(f)

for g in sorted(Metadatagizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkMetadata.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="MetaData.png")

## Node / Other ##

pathOther = NodePath+'Other'

files = os.listdir(pathOther)
Othergizmos = []
for f in files:
    Othergizmos.append(f)

for g in sorted(Othergizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkOther.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="ToolbarOther.png")


### Template Menu ###

tempImage = gbkMeTemp.addMenu('Image', icon="ToolbarImage.png")
tempDraw = gbkMeTemp.addMenu('Draw', icon="ToolbarDraw.png")
tempTime = gbkMeTemp.addMenu('Time', icon="ToolbarTime.png")
tempChannel = gbkMeTemp.addMenu('Channel', icon="ToolbarChannel.png")
tempColor = gbkMeTemp.addMenu('Color', icon="ToolbarColor.png")
tempFilter = gbkMeTemp.addMenu('Filter', icon="ToolbarFilter.png")
tempKeyer = gbkMeTemp.addMenu('Keyer', icon="ToolbarKeyer.png")
tempTransform = gbkMeTemp.addMenu('Transform', icon="ToolbarTransform.png")
temp3D = gbkMeTemp.addMenu('3D', icon="Toolbar3D.png")
tempParticles = gbkMeTemp.addMenu('Particles', icon="ToolbarParticles.png")
tempDeep = gbkMeTemp.addMenu('Deep', icon="ToolbarDeep.png")
tempMetadata = gbkMeTemp.addMenu('Metadata', icon="MetaData.png")
tempOther = gbkMeTemp.addMenu('Other', icon="ToolbarOther.png")


Templatepath = '/mnt/home/attila.gasparetz/AttilaG/GBKtoolbar_test/Templates/'

## Template / Image ##

template_folder = Templatepath + 'Image/*.nk'

templates = glob.glob(template_folder)

for template in sorted(templates):
    menu_name = format(os.path.basename(template).replace('.nk', ''))
    tempImage.addCommand(menu_name, 'nuke.nodePaste("{}")'.format(template), icon="test_019.png")

## Template / Draw ##

template_folder = Templatepath + 'Draw/*.nk'

templates = glob.glob(template_folder)

for template in sorted(templates):
    menu_name = format(os.path.basename(template).replace('.nk', ''))
    tempDraw.addCommand(menu_name, 'nuke.nodePaste("{}")'.format(template), icon="test_019.png")

## Template / Time ##

template_folder = Templatepath + 'Time/*.nk'

templates = glob.glob(template_folder)

for template in sorted(templates):
    menu_name = format(os.path.basename(template).replace('.nk', ''))
    tempTime.addCommand(menu_name, 'nuke.nodePaste("{}")'.format(template), icon="test_019.png")

## Template / Channel ##

template_folder = Templatepath + 'Channel/*.nk'

templates = glob.glob(template_folder)

for template in sorted(templates):
    menu_name = format(os.path.basename(template).replace('.nk', ''))
    tempChannel.addCommand(menu_name, 'nuke.nodePaste("{}")'.format(template), icon="test_019.png")

## Template / Color ##

template_folder = Templatepath + 'Color/*.nk'

templates = glob.glob(template_folder)

for template in sorted(templates):
    menu_name = format(os.path.basename(template).replace('.nk', ''))
    tempColor.addCommand(menu_name, 'nuke.nodePaste("{}")'.format(template), icon="test_019.png")

## Template / Filter ##

template_folder = Templatepath + 'Filter/*.nk'

templates = glob.glob(template_folder)

for template in sorted(templates):
    menu_name = format(os.path.basename(template).replace('.nk', ''))
    tempFilter.addCommand(menu_name, 'nuke.nodePaste("{}")'.format(template), icon="test_019.png")

## Template / Keyer ##

template_folder = Templatepath + 'Keyer/*.nk'

templates = glob.glob(template_folder)

for template in sorted(templates):
    menu_name = format(os.path.basename(template).replace('.nk', ''))
    tempKeyer.addCommand(menu_name, 'nuke.nodePaste("{}")'.format(template), icon="test_019.png")

## Template / Transform ##

template_folder = Templatepath + 'Transform/*.nk'

templates = glob.glob(template_folder)

for template in sorted(templates):
    menu_name = format(os.path.basename(template).replace('.nk', ''))
    tempTransform.addCommand(menu_name, 'nuke.nodePaste("{}")'.format(template), icon="test_019.png")

## Template / 3D ##

template_folder = Templatepath + '3D/*.nk'

templates = glob.glob(template_folder)

for template in sorted(templates):
    menu_name = format(os.path.basename(template).replace('.nk', ''))
    temp3D.addCommand(menu_name, 'nuke.nodePaste("{}")'.format(template), icon="test_019.png")

## Template / Particles ##

template_folder = Templatepath + 'Particles/*.nk'

templates = glob.glob(template_folder)

for template in sorted(templates):
    menu_name = format(os.path.basename(template).replace('.nk', ''))
    tempParticles.addCommand(menu_name, 'nuke.nodePaste("{}")'.format(template), icon="test_019.png")

## Template / Deep ##

template_folder = Templatepath + 'Deep/*.nk'

templates = glob.glob(template_folder)

for template in sorted(templates):
    menu_name = format(os.path.basename(template).replace('.nk', ''))
    tempDeep.addCommand(menu_name, 'nuke.nodePaste("{}")'.format(template), icon="test_019.png")

## Template / MetaData ##

template_folder = Templatepath + 'Metadata/*.nk'

templates = glob.glob(template_folder)

for template in sorted(templates):
    menu_name = format(os.path.basename(template).replace('.nk', ''))
    tempMetadata.addCommand(menu_name, 'nuke.nodePaste("{}")'.format(template), icon="test_019.png")

## Template / Other ##

template_folder = Templatepath + 'Other/*.nk'

templates = glob.glob(template_folder)

for template in sorted(templates):
    menu_name = format(os.path.basename(template).replace('.nk', ''))
    tempOther.addCommand(menu_name, 'nuke.nodePaste("{}")'.format(template), icon="test_019.png")



## Template / NKs in root folder ##

template_folder = Templatepath + '*.nk'

templates = glob.glob(template_folder)

for template in sorted(templates):
    menu_name = format(os.path.basename(template).replace('.nk', ''))
    gbkMeTemp.addCommand(menu_name, 'nuke.nodePaste("{}")'.format(template), icon="test_019.png")



### Python Menu ###

# gbkMePy.addCommand('PostageStampDis', 'xN', icon="ToolbarImage.png")

gbkMePy.addCommand('CloseWindows', 'close()' , icon="test_023.png")

gbkMePy.addCommand('Disconnect Viewers', 'disconnectViewers()' , icon="test_023.png")

gbkMePy.addCommand('Roto n Blur', 'RotoBlur_Shortcut()' , icon="test_023.png")

### 3rdParty Menu ###

Plugins = ['3DE4', 'RandomTiles','VideoCopilot','Mocha','HigX Tools','Cryptomatte','KeenTools','Peregrine','Projectionist','Pixelfudger']

for plugin in sorted(Plugins):
    gbkMe3rd.addCommand(plugin, 'xN', icon="Plugin.png")

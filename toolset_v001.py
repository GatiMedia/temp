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
        showMenu = gbkMeShow.addMenu(ro.split("/")[-2], icon="Camera.png")
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

gbkMeTemp.addCommand('GrainSetup', 'xN', icon="Plugin.png")

# TODO add .nk-s to Template as .gizmo-s in SHowMenu
# script = '/mnt/home/attila.gasparetz/AttilaG/GBKtoolbar_test/Templates/Blur_and_Grade_v001.nk'
#
## loads script in current script
# nuke.nodePaste(script)
#
## opens script in new window
# nuke.scriptOpen(script)

### Python Menu ###

gbkMePy.addCommand('PostageStampDis', 'xN', icon="ToolbarImage.png")

### 3rdParty Menu ###

gbkMe3rd.addCommand('pgBokeh', 'xN', icon="Image.png")

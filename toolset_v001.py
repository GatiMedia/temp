# --------------------------------------------------------------
#  GBK MENU ::::::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

xN = None

gbkMenu = nuke.menu('Nodes').addMenu('gbk_menu', icon="test_010.png")

gbkMeShow = gbkMenu.addMenu('Show', icon="test_017.png")
gbkMeNode = gbkMenu.addMenu('Nodes', icon="test_018.png")
gbkMeTemp = gbkMenu.addMenu('Templates', icon="test_016.png")
gbkMePy = gbkMenu.addMenu('Python', icon="test_014.png")
gbkMe3rd = gbkMenu.addMenu('3rdParty', icon="test_009.png")


## SubMenus Level 1 ##

## Show Menu ##

# currentShows = ['355' , 'Irr1' , 'BHE1' ]
#
# showNodes_355 = ['355_1' , '355_2' , '355_3' ]
# showNodes_Irr1 = ['Irr1_1' , 'Irr1_2' , 'Irr1_3' ]
# showNodes_BHE1 = ['BHE1_1' , 'BHE1_2' , 'BHE1_3' ]


path = '/mnt/home/attila.gasparetz/AttilaG/GBKtoolbar_test/Shows'

shows = []

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for folder in d:
        shows.append(folder)

    for show in shows:
        showMenu = gbkMeShow.addCommand(show, 'xN', icon="Camera.png")

    # for name in d:
    #     showPath.append(os.path.join(r, name + "/"))
    #
    # for gizmoPath in showPath:
    #         if files = os.listdir(gizmoPath):
    #             for g in sorted(files):
    #                 menuEntry = g.replace(".gizmo", "")
    #                 showMenu.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="")
    #         else:
    #             pass


# showMenu355 = gbkMeShow.addMenu('355', icon="Camera.png")
# showMenuIrr1 = gbkMeShow.addMenu('Irr1', icon="Camera.png")
# showMenuBHE1 = gbkMeShow.addMenu('BHE1', icon="Camera.png")
#
# for n in showNodes_355:
#     showMenu355.addCommand(n, 'xN', icon="")
#
# for n in showNodes_Irr1:
#     showMenuIrr1.addCommand(n, 'xN', icon="")
#
# for n in showNodes_BHE1:
#     showMenuBHE1.addCommand(n, 'xN', icon="")

## Node Menu ##

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

## Template Menu ##

gbkMeTemp.addCommand('GrainSetup', 'xN', icon="Plugin.png")

## Python Menu ##

gbkMePy.addCommand('PostageStampDis', 'xN', icon="ToolbarImage.png")

## 3rdParty Menu ##

gbkMe3rd.addCommand('pgBokeh', 'xN', icon="Image.png")



## SubMenus for Node ##

NodePath = '/mnt/home/attila.gasparetz/AttilaG/GBKtoolbar_test/Node/'

#image

# imageNodes = ['Node1' , 'Node2' , 'Node3' ]
#
# for i in imageNodes:
#     gbkImage.addCommand(i, 'xN', icon="")


pathImage = NodePath+'Image'

files = os.listdir(pathImage)
Imagegizmos = []
for f in files:
    Imagegizmos.append(f)

for g in sorted(Imagegizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkImage.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="ToolbarImage.png")

#draw

# drawNodes = ['Node1' , 'Node2' , 'Node3' ]
#
# for i in drawNodes:
#     gbkDraw.addCommand(i, 'xN', icon="")

pathDraw = NodePath+'Draw'

files = os.listdir(pathDraw)
Drawgizmos = []
for f in files:
    Drawgizmos.append(f)

for g in sorted(Drawgizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkDraw.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="ToolbarDraw.png")

#channel

# channelNodes = ['Node1' , 'Node2' , 'Node3' ]
#
# for i in channelNodes:
#     gbkChannel.addCommand(i, 'xN', icon="")

pathChannel = NodePath+'Channel'

files = os.listdir(pathChannel)
Channelgizmos = []
for f in files:
    Channelgizmos.append(f)

for g in sorted(Channelgizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkChannel.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="ToolbarChannel.png")

#color

# colorNodes = ['Node1' , 'Node2' , 'Node3' ]
#
# for i in colorNodes:
#     gbkColor.addCommand(i, 'xN', icon="")

pathColor = NodePath+'Color'

files = os.listdir(pathColor)
Colorgizmos = []
for f in files:
    Colorgizmos.append(f)

for g in sorted(Colorgizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkColor.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="ToolbarColor.png")

#filter

# filterNodes = ['Node1' , 'Node2' , 'Node3' ]
#
# for i in filterNodes:
#     gbkFilter.addCommand(i, 'xN', icon="")

pathFilter = NodePath+'Filter'

files = os.listdir(pathFilter)
Filtergizmos = []
for f in files:
    Filtergizmos.append(f)

for g in sorted(Filtergizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkFilter.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="ToolbarFilter.png")

#keyer

# keyerNodes = ['Node1' , 'Node2' , 'Node3' ]
#
# for i in keyerNodes:
#     gbkKeyer.addCommand(i, 'xN', icon="")

pathKeyer = NodePath+'Keyer'

files = os.listdir(pathKeyer)
Keyergizmos = []
for f in files:
    Keyergizmos.append(f)

for g in sorted(Keyergizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkKeyer.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="ToolbarKeyer.png")

#transform

# transformNodes = ['Node1' , 'Node2' , 'Node3' ]
#
# for i in transformNodes:
#     gbkTransform.addCommand(i, 'xN', icon="")

pathTransform = NodePath+'Transform'

files = os.listdir(pathTransform)
Transformgizmos = []
for f in files:
    Transformgizmos.append(f)

for g in sorted(Transformgizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkTransform.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="ToolbarTransform.png")

#3D

# threeDNodes = ['Node1' , 'Node2' , 'Node3' ]
#
# for i in threeDNodes:
#     gbk3D.addCommand(i, 'xN', icon="")


path3D = NodePath+'3D'

files = os.listdir(path3D)
ThreeDgizmos = []
for f in files:
    ThreeDgizmos.append(f)

for g in sorted(ThreeDgizmos):
    menuEntry = g.replace(".gizmo", "")
    gbk3D.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="Toolbar3D.png")

#particles

# particlesNodes = ['Node1' , 'Node2' , 'Node3' ]
#
# for i in particlesNodes:
#     gbkParticles.addCommand(i, 'xN', icon="")

pathParticles = NodePath+'Particles'

files = os.listdir(pathParticles)
Particlesgizmos = []
for f in files:
    Particlesgizmos.append(f)

for g in sorted(Particlesgizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkParticles.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="ToolbarParticles.png")

#deep

# deepNodes = ['Node1' , 'Node2' , 'Node3' ]
#
# for i in deepNodes:
#     gbkDeep.addCommand(i, 'xN', icon="")

pathDeep = NodePath+'Deep'

files = os.listdir(pathDeep)
Deepgizmos = []
for f in files:
    Deepgizmos.append(f)

for g in sorted(Deepgizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkDeep.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="ToolbarDeep.png")

#metadata

# metadataNodes = ['Node1' , 'Node2' , 'Node3' ]
#
# for i in metadataNodes:
#     gbkMetadata.addCommand(i, 'xN', icon="")

pathMetadata = NodePath+'Metadata'

files = os.listdir(pathMetadata)
Metadatagizmos = []
for f in files:
    Metadatagizmos.append(f)

for g in sorted(Metadatagizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkMetadata.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="MetaData.png")

#other

# otherNodes = ['Node1' , 'Node2' , 'Node3' ]
#
# for i in otherNodes:
#     gbkOther.addCommand(i, 'xN', icon="")

pathOther = NodePath+'Other'

files = os.listdir(pathOther)
Othergizmos = []
for f in files:
    Othergizmos.append(f)

for g in sorted(Othergizmos):
    menuEntry = g.replace(".gizmo", "")
    gbkOther.addCommand(menuEntry, "nuke.createNode('" + menuEntry + "')", icon="ToolbarOther.png")

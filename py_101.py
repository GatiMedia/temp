### Python snippets 101 GBK ###


### First step ###


print "Hello World!"


### Using variable ###


name = 'Mara'
hy = 'Hello '
print hy + name + '!'


### Create a Node ###


nuke.createNode("Blur")

nuke.createNode("Tracker4")

nuke.createNode("Blocky")


nuke.createNode("Blur")['size'].setValue(80)


m = nuke.createNode("Blur")
m['channels'].setValue("rgb")
m['size'].setValue(50)


nuke.nodes.Blur()


nuke.nodes.Blur(mix=.5,size=10)


### Asking knob value with .value() and .getValue() ###


nuke.toNode('Blur1')["channels"].value()

nuke.toNode('Blur1').knob("channels").value()

nuke.toNode('Blur1')["filter"].getValue()


### Setting knob value ###


nuke.toNode('Blur1')["size"].setValue(3)


### Setting expression as a value ###

nuke.toNode('Blur1')["size"].setExpression('Blur2.size * 2')

nuke.toNode('Transform1')["filter"].setExpression("Transform2.filter")


### Remove animation / expression ###


nuke.toNode('Transform1')["filter"].clearAnimated()


### Create multiple nodes with for loop and range ###


for i in range(15):
    i = nuke.createNode("Blur")
    i["channels"].setValue('rgb')
    i["size"].setExpression('Blur1.size')


### Formatting values ###


# Interger - int(x)

x = 12.8
print type(x)
x = int(x)
print type(x)
print x

# Float - float(x)

x = 12
print type(x)
x = float(x)
print type(x)
print x

# String - str(x)

x = 12.5
print type(x)
x = str(x)
print type(x)
print x


### Run on any selected nodes ###


nodes = nuke.selectedNodes()
for node in nodes:
    try:
        node.knob("size").setValue(5)
    except Exception:
        pass


### Run on all nodes in a script ###


nodes = nuke.allNodes()
for node in nodes:
    try:
        node.knob("size").setValue(20)
    except Exception:
        pass


### Run an all specified Classes ###


nodes = nuke.allNodes('Merge2')
for node in nodes:
    node.knob("mix").setValue(.5)


### Run an selected specified Classes ###


nodes = nuke.selectedNodes('Merge2')
for node in nodes:
    try:
        node.knob("mix").setValue(.8)
    except Exception:
        pass


### Run on all multiple Classes ###


nodes_classes = ["Read", "PostageStamp", "Constant", "ColorBars", "CheckerBoard2", "ColorWheel"]

for node in nuke.allNodes(group=nuke.root()):
    if node.Class() in nodes_classes:
        try:
            node["postage_stamp"].setValue(True)
        except Exception:
            pass


### Run on selected multiple Classes ###


nuke.root().begin()

nodes_classes = ["Read", "PostageStamp", "Constant", "ColorBars", "CheckerBoard2", "ColorWheel"]

for node in nuke.selectedNodes():
    if node.Class() in nodes_classes:
        try:
            node["postage_stamp"].setValue(True)
        except Exception:
            pass
nuke.root().end()


### Path for your nuke folder ###


nuke.pluginPath()


# For checkboxes value can be True or False equals to 1 or 0

# For dropdown menu values can be the name of the option or number of the option starting with 0 from the top

# To find the Class of the node select it and press `i` over the NodeGraph

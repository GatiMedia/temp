# The power of Iteration #
## ( for loop ) ##


# Practice Snippets #


# Setting up size for all Blur nodes
for node in nuke.allNodes('Blur'):
    node['size'].setValue(5)


# Printing all node's name
for node in nuke.allNodes():
    print (node['name'].value())


# Setting up selected node's size value ( with/without try )

for node in nuke.selectedNodes():
    node['size'].setValue(50)
    node['channels'].setValue('rgba')


###

for node in nuke.selectedNodes():
    try:
        node['size'].setValue(10)
        node['channels'].setValue('rgb')
    except:
        pass


# Check specific Read node's colrospace
print (nuke.toNode('Read16')['colorspace'].value())


for node in nuke.selectedNodes():
    try:
        node['colorspace'].setValue('ACES - ACES2065-1')
    except Exception:
        pass


for node in nuke.selectedNodes():
    try:
        retime = nuke.createNode('Retime')
        retime['output.first_lock'].setValue(1)
        retime['output.first'].setValue(1001)
        retime['xpos'].setValue(node['xpos'].value())
        retime['ypos'].setValue(node['ypos'].value() + 100)
        retime.setInput(0, node)
    except:
        pass


for node in nuke.selectedNodes():
    try:
        dot = nuke.nodes.Dot()
        dot['xpos'].setValue(node['xpos'].value() + 35)
        dot['ypos'].setValue(node['ypos'].value() + 100)
        dot.setInput(0, node)
    except:
        pass


# Printing Range

for i in range(10):
    print (i)

# Printing Range with start/end
    
for i in range(5,10):
    print (i)

# Printing Range with start/end/step 
   
for i in range(1, 10, 2):
    print (i)

# Printing Range backward
    
for i in range(10,5,-1):
    print (i)



Py functions needed:
allNodes()
selectedNodes() / selectedNode()
toNode()
knob()
value() / getValue()
setValue()
setExpression()
setInput()


# Getting knob’s value #

# Get knob’s value with getValue()

print (nuke.toNode('Blur12')['filter'].getValue())

# Get knob’s value with value()

print (nuke.toNode('Blur12')['filter'].value())

# Get knob’s expression value with toScript()

print (nuke.toNode('Blur12')['size'].toScript())


# Practice Snippets #


# Setting a value on selected nodes

nodes = nuke.selectedNodes()
for node in nodes:
    try:
        node.knob("size").setValue(5) 
    except:
        pass

# Setting a value on all nodes in a specific Class

nodes = nuke.allNodes(“Merge2”)
for node in nodes:
    try:
        node.knob("mix").setValue(.5)
    except:
        pass

# Setting multiple values on all nodes in a specific Class

nodes = nuke.selectedNodes('Blur')
for node in nodes:
    try:
        node['size'].setExpression('t/80')
        node['channels'].setValue('rgb')
        node['label'].setValue('Just Adjusted')
    except:
        pass


# Connecting selected nodes to a specified node

t = nuke.toNode('Transform1')
nodes = nuke.selectedNodes()
for i in nodes:
    i.setInput(0, t)


# Connecting selected nodes to a specified node without variables

for i in nuke.selectedNodes():
    i.setInput(0, nuke.toNode('Transform1'))


# Extra Material #

https://www.w3schools.com/python/python_for_loops.asp

https://www.learnpython.org/en/Loops

https://pynative.com/python-range-function/

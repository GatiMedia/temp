The power of Iteration
( for loop )


Py functions needed:
allNodes()
selectedNodes() / selectedNode()
toNode()
knob()
value() / getValue()
setValue()
setExpression()
setInput()

Getting knob’s value:

# Get knob’s value with getValue()

print (nuke.toNode('Blur12')['filter'].getValue())

# Get knob’s value with value()

print (nuke.toNode('Blur12')['filter'].value())

# Get knob’s expression value with toScript()

print (nuke.toNode('Blur12')[‘size’].toScript())


Practice Snippets:


# Setting a value on selected nodes

nodes = nuke.selectedNodes()
for node in nodes:
    try:
        node.knob("size").setValue(5) 
    except Exception:
        pass

# Setting a value on all nodes in a specific Class

nodes = nuke.allNodes(“Merge2”)
for node in nodes:
    try:
        node.knob("mix").setValue(.5)
    except Exception:
        pass

# Setting multiple values on all nodes in a specific Class

nodes = nuke.selectedNodes('Blur')
for node in nodes:
    try:
        node['size'].setExpression('t/80')
        node['channels'].setValue('rgb')
        node['label'].setValue('Just Adjusted')
    except Exception:
        pass


# Connecting selected nodes to a specified node

t = nuke.toNode('Transform1')
nodes = nuke.selectedNodes()
for i in nodes:
    i.setInput(0, t)
    i.setInput(1, None)


Material:

https://www.w3schools.com/python/python_for_loops.asp

https://www.learnpython.org/en/Loops

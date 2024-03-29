#### WIP gizmo QC functions ####

# GOAL: Build a set of functions that checks/fixes common Gizmo mistakes that artists would check before adding new tools to the global toolset.
# Inspiration: https://benmcewan.com/blog/2019/10/21/back-to-basics-common-errors-when-creating-a-gizmo/ 

# Check if node a Gizmo 
# TODO need to check if Group too

def isGizmo(node):
    gizmo = isinstance(node, nuke.Gizmo)
    if gizmo:
        gizmo = 'Ouch! This node IS a Gizmo!'
    else:
        gizmo = 'Great! This node is NOT a Gizmo'
    return gizmo

print (isGizmo(nuke.selectedNode()))


# Check if node has Viewer inside
def isViewerInside(node):
    viewerList = []
    with node:
        nodes = nuke.allNodes(recurseGroups=True)
        for n in nodes:
            if n.Class() == 'Viewer':
                viewerList.append(n.name())
    if not viewerList:
        viewerList = 'Great! No Viewer node inside'
    else:
        viewerList = 'There are Viewer node(s) inside:\n' + ', '.join(viewerList)
    return (viewerList)

print(isViewerInside(nuke.selectedNode()))


# Check if node has blink script inside
def isBlinkInside(node):
    blinkList = []
    with node:
        nodes = nuke.allNodes(recurseGroups=True)
        for n in nodes:
            if n.Class() == 'BlinkScript' or n.Class() == 'ParticleBlinkScript':
                blinkList.append(n.name())
    if not blinkList:
        blinkList = 'No Blink node inside'
    else:
        blinkList = 'There are Blink node(s) inside:\n' + ', '.join(blinkList)
    return (blinkList)

print(isBlinkInside(nuke.selectedNode()))

# Check for expression errors on knobs ( solution from Erwan Leroy )
# https://community.foundry.com/discuss/topic/160172/how-to-print-expression-errors-like-it-s-in-the-error-console#1238910
# TODO need to turn into a def 

node = nuke.selectedNode()
import shlex
errorList = []
for n in node.nodes():
    for knob in n.allKnobs():
        if knob.hasExpression():
            expression = shlex.split(knob.toScript().strip('{}').replace(" ",""))
            full_name = knob.fullyQualifiedName()
            try:
                nuke.tcl('in {} {{expression {}}}'.format(full_name, expression[0]))
                result = "great! No expression error!"
            except RuntimeError as tcl_error:
                errorList.append('ERROR: {}: {}'.format(full_name, tcl_error))
if not errorList:
    print('Great! No expression error in the node!')
else:
    print('\n'.join(errorList))

##### (MORE) WIP PARTS #####

# Check Py 3 compatibility:
# https://stackoverflow.com/questions/40886456/how-to-detect-if-code-is-python-3-compatible
# Turn code Py3 compatibile if needed:
# https://docs.python.org/3/library/2to3.html

# Convert Gizmo to Group - also making sure that if ppl brought the node as a Gizmo{ somewhere it still does something as it is more likely an empty shell
# https://www.leafpictures.de/code/gizmo-to-group
# https://fredrikaverpil.github.io/2018/06/25/nuke-gizmos-to-groups/
# http://www.nukepedia.com/python/nodegraph/convertgizmostogroups

# NukeX compatibility - didn't find a function that sorts this so probably need to hard code the list of nodes only running on X
# https://www.foundry.com/products/nuke-family/nuke/features

# Check if there's a knobChanged() value or other callbacks

# Try to add part that checks if Copy would error without an "![exist parent.input]" part

# Disconnected nodes

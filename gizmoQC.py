#### WIP gizmo QC functions ####

# Check if node a Gizmo
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
    for n in node.nodes():
        if n.Class() == 'Viewer':
            viewerList.append(n.name())
        if n.Class() == 'Group':
            for i in n.nodes():
                if i.Class() == 'Viewer':
                    viewerList.append(i.name())
                if i.Class() == 'Group':
                    for x in n.nodes():
                        if x.Class() == 'Viewer':
                            viewerList.append(x.name())
                        if x.Class() == 'Group':
                            for y in n.nodes():
                                if y.Class() == 'Viewer':
                                    viewerList.append(y.name())
                                if y.Class() == 'Group':
                                    for z in n.nodes():
                                        if z.Class() == 'Viewer':
                                            viewerList.append(z.name())
    viewerList = 'There are Viewer node(s) inside:\n' + ', '.join(viewerList)
    if not viewerList:
        viewerList = 'Great! No Viewer node inside'
    return (viewerList)

print(isViewerInside(nuke.selectedNode()))

# Check if node has blink script inside
def isBlinkInside(node):
    msg = 'No blink script inside'
    for n in node.nodes():
        if n.Class() == 'BlinkScript' or n.Class() == 'ParticleBlinkScript':
            msg = 'There is a node with blink script inside'
        else:
            continue
    return msg

print(isBlinkInside(nuke.selectedNode()))


##### WIP PARTS #####

# Check for expression errors on knobs:
# https://community.foundry.com/discuss/topic/160172/how-to-print-expression-errors-like-it-s-in-the-error-console#1238910

# Check Py 3 compatibility:
# https://stackoverflow.com/questions/40886456/how-to-detect-if-code-is-python-3-compatible

# Convert Gizmo to Group
# https://www.leafpictures.de/code/gizmo-to-group
# https://fredrikaverpil.github.io/2018/06/25/nuke-gizmos-to-groups/
# http://www.nukepedia.com/python/nodegraph/convertgizmostogroups

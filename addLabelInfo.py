import nuke

def addLabelInfo():
    nodes = nuke.selectedNodes('Read')
    if len(nodes) == 0:
        nuke.alert('<font color=orange><h3>Please, select a Read node(s) first!')
    else:
        for n in nodes:
            n['label'].setValue("Shot: [lindex [split [value file] /] 4 ]_[lindex [split [value file] /] 6 ]_[lindex [split [value file] /] 8 ]\nVersion: [lindex [split [value file] /] 12 ]\nFormat: [lindex [value format] 0]*[lindex [value format] 1]\nFr.Range: [value first] - [value last]")

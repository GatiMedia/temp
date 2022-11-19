## assigning variables
BDADJUST_PREFIX = """<p align="""
all_backdrop = nuke.allNodes('BackdropNode')
label_values = []
name_values = []

## appending a lists from BackdropNodes and Backdrop_Adjusts
for n in all_backdrop:
    if n['label'].value():
        if not n['label'].value().startswith(BDADJUST_PREFIX):
            label_values.append(n['label'].value())
            name_values.append(n.name())
for n in all_backdrop:
    if n['label'].value().startswith(BDADJUST_PREFIX):
        if n['note'].value():
            label_values.append(n['note'].value())
            name_values.append(n.name())

## sorting the lists
zipped_lists = zip(label_values, name_values)
sorted_zipped_lists = sorted(zipped_lists)
sorted_names = [element for _, element in sorted_zipped_lists]
label_values.sort()
print(label_values)

## capping the length of the label value at 30 characters
for label in label_values:
    if len(label)>40:
        label_index = label_values.index(label)
        label_values.remove(label)
        new_label = label[:30] + "..."
        label_values.insert(label_index, new_label)

## defining the Search popup window
class BackdropSearchWindow(nukescripts.PythonPanel):
    def __init__(self):
        nukescripts.PythonPanel.__init__(self, 'BackdropAdjustSearch')
        self.setMinimumSize(400, 150)

        self.labelKnob = nuke.Enumeration_Knob('label_values', 'Labels', label_values)
        self.addKnob(self.labelKnob)

        self.spaceKnob = nuke.Text_Knob('space2', '')
        self.addKnob(self.spaceKnob)

        self.infoKnob = nuke.Text_Knob('info', '')
        self.infoKnob.setValue('<p style="font-size:20px">&#128269; Select Backdrop by label</p>')
        self.addKnob(self.infoKnob)

        self.infoKnob2 = nuke.Text_Knob('info2', '')
        self.infoKnob2.setValue('<p style="font-size:20px">and hit OK to Zoom on it!</p>')
        self.addKnob(self.infoKnob2)

        self.spaceKnob = nuke.Text_Knob('space3', '')
        self.addKnob(self.spaceKnob)

def createBDASearchPopup():
    bdS = BackdropSearchWindow()
    if bdS.showModalDialog():
        new_label = bdS.labelKnob.value()
        index = label_values.index(new_label)
    for node in nuke.allNodes():
        node.setSelected(False)
    selBDnode = nuke.toNode(sorted_names[index])
    print(selBDnode.getNodes())
    selBDnode.setSelected(True)
    if selBDnode.getNodes():
        for n in selBDnode.getNodes():
            n.setSelected(True)

    nuke.zoomToFitSelected()

createBDASearchPopup()

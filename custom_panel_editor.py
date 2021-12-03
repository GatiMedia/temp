### NODE CUSTOM PANEL EDITOR ###

import os
from datetime import date

if not len(nuke.selectedNodes()) == 1:
    nuke.message("\n<font color=yellow><b>Select a <u>single</u> node first!</font></b>\n")
else:
    userName = os.getenv('USER').split(".")[0].capitalize() + " " + os.getenv('USER').split(".")[1].capitalize()
    
    currDate = str(date.today())
    
    p = nuke.Panel('Node Custom Panel Editor')
    
    p.setWidth(500)
    p.addSingleLineInput('Node author version', '<e.g. 3.0>')
    p.addSingleLineInput('Node GBK version', '<e.g. 1.4>')
    p.addSingleLineInput('Link to source (optional)', '')
    p.addMultilineTextInput('Comment (optional)', '')
    p.addMultilineTextInput('TODO (optional)', '<e.g. - remove viewer\n- add new function>')
    
    ret = p.show()
    
    nodeAuthor = (p.value('Node author version'))
    nodeMajor = (p.value('Node GBK version'))
    nodeLink = str(p.value('Link to source (optional)'))
    nodeComment = str(p.value('Comment (optional)'))
    nodeTodo = str(p.value('TODO (optional)'))
    
    node = nuke.selectedNode()
    knobTab = nuke.Tab_Knob('gbk_user', 'GBK_User')
    node.addKnob(knobTab)
    
    knobName = nuke.Text_Knob('name', '')
    node.addKnob(knobName)
    knobName.setValue("Added by: " + userName + "\nDate: " + currDate)
    
    node.addKnob(nuke.Text_Knob('', ''))
    
    knobVersion = nuke.Text_Knob('version', '')
    node.addKnob(knobVersion)
    knobVersion.setValue("Author version: v" + nodeAuthor + "\nGBK Version: v" + nodeMajor)
    
    if nodeLink:
        knobLink = nuke.Text_Knob('link', '')
        node.addKnob(knobLink)
        knobLink.setValue("\"<a href=\"" + nodeLink + "\"><font color=yellow>Source</font></a>\"")
    else:
        pass
    
    node.addKnob(nuke.Text_Knob('', ''))
    
    if nodeComment:
        knobComment = nuke.Text_Knob('comment', '')
        node.addKnob(knobComment)
        knobComment.setValue("Comment: " + nodeComment )
    else:
        pass
    
    if nodeTodo:
        knobTodo = nuke.Text_Knob('todo', '')
        node.addKnob(knobTodo)
        knobTodo.setValue("TODO:\n" + nodeTodo )
    else:
        pass

## SmartVector to STMap ##

selSV = nuke.selectedNode()
sv_x = selSV['xpos'].value()
sv_y = selSV['ypos'].value()
sv_first = selSV['first'].value()
sv_last = selSV['last'].value()
sv_range = range(selSV['last'].value() - sv_first)
selSV.setSelected(False)

dot = nuke.nodes.Dot()
dot.setInput(0, selSV)
dot['xpos'].setValue(sv_x + 35)
dotx = dot['xpos'].value()
dot['ypos'].setValue(sv_y + 200)
doty = dot['ypos'].value()
dot.setSelected(True)

vecDist1 = nuke.createNode('VectorDistort')
vecDist1.setInput(0, dot)
vecDist1['reference_frame'].setValue(sv_first)
vecDist1['output_mode'].setValue('st-map')
vecDist1['xpos'].setValue(sv_x)
vecDist1['ypos'].setValue(doty + 200)
vecDistY = vecDist1['ypos'].value()
dot.setSelected(False)
vecDist1.setSelected(True)

#GBKWrite
from scarecrow.common import usage_logger;usage_logger.write_usage_log("nuke-menu","Write GBK");from nuketools import writetab;writetab.createFidoWriteNode()

dot.setSelected(True)


for i in sv_range[0::10]:
    try:
        vecDist2 = nuke.createNode('VectorDistort')
        vecDist2.setInput(0, dot)
        vecDist2['reference_frame'].setValue(sv_first+i)
        vecDist2['output_mode'].setValue('st-map')
        vecDist2['ypos'].setValue(vecDistY)
        vecDist2_x = sv_x
        #print (vecDist2_x)
        vecDist2['xpos'].setValue(vecDist2_x + (i * 33))
        vecDist2_x = vecDist2['xpos'].value()
        print (vecDist2_x)
        vecDist2.setSelected(True)
        #GBKWrite
        from scarecrow.common import usage_logger;usage_logger.write_usage_log("nuke-menu","Write GBK");from nuketools import writetab;writetab.createFidoWriteNode()
    except Exception:
        pass

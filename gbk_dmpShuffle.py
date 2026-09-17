
import nuke


def dmpShuffle():
    nodes = nuke.selectedNodes()

    X_DIST = 220
    Y_DIST = 200
    SELECT_VAL = True
    PREFIX_1 = "L_"
    PREFIX_2 = "OP_"
    if not len(nodes) == 1:
        nuke.alert('<font color=orange><h3>Please, select a single Read node first!')
    else:
        curSel = nuke.selectedNode()
        curSelChannels = curSel.channels()
        layersList = []
        for rawChannels in curSelChannels:
            splitRawChannels = rawChannels.split('.')
            layersList.append(splitRawChannels[0])
        channelLayers = list(set(layersList))
        channelLayers.sort()
        noteVal = '' + '\n'.join(channelLayers)

        new_layersList = []
        for l in channelLayers:
            if PREFIX_1 in l or PREFIX_2 in l:
                new_layersList.append(l)
            else:
                pass

        if len(new_layersList) == 1:
            nuke.alert('<font color=orange><h3><center>Not enough layers to break it down!\n\nOnly found:\n\n<font color=yellow><h4>' + ',\n'.join(new_layersList))
        else:
            # create dotMain
            dot = connectDot = nuke.nodes.Dot()
            dot['xpos'].setValue(int(curSel['xpos'].value()) + (curSel.screenWidth() / 2) - (dot.screenWidth() / 2))
            dot['ypos'].setValue(int(curSel['ypos'].value()) + 300)
            dot.setSelected(SELECT_VAL)
            dot.setInput(0, curSel)

            # creating remove_node
            remove_node = nuke.nodes.Remove()
            remove_node['xpos'].setValue(int(dot['xpos'].value())-36)
            remove_node['ypos'].setValue(int(dot['ypos'].value()) + Y_DIST)
            remove_node['operation'].setValue('remove')
            remove_node['channels'].setValue('all')
            remove_node.setSelected(SELECT_VAL)
            remove_node.setInput(0, dot)

            merge_node_old = None

            for index, n in enumerate(new_layersList):
                # creating dot
                newX = dot['xpos'].value()
                newY = dot['ypos'].value()
                oldDot = dot
                dot = nuke.nodes.Dot()
                dot['xpos'].setValue(int(newX) + X_DIST)
                dot['ypos'].setValue(newY)
                dot.setSelected(SELECT_VAL)
                newDot = dot
                newDot.setInput(0, oldDot)

                # creating shuffle
                shuffle = nuke.nodes.Shuffle2()
                shuffle['in1'].setValue(n)
                shuffle['label'].setValue("<b><center>" + n + "</b></center>")
                shuffle['note_font_size'].setValue(22)
                shuffle['xpos'].setValue(int(dot['xpos'].value())-36)
                shuffle['ypos'].setValue(int(dot['ypos'].value()) + Y_DIST)
                shuffle.setSelected(SELECT_VAL)
                shuffle.setInput(0, newDot)

                # creating unpremult
                unpremult = nuke.nodes.Unpremult()
                unpremult['xpos'].setValue(int(shuffle['xpos'].value()))
                unpremult['ypos'].setValue(int(shuffle['ypos'].value() + Y_DIST))
                unpremult.setSelected(SELECT_VAL)
                unpremult.setInput(0, shuffle)

                # creating premult
                premult = nuke.nodes.Premult()
                premult['xpos'].setValue(int(shuffle['xpos'].value()))
                premult['ypos'].setValue(int(unpremult['ypos'].value() + (2*Y_DIST)))
                premult.setSelected(SELECT_VAL)
                premult.setInput(0, unpremult)

                # creating dot_connect
                dot_connect = nuke.nodes.Dot()
                dot_connect['xpos'].setValue(int(dot['xpos'].value()))
                dot_connect['ypos'].setValue(int(premult['ypos'].value() + (Y_DIST*(1+index))))
                dot_connect.setSelected(SELECT_VAL)
                dot_connect.setInput(0, premult)

                #creating merge_node
                merge_node = nuke.nodes.Merge2()
                merge_node['xpos'].setValue(int(remove_node['xpos'].value()))
                merge_node['ypos'].setValue(int(dot_connect['ypos'].value()))
                merge_node['also_merge'].setValue('all')
                merge_node['label'].setValue(n)
                merge_node.setSelected(SELECT_VAL)
                merge_node.setInput(1, dot_connect)
                if index == 0:
                    merge_node.setInput(0, remove_node)
                else:
                    merge_node.setInput(0, merge_node_old)
                merge_node_old = merge_node

                if index + 1 == len(new_layersList):
                    # creating dot_connect
                    dot_connect = nuke.nodes.Dot()
                    dot_connect['xpos'].setValue(int(merge_node['xpos'].value()+36))
                    dot_connect['ypos'].setValue(int(merge_node['ypos'].value() + Y_DIST))
                    dot_connect.setSelected(SELECT_VAL)
                    dot_connect.setInput(0, merge_node)


if __name__ == "__main__":
    dmpShuffle()

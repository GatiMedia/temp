def findAndDeleteViewerNodes():
    viewers=[]
    for n in nuke.allNodes('Viewer'):
        viewers.append(n.fullName())
        nuke.delete(n)
    if viewers:
        viewers=str((', '.join(viewers)))
    else:
        viewers=None
    return viewers


def purgeGroups():
    all_viewers=[]



    all_viewers = [x for x in all_viewers if x is not None]
    print(all_viewers)
purgeGroups()



def purgeGroups():
    all_viewers=[]
    for g in nuke.allNodes('Group'):
        with g:
            all_viewers.append(findAndDeleteViewerNodes())
            for g in nuke.allNodes('Group'):
                with g:
                    all_viewers.append(findAndDeleteViewerNodes())
                    for g in nuke.allNodes('Group'):
                        with g:
                            all_viewers.append(findAndDeleteViewerNodes())
    all_viewers = [x for x in all_viewers if x is not None]
    print(all_viewers)
purgeGroups()

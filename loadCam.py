import os
import nuke

SLAP_PATH_PREFIX = "/LYR_030_cameraLayout/versions/"

def loadCam():
    nodes = nuke.selectedNodes('Read')
    if not len(nodes) == 1:
        nuke.alert('<font color=orange><h3>Please, select a single Read node\n of a Lighting Slapcomp first!')
    else:
        for n in nodes:
            shotdir = os.path.dirname(n['file'].value())
            slapcompdir = "/".join(shotdir.split("/")[:-4]) + SLAP_PATH_PREFIX
            if not os.path.isdir(slapcompdir):
                nuke.alert('<font color=orange><h3>Can`t find a camera folder at:\n\n<h4>' + slapcompdir + '<h3>\n\n:((((')
            else:
                folders = []
            for folder in os.listdir(slapcompdir):
                d = os.path.join(slapcompdir, folder)
                if os.path.isdir(d):
                    folders.append(folder)
            folders.sort()
            last_version_folder = folders[-1]
            for file in os.listdir(slapcompdir + last_version_folder):
                if file.endswith(".abc"):
                    cam_path = os.path.join(slapcompdir + last_version_folder, file)
                    cam = nuke.nodes.Camera2()
                    cam['read_from_file'].setValue(True)
                    cam['file'].setValue(cam_path)
                    cam['xpos'].setValue(n['xpos'].value())
                    cam['ypos'].setValue(n['ypos'].value()+200)
                    cam['label'].setValue("Version: " + last_version_folder + "\nShot: " + "_".join(file.split("_")[2:]))
                    cam.setSelected(True)
                    n.setSelected(False)

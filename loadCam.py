import os
import nuke

SLAP_PATH_PREFIX = "/LYR_030_cameraLayout/versions/"

def loadCam():
    nodes = nuke.selectedNodes('Read')
    if len(nodes) == 0:
        nuke.alert('<font color=orange><h3>Please, select a Read node(s)\n of a Beauty render first!')
    else:
        cameras = []
        for n in nodes:
            shotdir = os.path.dirname(n['file'].value())
            camdir = "/".join(shotdir.split("/")[:-4]) + SLAP_PATH_PREFIX
            if not os.path.isdir(camdir):
                nuke.alert('<font color=orange><h3>Can`t find a camera folder at:\n\n<h4>' + camdir + '<h3>\n\n:((((')
            else:
                folders = []
                for folder in os.listdir(camdir):
                    d = os.path.join(camdir, folder)
                    if os.path.isdir(d):
                        folders.append(folder)
                folders.sort()
                last_version_folder = folders[-1]
                for file in os.listdir(camdir + last_version_folder):
                    if file.endswith(".abc"):
                        cam_path = os.path.join(camdir + last_version_folder, file)
                        cam = nuke.nodes.Camera2()
                        cam['read_from_file'].setValue(True)
                        cam['file'].setValue(cam_path)
                        cam['xpos'].setValue(n['xpos'].value())
                        cam['ypos'].setValue(n['ypos'].value()+200)
                        cam['label'].setValue("\Shot: " + "_".join(file.split("_")[2:]) + "\nVersion: " + last_version_folder)
                        cam.showControlPanel()
                        cameras.append(cam.name())
        for node in nuke.selectedNodes():
            node.setSelected(False) 
        print(cameras)
        for camera in cameras:
            nuke.toNode(camera).setSelected(True)

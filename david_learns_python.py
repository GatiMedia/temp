

# 1 # Create a Nuke menu


# --------------------------------------------------------------
#  GLOBAL IMPORTS ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

import nuke

# ----- CREATE UTILITIES MENU & ASSIGN ITEMS -------------------

utilitiesMenu = nuke.menu('Nuke').addMenu('Davbids Menu')

# ----------------------------------------------------------------
#  CUSTOM FUNCTIONS ::::::::::::::::::::::::::::::::::::::::::::::
# ----------------------------------------------------------------


def close():
    for node in nuke.allNodes(recurseGroups=True):
        node.hideControlPanel()

try:
    utilitiesMenu.addCommand('Close Properties', 'close()', 'shift+d', icon='Tile.png')
except:
    pass



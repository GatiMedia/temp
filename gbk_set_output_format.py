# --------------------------------------------------------------
#  set_output_format.py
#  Last Updated by: Attila Gasparetz
#  Last Updated: 09/07/2026
# --------------------------------------------------------------

import nuke

def setOutputFormat():
    for n in nuke.selectedNodes():
        try:
            if n.Class() == "Reformat":
                if "Output Resolution_2" in n['format'].toScript() or "Output Resolution_1" in n['format'].toScript():
                    try:
                        n['format'].setValue('Output Resolution')
                    except:
                        pass
                    if "Output Resolution_2" in n['format'].toScript():
                        n['format'].setValue('Output Resolution_1')
                    else:
                        pass
                else:
                    pass
            else:
                pass
        except:
            pass

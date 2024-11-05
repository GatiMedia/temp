# --------------------------------------------------------------
#  sg_buddy.py
#  Version: 1.0
#  Last Updated: 05/11/2024
#  Last updated by: Attila Gasparetz
# --------------------------------------------------------------

import nuke
import os
import re


def add_missing_frames():
    if len(nuke.selectedNodes('WriteTank')) == 0:
        nuke.alert('<font color=orange><h3>Please, select at least a single SGWrite node first!')
    else:
        for n in nuke.selectedNodes('WriteTank'):
            context = n["path_context"].value()
            local = n["path_local"].value()
            path = os.path.join(context, local[:-2], str("main/"))

            files = []
            for (dirpath, dirnames, filenames) in os.walk(path):
                files.extend(filenames)
                break
            file_ends = []
            for f in files:
                file_end_matches = (re.findall('\d\d\d\d.exr', f))
                file_ends.extend(file_end_matches)
              
            extension = re.compile(r'.exr')
            frame_values = [extension.sub('', string) for string in file_ends]

            first_frame = (int(nuke.toNode('root')['first_frame'].value()))
            last_frame = (int(nuke.toNode('root')['last_frame'].value()))

            frame_values = [int(num) for num in frame_values]
            full_fr_range = [int(num) for num in range(first_frame, last_frame + 1)]

            missing_frames = []
            for fr in full_fr_range:
                if fr not in frame_values:
                    missing_frames.append(fr)

            def get_line_numbers_concat(line_nums):
                seq = []
                final = []
                last = 0
                for index, val in enumerate(line_nums):
                    if last + 1 == val or index == 0:
                        seq.append(val)
                        last = val
                    else:
                        if len(seq) > 1:
                            final.append(str(seq[0]) + '-' + str(seq[len(seq) - 1]))
                        else:
                            final.append(str(seq[0]))
                        seq = []
                        seq.append(val)
                        last = val
                    if index == len(line_nums) - 1:
                        if len(seq) > 1:
                            final.append(str(seq[0]) + '-' + str(seq[len(seq) - 1]))
                        else:
                            final.append(str(seq[0]))
                final_str = ', '.join(map(str, final))
                return final_str

            n['frames'].setValue(str(get_line_numbers_concat(missing_frames)))
          
def add_root_range():
    if len(nuke.selectedNodes('WriteTank')) == 0:
        nuke.alert('<font color=orange><h3>Please, select at least a single SGWrite node first!')
    else:
        for n in nuke.selectedNodes('WriteTank'):
            first_frame = (int(nuke.toNode('root')['first_frame'].value()))
            last_frame = (int(nuke.toNode('root')['last_frame'].value()))
            n['frames'].setValue(str(first_frame) + " - " + str(last_frame))

<?xml version="1.0" encoding="UTF-8"?><script>


print(type(nuke.ViewerWindow()))

#Get the bbox data
bboxinfo = nuke.activeViewer().node()['colour_sample_bbox'].value()
#Get the aspect of the input. Note that we sample input[0] for the width and height info!
aspect = float(self.node.input(0).width())/float(self.node.input(0).height())
#Convert relative coordinates into x and y coordinates
self.mousePosition = [(bboxinfo[0]*0.5+0.5)*self.node.input(0).width(),(((bboxinfo[1]*0.5)+(0.5/aspect))*aspect)*self.node.input(0).height()]

bboxinfo = nuke.activeViewer().node()['colour_sample_bbox'].value()



print(bboxinfo)


activeViewer = nuke.activeViewer().node()
formatWidth = activeViewer.width()
formatHeight = activeViewer.height()
formatAspect = float(formatHeight) / float(formatWidth)

print(formatWidth)


info = activeViewer.knob('colour_sample_bbox').value()


print(info)


m = nuke.toNode('Viewer1').input(0).width()

print(m)




bbox = nuke.activeViewer().node().input(nuke.activeViewer().activeInput()).bbox()
print bbox.x(), bbox.y(), bbox.w(), bbox.h()


m = nuke.activeViewer().node().roi()
print(m)



m = nuke.ViewerWindow()[getGLCameraMatrix()]

print(m)


help(nuke.activeViewer().node())


nuke.activeViewer().node().capture(&quot;D:\test.test01.####.jpg&quot;)

m = nuke.activeViewer().node().screenWidth()
n = nuke.activeViewer().node().screenHeight()
print(m,n)

m = nuke.activeViewer().node()['colour_sample_bbox'].value()
print(m)




m = nuke.activeViewer().node()['colour_sample_bbox'].value()
print(m)






#Get the bbox data

bboxinfo = nuke.activeViewer().node()['colour_sample_bbox'].value()

#Get the aspect of the input. Note that we sample input[0] for the width and height info!

aspect = float(self.node.input(0).width())/float(self.node.input(0).height())

#Convert relative coordinates into x and y coordinates

mousePosition = [(bboxinfo[0]*0.5+0.5)*self.node.input(0).width(),(((bboxinfo[1]*0.5)+(0.5/aspect))*aspect)*self.node.input(0).height()]

print(mousePosition)


m = nuke.activeViewer().node()['center'].value()
print(m)

m = nuke.toNode('Viewer1')['center'].value()
print(m)


m = nuke.ViewerContext()['mouse_x'].value
print(m)

m = nuke.activeViewer().node()
print(m)




######



### FIRST STEP ###

print (&quot;Hello World!&quot;)

### USING VARIABLE ###

name = 'Attila'
age = '30'
country = 'Hungary'
print ('Hello, my name is  ' + name + '! I am ' + age + '. I am from ' + country)

name = 'Attila'
age = 30
country = 'Hungary'
print(&quot;Hello, my name is  %s! I am %d. I am from %s.&quot; % (name, age, country))

# %d will truncate to integer, %s will maintain formatting, %f will print as float and %g is used for generic number

name = 'Attila'
age = 30
country = 'Hungary'
print(&quot;Hello, my name is  {}! I am {}. I am from {}.&quot;.format(name, age, country))

### TYPE CONVERSION ###

# Integer - int(x)

x = 12.8
print type(x)
x = int(x)
print type(x)
print x

# Float - float(x)

x = 12
print type(x)
x = float(x)
print type(x)
print x

# String - str(x)

x = 12.5
print type(x)
x = str(x)
print type(x)
print x

### CREATE A NODE ###
## Functions: createNode, setValue ##

# Can check node's Class with the `i` hotkey
nuke.createNode(&quot;Blur&quot;)

# Make sure you used a right Class
nuke.createNode(&quot;Tracker4&quot;)

# Can call nodes that are removed from GUI
nuke.createNode(&quot;Blocky&quot;)
nuke.createNode(&quot;Twist&quot;)

# Set a value
nuke.createNode(&quot;Blur&quot;)['size'].setValue(80)

# Set multiple values using a variable
m = nuke.createNode(&quot;Blur&quot;)
m['channels'].setValue(&quot;rgb&quot;)
m['size'].setValue(50)
m['mix'].setValue(.5)
m['label'].setValue(&quot;Size: [value size]\nChannels: [value channels]\nMix: [value mix]&quot;)

# Creating node for scripting
nuke.nodes.Blur()

nuke.nodes.Blur(mix=.5,size=10)

### GETTING KNOB VALUE ###
## Functions: toNode, value, getValue, knob ###

# Calling knobs as list items
nuke.toNode('Blur1')[&quot;channels&quot;].value()

# Calling knobs with a function
nuke.toNode('Blur1').knob(&quot;channels&quot;).value()

nuke.toNode('Blur1')[&quot;filter&quot;].getValue()

### SETTING KNOB VALUE ###
## Functions: setValue ##

# Setting single value
nuke.toNode('Blur1')[&quot;size&quot;].setValue(10)

# Setting multiple values
b = nuke.toNode('Blur1')
b[&quot;size&quot;].setValue(20)
b[&quot;mix&quot;].setValue(.8)
b[&quot;filter&quot;].setValue(0)
b[&quot;channels&quot;].setValue(&quot;rgb&quot;)

### SETTING EXPRESSION VALUE ###
## Functions: setExpression ##

nuke.toNode('Blur1')[&quot;size&quot;].setExpression('Blur2.size * 2')

# You can add expression to knobs with python you can't do manually in some cases
nuke.toNode('Transform1')[&quot;filter&quot;].setExpression(&quot;Transform2.filter&quot;)

### REMOVE ANIMATION / EXPRESSION ###
## Functions: clearAnimated ##

nuke.toNode('Transform1')[&quot;filter&quot;].clearAnimated()

### CREATE MULTIPLE NODES WITH `FOR LOOP` ###
## Functions: range ##

for i in range(15):
    i = nuke.createNode(&quot;Blur&quot;)
    i[&quot;channels&quot;].setValue('rgb')
    i[&quot;size&quot;].setExpression('Blur1.size')

### CONNECT MULTIPLE NODES TO A SINGLE NODE ###
## Functions: selectedNodes, setInput ##

t = nuke.toNode('Transform1')
nodes = nuke.selectedNodes()
for i in nodes:
    i.setInput(0, t)
    i.setInput(1, None)

### RUN ON ANY SELECTED NODES ###
## Functions: selectedNodes ##

nodes = nuke.selectedNodes()
for node in nodes:
    try:
        node.knob(&quot;size&quot;).setValue(5)
    except Exception:
        pass

### RUN ON ALL NODES IN A SCRIPT ###
## Functions: allNodes ##

nodes = nuke.allNodes()
for node in nodes:
    try:
        node.knob(&quot;size&quot;).setValue(20)
    except Exception:
        pass

### RUN AN ALL SPECIFIED CLASSES ###

nodes = nuke.allNodes('Merge2')
for node in nodes:
    node.knob(&quot;mix&quot;).setValue(.5)

### RUN AN SELECTED SPECIFIED CLASSES ###

nodes = nuke.selectedNodes('Merge2')
for node in nodes:
    try:
        node.knob(&quot;mix&quot;).setValue(.8)
    except Exception:
        pass

### RUN ON ALL MULTIPLE CLASSES ###

nodes_classes = [&quot;Read&quot;, &quot;PostageStamp&quot;, &quot;Constant&quot;, &quot;ColorBars&quot;, &quot;CheckerBoard2&quot;, &quot;ColorWheel&quot;]

for node in nuke.allNodes(group=nuke.root()):
    if node.Class() not in nodes_classes:
        continue
    try:
        node[&quot;postage_stamp&quot;].setValue(False)
    except Exception:
        pass

### RUN ON SELECTED MULTIPLE CLASSES ###

nuke.root().begin()
nodes_classes = [&quot;Read&quot;, &quot;PostageStamp&quot;, &quot;Constant&quot;, &quot;ColorBars&quot;, &quot;CheckerBoard2&quot;, &quot;ColorWheel&quot;]
for node in nuke.selectedNodes():
    if node.Class() not in nodes_classes:
        continue
    try:
        node[&quot;postage_stamp&quot;].setValue(True)
    except Exception:
        pass
nuke.root().end()

### PATH FOR YOUR NUKE FOLDER ###

nuke.pluginPath()

### PERFORMANCE TIMER ###

#start
nuke.startPerformanceTimers()

#reset
nuke.resetPerformanceTimers()

#stop
nuke.stopPerformanceTimers()

# https://learn.foundry.com/nuke/developers/90/pythondevguide/performance.html

### FUN ###

import webbrowser
sel = nuke.selectedNode()
site = 'https://imgur.com/search/score/?q=cat'
name = nuke.PyScript_Knob('button', '&lt;font color=pink&gt;Click HERE', &quot;webbrowser.open(site)&quot;)
sel.addKnob(name)

### NOTES ###

# For checkboxes the value can be True or False that equals to 1 or 0

# For dropdown menu values can be the name of the option or the serial number of the option starting with 0 from the top

# To find the Class of the node select it and press `i` over the NodeGraph



m = nuke.toNode('ScanlineRender1')[&quot;antialiasing&quot;].getValue()
print (m)

m = nuke.toNode('ScanlineRender1')[&quot;antialiasing&quot;].value()
print (m)


m = nuke.toNode('ScanlineRender1')[&quot;antialiasing&quot;].hasExpression()
print (m)


nuke.toNode('ScanlineRender1')[&quot;antialiasing&quot;].setExpression('[python 0.0 if nuke.executing() else 3.0]')


nuke.toNode('ScanlineRender1')[&quot;antialiasing&quot;].clearAnimated()


nuke.pluginPath()


nuke.toNode('Transform1')[&quot;filter&quot;].setValue('3.0')

m = nuke.toNode('Transform1')[&quot;filter&quot;].getValue()
print (m)

m = nuke.toNode('Transform1')[&quot;filter&quot;].hasExpression()
print (m)


nuke.toNode('Transform1')[&quot;filter&quot;].setExpression('[python 1.0 if nuke.executing() else 3.0]')


nuke.toNode('Transform1')[&quot;filter&quot;].clearAnimated()



####

#### Print all nodes` name in a script ####


names = []

expressionL = []


for s in nuke.allNodes():
    names.append(s['name'].value())
    expressionL.append(s.hasExpression())
    print (', '.join(names + expressionL))




m = nuke.toNode('ScanlineRender1')

expR = []

for i in m:
    expR.append(i.hasExpression())


node = nuke.selectedNode()
for knob in node.allKnobs():
    if knob.hasExpression():
        for anim in knob.animations():
            expr = anim.expression()
print(expr)

##



nodes = nuke.selectedNodes()
for i in nodes:
    names = nuke.toNode(i['name'].value())
    for knob in names.allKnobs():
        if knob.hasExpression():
            for anim in knob.animations():
                expr = anim.expression()
print (expr)


for knob in node.allKnobs():
    if knob.hasExpression():
        for anim in knob.animations():
            expr = anim.expression()


import re
for node in nuke.allNodes(recurseGroups=True):
    for knob in node.allKnobs():
        if knob.hasExpression():
            for anim in knob.animations():
                expr = anim.expression()
                if re.search(&quot;\$gui&quot;, expr):
                    node.setSelected(True)
                    nuke.zoomToFitSelected()
                    print &quot;Knob: %s.%s&quot; % (node.fullName(), anim.knobAndFieldName())

###


names = []


expressionL = []

for s in nuke.selectedNodes():
    expressionL.append(s.hasExpression())
    print (', '.join(expressionL))




# Print knob value with getValue()
print (nuke.toNode('ScanlineRender1')[&quot;antialiasing&quot;].getValue())

# Print knob value with value()
print (nuke.toNode('ScanlineRender1')[&quot;antialiasing&quot;].value())

# Assigning $gui for antialiasing making 'none' on use and 'high' on farm
nuke.toNode('ScanlineRender1')[&quot;antialiasing&quot;].setExpression('$gui ? 0.0 : 3.0')

# Checking if the knob has expression
print(nuke.toNode('ScanlineRender1')[&quot;antialiasing&quot;].hasExpression())

# Checking if the knob is animated
print(nuke.toNode('ScanlineRender1')[&quot;antialiasing&quot;].isAnimated())

# Removing expression from the knob
nuke.toNode('ScanlineRender1')[&quot;antialiasing&quot;].clearAnimated()








####


import platform
import subprocess
import os

# get write node
writeNode = nuke.selectedNode()

# get path to directory
path = writeNode.knob('file').evaluate()
path = os.path.dirname(path)


operatingSystem = platform.system()

# windows
if operatingSystem == 'Windows':
    os.startfile(path)
# mac
elif operatingSystem == 'Darwin':
    subprocess.Popen(['open', path])
# linux
else:
    subprocess.Popen(['xdg-open', path])


#####

node_xpos = []
node_ypos = []
if nuke.selectedNodes():
    for s in nuke.selectedNodes():
        node_xpos.append(s['xpos'].value())
        node_ypos.append(s['ypos'].value())
    
    x_max = max(node_xpos)
    x_min = min(node_xpos)
    
    x_width = (float(x_max) - float(x_min))
    print (x_width)
    
    y_max = max(node_ypos)
    y_min = min(node_ypos)
    
    y_height = (float(y_max) - float(y_min))
    print (y_height)
    
    bd = nuke.thisNode()
    bd.setXpos(int(x_min) - 100)
    bd['bdwidth'].setValue(x_width+300)
    bd.setYpos(int(y_min) - 200)
    bd['bdheight'].setValue(y_height+300)
else:
    nuke.message('&lt;font color=orange&gt;&lt;b&gt;Select nodes first!')




####


def create_BD_Adj():
    node_xpos = []
    node_ypos = []
    if nuke.selectedNodes():
        for s in nuke.selectedNodes():
            node_xpos.append(s['xpos'].value())
            node_ypos.append(s['ypos'].value())

        x_max = max(node_xpos)
        x_min = min(node_xpos)

        x_width = (float(x_max) - float(x_min))

        y_max = max(node_ypos)
        y_min = min(node_ypos)

        y_height = (float(y_max) - float(y_min))

        bd_this = nuke.createNode('Backdrop_Adjust')

        bd_this.setXpos(int(x_min) - 100)
        bd_this['bdwidth'].setValue(x_width + 300)
        bd_this.setYpos(int(y_min) - 200)
        bd_this['bdheight'].setValue(y_height + 300)
        bd_this.hideControlPanel()
    else:
        bd_that = nuke.createNode('Backdrop_Adjust')
        bd_that.hideControlPanel()


nuke.menu('Nodes').addMenu('Other').addCommand('BackdropAdjust.', 'create_BD_Adj()', shortcut='ctrl+b', icon='Backdrop.png', index=3)



####


z_list = []

for s in nuke.selectedNodes():
    try:
        z_list.append(s['z_order'].value())
    except:
        pass

print min(z_list)



##


node_xpos = []
node_ypos = []
z_list = []
if nuke.selectedNodes():
    for s in nuke.selectedNodes():
        try:
            node_xpos.append(s['xpos'].value())
            node_ypos.append(s['ypos'].value())
            z_list.append(s['z_order'].value())
        except:
            pass

    x_max = max(node_xpos)
    x_min = min(node_xpos)
    
    x_width = (float(x_max) - float(x_min))
    print (x_width)
    
    y_max = max(node_ypos)
    y_min = min(node_ypos)
    
    y_height = (float(y_max) - float(y_min))
    print (y_height)
    
    if not z_list:
        z_list.append(0)
    z_min = min(z_list)


    bd = nuke.thisNode()
    bd.setXpos(int(x_min) - 100)
    bd['bdwidth'].setValue(x_width+300)
    bd.setYpos(int(y_min) - 200)
    bd['bdheight'].setValue(y_height+300)
    bd['z_order'].setValue(z_min - 1)
else:
    nuke.message('&lt;font color=orange&gt;&lt;b&gt;Select nodes first!')


####



##


# Dec to Hex

print hex(948866560)

# Dec to Hex

s = &quot;0x186e6e00&quot;

i = int(s, 16)

print (str(i))


##

s = &quot;0x388e8e00&quot;

print (s[4:6])


##

import colorsys
m = colorsys.rgb_to_hsv(0.2, 0.4, 0.4)
print (m)


##

s = &quot;0x388e8e00&quot;


r = (s[2:4])

g = (s[4:6])

b = (s[6:8])

print(b)



h = input('Enter hex: ').lstrip('#')

# Hex to RGB

h = &quot;B4FBB8&quot;
print('RGB =', tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))

Enter hex: #B4FBB8
RGB = (180, 251, 184)

# RGB to Hex

print ('%02x%02x%02x' % (0, 228, 64))

#######


dec_til = nuke.toNode('BackdropNode8')['tile_color'].getValue()

### MODIFY TILE COLOR ###

color_list = []

for s in nuke.selectedNodes('BackdropNode'):
    try:
        color_list.append(s['tile_color'].value())
    except:
        pass

dec_til = min(color_list)

# Dec to Hex
hex_til = hex(int(dec_til))

# Hex strip
hex_til_to_rgb = hex_til[2:8]

# Hex to RGB
rgb_til = tuple(int(hex_til_to_rgb[i:i+2], 16) for i in (0, 2, 4))

rgb_til_list = list(rgb_til)

# Modifying RGB to a new value
rgb_til_list_new = []
for i in rgb_til_list:
    rgb_til_list_new.append(i - 30)

# Preventing minus values
for n, i in enumerate(rgb_til_list_new):
   if i &lt; 0:
      rgb_til_list_new[n] = 1

# RGB to Hex
new_hex = ('%02x%02x%02x' % (rgb_til_list_new[0], rgb_til_list_new[1], rgb_til_list_new[2])) + '00'

# Hex to Dec
new_dec = int(new_hex, 16)

nuke.toNode('BackdropNode9')['tile_color'].setValue(int(new_dec))


print (dec_til)
print (hex_til)
print (rgb_til_list_new)
print (new_dec)

#####


m = nuke.toNode('Backdrop_Adjust3')['tile_color'].value()
print (m)

#####





nuke.pluginPath()




####


import nukescripts
import nuke
import colorsys
import struct


def createDakerBD():

    def hex2rgb(rgb):
        return struct.unpack('BBB', rgb.decode('hex'))

    def rgb2hex(rgb):
        return struct.pack('BBB', *rgb).encode('hex')

    #this func takes in and integer color and reduces it's luminance by half. If it errors it means that one of the convertions is not possible. AKA we are too close to 0
    def alter_integer_luma(tile_integer, loss):

        tile_integer = int(tile_integer) # removing decimal point that messes up in the hex func

        try:
            old_rgb = hex2rgb(hex(tile_integer)[2:-2]) #stripping the initial 0x and ending ff from the color value
            hls = colorsys.rgb_to_hls(old_rgb[0], old_rgb[1], old_rgb[2])
            new_rgb = colorsys.hls_to_rgb(hls[0], hls[1]/loss, hls[2])
            new_hex = rgb2hex(new_rgb)
            full_hex = str(new_hex) + 'ff'
            new_int = int(full_hex, 16) # this is the best conversion from hex to nuke that I found
            return new_int

        except Exception:
            return 255 # 255 is black in nuke's weird integers colors

    def calc_integer_luma(tile_integer):
        try:
            rgb = hex2rgb(hex(int(tile_integer))[2:-2]) #stripping the initial 0x and ending ff from the color value
            luma = (rgb[0]*0.2116) + (rgb[1]*0.7152) + (rgb[2]*0.0722)
            return luma
        except Exception:
            return 0

    # creates backdrop using the autobackdrop script
    backdrop =  nukescripts.autobackdrop.autoBackdrop()
    bd_color = int(backdrop['tile_color'].getValue())

    sel = nuke.selectedNodes('BackdropNode')

    min_luma = 99999 #this is basicaly an impossibly high ammount of luma
    loss = 2.0 #is the ammount of luminance we want to loose for every step (1 is none, 2 is half)

    for e in sel:
        color = int(e['tile_color'].getValue())
        this_luma = calc_integer_luma(color)
        if this_luma &lt; min_luma:
            min_luma = this_luma

    while calc_integer_luma(bd_color) &gt; min_luma:
        bd_color = alter_integer_luma(bd_color, loss)
        
    if min_luma == 0:
        bd_color = 255

    backdrop['tile_color'].setValue(bd_color)



m = nuke.toNode('Backdrop_Adjust3')['tile_color'].value()
n = createDakerBD(m)

print (n)


# map

my_list = [1,2,3]

def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, my_list)))

# filter

my_list = [1,2,3]

def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list)))

# zip

my_list = [1,2,3]

your_list = [10, 20, 30]

m =  (list(zip(my_list, your_list)))

print (m)

# reduce

from functools import reduce

my_list = [1,2,3]

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print (reduce(accumulator ,my_list, 10))



###


def create_BD_Adj():
    node_Xpos = []
    node_Ypos = []
    z_List = []
    sel = nuke.selectedNodes()
    if sel:
        for s in sel:
            try:
                node_Xpos.append(s['xpos'].value())
                node_Ypos.append(s['ypos'].value())
                z_List.append(s['z_order'].value())
            except:
                pass

        x_Max = max(node_Xpos)
        x_Min = min(node_Xpos)

        x_Width = (float(x_Max) - float(x_Min))

        y_Max = max(node_Ypos)
        y_Min = min(node_Ypos)

        y_Height = (float(y_Max) - float(y_Min))

        if not z_List:
            z_List.append(0)
        z_Min = min(z_List)

        #TODO add darker tile color part

        ok_colors = [3149642751, 2863311615, 2576980479, 2290649343, 2004318207, 1717987071, 1431655935, 1145324799, 572662527, ]

        bd_this = nuke.createNode('Backdrop_Adjust')



        bd_this.setXpos(int(x_Min) - 100)
        bd_this['bdwidth'].setValue(x_Width + 300)
        bd_this.setYpos(int(y_Min) - 200)
        bd_this['bdheight'].setValue(y_Height + 300)
        bd_this['z_order'].setValue(z_Min - 1)
        bd_this.hideControlPanel()
    else:
        bd_that = nuke.createNode('Backdrop_Adjust')
        bd_that['tile_color'].setValue(1717987071)
        bd_that['z_order'].setValue(0)
        bd_that.hideControlPanel()


nuke.menu('Nodes').addMenu('Other').addCommand('BackdropAdjust.', 'create_BD_Adj()', shortcut='ctrl+b', icon='Backdrop.png', index=3)


###



bd_this = nuke.toNode('Backdrop_Adjust')

ok_colors = [3149642751, 2863311615, 2576980479, 2290649343, 2004318207, 1717987071, 1431655935, 1145324799,
             572662527, 286331391, 255]

if nuke.selectedNodes('BackdropNode'):
    existing_indexes = [0]
    for bd in nuke.selectedNodes('BackdropNode'):
        color = int(bd['tile_color'].getValue())
        try:
            curr_index = ok_colors.index(color)
            existing_indexes.append(curr_index)
        except ValueError:
            continue

    new_index = sorted(existing_indexes)[-1] + 1

    try:
        bd_this['tile_color'].setValue(ok_colors[new_index])
    except IndexError:
        bd_this['tile_color'].setValue(ok_colors[-1])
else:
    bd_this['tile_color'].setValue(3149642751)


###

b = nuke.toNode('Backdrop_Adjust')
b['bdwidth'].setValue(500)
b['bdheight'].setValue(500)
b['z_order'].setValue(0)



nuke.pluginPath()

#fromTom

if s.Class() == &quot;BackDrop&quot;:
    node_xpos.append(s['xpos'].value()+s['bdwidth'].value())
else:
    node_xpos.append(s['xpos'].value())






node_xpos = []
node_ypos = []
z_List = []

if s.Class() == &quot;BackDrop&quot;:
    node_xpos.append(s['xpos'].value())
    node_xpos.append(s['xpos'].value()+s['bdwidth'].value())
    node_ypos.append(s['ypos'].value())
    node_xpos.append(s['ypos'].value() + s['bdheight'].value())
    z_List.append(s['z_order'].value())
else:
    node_xpos.append(s['xpos'].value())
    node_ypos.append(s['ypos'].value())

print (&quot;\node_xpos: &quot; + str(node_xpos))
print (&quot;node_ypos: &quot; + str(node_ypos))

### CURRENT FOR NODE


bd = nuke.toNode('Backdrop_Adjust')



node_xpos = []
node_ypos = []
z_List = []
corner_x = []
corner_y = []
corner_bottom = []
if nuke.selectedNodes('BackdropNode'):
    sel_bd = nuke.selectedNodes('BackdropNode')
    for s in sel_bd:
        node_xpos.append(s['xpos'].value())
        node_ypos.append(s['ypos'].value())
        node_xpos.append(s['ypos'].value() + s['bdheight'].value())
        z_List.append(s['z_order'].value())
    else:
        pass

print (&quot;\node_xpos: &quot; + str(node_xpos))
print (&quot;node_ypos: &quot; + str(node_ypos))
print (&quot;corner_bottom: &quot; + str(corner_bottom))


if nuke.selectedNodes():
    for s in nuke.selectedNodes():
        node_xpos.append(s['xpos'].value())
        node_ypos.append(s['ypos'].value())
        
    
    x_max = max(node_xpos)
    x_min = min(node_xpos)
    
    print (&quot;node_xpos: &quot; + str(node_xpos))
    print (&quot;node_ypos: &quot; + str(node_ypos))

    print (&quot;x_max: &quot; + str(x_max))
    print (&quot;x_min: &quot; + str(x_min))


    x_width = (float(x_max) - float(min(node_xpos)))


    y_max = max(node_ypos)
    y_min = min(node_ypos)


    #if not corner_bottom:
     #   corner_bottom.append(y_max - 1.0)
    #cornerYMax = max(corner_bottom)

    #print (&quot;cornerYMax: &quot; + str(cornerYMax))
    #print (&quot;y_max: &quot; + str(y_max))


    #if cornerYMax &gt; y_max:
     #   extra_y = abs((float(y_max) - float(cornerYMax)))
    #else:
     #   extra_y = 0

    #print (&quot;extra_y: &quot; + str(extra_y))


    y_height =  abs((float(min(node_ypos)) - float(y_max)) )


    print (&quot;y_max: &quot; + str(y_max))
    print (&quot;y_min: &quot; + str(y_min))

    print (&quot;x_width: &quot; + str(x_width))
    print (&quot;y_height: &quot; + str(y_height))

    if not corner_x:
        corner_x.append(x_max - 1.0)
    cornerXMin = min(corner_x)
    xMax = max(node_xpos)

    print (&quot;cornerMin: &quot; + str(cornerMin))

    print (&quot;xMax: &quot; + str(xMax))

    if cornerXMin &lt; xMax:
        extra_val = 100
    else:
        extra_val = 0

    print (&quot;extra_val: &quot; + str(extra_val))

    if not z_List:
        z_List.append(0)
    z_Min = min(z_List)

    bd.setXpos(int(x_min) - 100)
    bd['bdwidth'].setValue(x_width + extra_val + 200)
    bd.setYpos(int(y_min) - 200)
    bd['bdheight'].setValue(y_height + extra_y + 300)
    bd['z_order'].setValue(z_Min - 1)






####


this = nuke.selectedNode()

print (&quot;\nname: &quot; + str(this['name'].value()))
print (&quot;ypos: &quot; + str(this['ypos'].value()))

print (&quot;xpos: &quot; + str(this['xpos'].value()))

print (&quot;bdwidth: &quot; + str(this['bdwidth'].value()))
print (&quot;bdheight: &quot; + str(this['bdheight'].value()))


###

corner_x = []
corner_y = []

if nuke.selectedNodes('BackdropNode'):
    sel_bd = nuke.selectedNodes('BackdropNode')
    for s in sel_bd:
        corner_x.append(s['xpos'].value() + s['bdwidth'].value())
        corner_y.append(s['ypos'].value() - s['bdheight'].value())

corner_x_max = max(corner_x)
corner_y_min = min(corner_y)


print (corner_x_max)
print (corner_y_min)


###

bd = nuke.toNode('Backdrop_Adjust')

node_xpos = []
node_ypos = []
z_List = []
corner_x = []
corner_y = []
corner_bottom = []
if nuke.selectedNodes('BackdropNode'):
    sel_bd = nuke.selectedNodes('BackdropNode')
    for s in sel_bd:
        corner_x.append(s['xpos'].value() + s['bdwidth'].value())
        corner_y.append(s['ypos'].value())
        corner_bottom.append(s['ypos'].value() + s['bdheight'].value())
        z_List.append(s['z_order'].value())
    else:
        pass

if nuke.selectedNodes():
    for s in nuke.selectedNodes():
        node_xpos.append(s['xpos'].value())
        node_ypos.append(s['ypos'].value())
        
    
    x_max = max(node_xpos + corner_x)
    x_min = min(node_xpos)

    x_width = (float(x_max) - float(min(node_xpos + corner_x)))


    y_max = max(node_ypos)
    y_min = min(node_ypos)


    if not corner_bottom:
        corner_bottom.append(y_max - 1.0)
    cornerYMax = max(corner_bottom)

    if cornerYMax &gt; y_max:
        extra_y = abs((float(y_max) - float(cornerYMax)))
    else:
        extra_y = 0


    y_height =  abs((float(min(node_ypos + corner_y)) - float(y_max)) )

    if not corner_x:
        corner_x.append(x_max - 1.0)
    cornerXMin = min(corner_x)
    xMax = max(node_xpos)

    if cornerXMin &lt; xMax:
        extra_val = 100
    else:
        extra_val = 0


    print (&quot;cornerXMin: &quot; + str(cornerXMin))
    print (&quot;xMax: &quot; + str(xMax))
    print (&quot;corner_x: &quot; + str(corner_x))

    print (&quot;extra_val: &quot; + str(extra_val))



    if not z_List:
        z_List.append(0)
    z_Min = min(z_List)

    bd.setXpos(int(x_min) - 100)
    bd['bdwidth'].setValue(x_width + extra_val + 200)
    bd.setYpos(int(y_min) - 200)
    bd['bdheight'].setValue(y_height + extra_y + 300)
    bd['z_order'].setValue(z_Min - 1)
else:
    nuke.message('&lt;font color=orange&gt;&lt;b&gt;Select nodes first!')

###



print (nuke.selectedNode()['dependencies'])



node = nuke.selectedNode()
knob = nuke.nuke.Multiline_Eval_String_Knob('text', 'Text') 
#knob.setRange(1,10)
#knob.setValue(1)
node.addKnob(knob)


node = nuke.selectedNode()
knob = nuke.nuke.Double_Knob('scale3', 'Scgsdale') 
#knob.setRange(1,10)
#knob.setValue(1)
node.addKnob(knob)




####

# plate

bd = nuke.toNode('Backdrop_Adjust')

bd['tile_color'].setValue(1717987071)
bd['note'].setValue('PLATE')
bd['note_font_size'].setValue(102)
bd['note_color'].setValue('Orange')


# denoise

bd = nuke.toNode('Backdrop_Adjust')

bd['tile_color'].setValue(1717987071)
bd['note'].setValue('DENOISE')
bd['note_font_size'].setValue(82)
bd['note_color'].setValue('Orange')


# reference

bd = nuke.toNode('Backdrop_Adjust')

bd['tile_color'].setValue(1717987071)
bd['note'].setValue('REF')
bd['note_font_size'].setValue(82)
bd['note_color'].setValue('Orange')


# fg

bd = nuke.toNode('Backdrop_Adjust')

bd['tile_color'].setValue(3149642751)
bd['note'].setValue('FG')
bd['note_font_size'].setValue(72)
bd['note_color'].setValue('Black')


# bg

bd = nuke.toNode('Backdrop_Adjust')

bd['tile_color'].setValue(3149642751)
bd['note'].setValue('BG')
bd['note_font_size'].setValue(72)
bd['note_color'].setValue('Black')

# 3d

bd = nuke.toNode('Backdrop_Adjust')

bd['tile_color'].setValue(2576980479)
bd['note'].setValue('3D')
bd['note_font_size'].setValue(72)
bd['note_color'].setValue('Black')


# camera

bd = nuke.toNode('Backdrop_Adjust')

bd['tile_color'].setValue(2137407487)
bd['note'].setValue('CAMERA')
bd['note_font_size'].setValue(72)
bd['note_color'].setValue('Aqua')



# track

bd = nuke.toNode('Backdrop_Adjust')

bd['tile_color'].setValue(1916764159)
bd['note'].setValue('TRACK')
bd['note_font_size'].setValue(72)
bd['note_color'].setValue('Silver')



# matte

bd = nuke.toNode('Backdrop_Adjust')

bd['tile_color'].setValue(2134861567)
bd['note'].setValue('DMP')
bd['note_font_size'].setValue(72)
bd['note_color'].setValue('Fuchsia')


# color correct

bd = nuke.toNode('Backdrop_Adjust')

bd['tile_color'].setValue(1062830079)
bd['note'].setValue('GRADE')
bd['note_font_size'].setValue(72)
bd['note_color'].setValue('Silver')


# lens effect

bd = nuke.toNode('Backdrop_Adjust')

bd['tile_color'].setValue(1065320447)
bd['note'].setValue('LENS\nEFFECT')
bd['note_font_size'].setValue(72)
bd['note_color'].setValue('Yellow')


# grain

bd = nuke.toNode('Backdrop_Adjust')

bd['tile_color'].setValue(1717987071)
bd['note'].setValue('GRAIN')
bd['note_font_size'].setValue(72)
bd['note_color'].setValue('Aqua')


# key

bd = nuke.toNode('Backdrop_Adjust')

bd['tile_color'].setValue(1065310719)
bd['note'].setValue('KEY')
bd['note_font_size'].setValue(72)
bd['note_color'].setValue('Lime')


# roto

bd = nuke.toNode('Backdrop_Adjust')

bd['tile_color'].setValue(1920942079)
bd['note'].setValue('ROTO')
bd['note_font_size'].setValue(72)
bd['note_color'].setValue('Yellow')


nuke.pluginPath()

####################


node_xpos = []
node_ypos = []
z_List = []
if nuke.selectedNodes('BackdropNode'):
    sel_bd = nuke.selectedNodes('BackdropNode')
    for s in sel_bd:
        node_xpos.append(s['xpos'].value()+s['bdwidth'].value())
        node_ypos.append(s['ypos'].value()+s['bdheight'].value())
        z_List.append(s['z_order'].value())
    else:
        pass

if nuke.selectedNodes():
    for s in nuke.selectedNodes():
        node_xpos.append(s['xpos'].value())
        node_ypos.append(s['ypos'].value())

x_max = max(node_xpos)
x_min = min(node_xpos)

x_width = (float(x_max) - float(x_min))

y_max = max(node_ypos)
y_min = min(node_ypos)

y_height = (float(y_max) - float(y_min))

bd_this = nuke.nodes.Backdrop_Adjust()

bd_this.setXpos(int(x_min)-80)
bd_this['bdwidth'].setValue(int(x_width) + 240)
bd_this.setYpos(int(y_min)- 160)
bd_this['bdheight'].setValue(int(y_height) + 320)

print (&quot;\nx_max: &quot; + str(x_max))
print (&quot;x_min: &quot; + str(x_min))
print (&quot;x_width: &quot; + str(x_width))


print (&quot;y_max: &quot; + str(y_max))
print (&quot;y_min: &quot; + str(y_min))
print (&quot;y_height: &quot; + str(y_height))





############





node_xpos = []
node_ypos = []
z_List = []
bd_xpos = []
bd_ypos = []
if nuke.selectedNodes('BackdropNode'):
    sel_bd = nuke.selectedNodes('BackdropNode')
    for s in sel_bd:
        bd_xpos.append(s['xpos'].value())
        bd_xpos.append(s['xpos'].value()+s['bdwidth'].value())
        bd_ypos.append(s['ypos'].value())
        bd_ypos.append(s['ypos'].value()+s['bdheight'].value())
        z_List.append(s['z_order'].value())
    else:
        pass

if nuke.selectedNodes():
    for s in nuke.selectedNodes():
        node_xpos.append(s['xpos'].value())
        node_ypos.append(s['ypos'].value())


x_max = max(node_xpos)
x_min = min(node_xpos)

y_max = max(node_ypos)
y_min = min(node_ypos)


# calculating in the node's size if the lowest right corner isn't a Backdrop but a node
if not bd_xpos:
    bd_xpos.append(x_min)
    bd_ypos.append(y_max)

if bd_xpos:
    max_bd_xpos = max(bd_xpos)
    min_bd_xpos = min(bd_xpos)

    max_bd_ypos = max(bd_ypos)
    min_bd_ypos = min(bd_ypos)

    if max_bd_xpos &gt; x_max:    
        x_extra = 0
    else:
        x_extra = 80


    if max_bd_ypos &gt; y_max:    
        y_extra = 0
    else:
        y_extra = 30

else:
    pass



print (&quot;y_extra: &quot; + str(y_extra))

print (&quot;x_extra: &quot; + str(x_extra))


x_max = max(node_xpos + bd_xpos)
x_min = min(node_xpos + bd_xpos)

print (&quot;x_max: &quot; + str(x_max))
print (&quot;x_min: &quot; + str(x_min))


x_width = (float(x_max) - float(x_min))

y_max = max(node_ypos + bd_ypos)
y_min = min(node_ypos + bd_ypos)

y_height = (float(y_max) - float(y_min))


if not z_List:
    z_List.append(0)
z_Min = min(z_List)


bd_this = nuke.nodes.Backdrop_Adjust()

bd_this.setXpos(int(x_min) - 100)
bd_this['bdwidth'].setValue(int(x_width)+ int(x_extra) + 200)
bd_this.setYpos(int(y_min) - int(y_extra) - 100)
bd_this['bdheight'].setValue(int(y_height) + int(y_extra) + 200)
bd_this['z_order'].setValue(z_Min - 1)








bd_this.setXpos(int(x_min) - int(x_extra) - 100)
bd_this['bdwidth'].setValue(int(x_width) + int(x_extra * 2) + 200)





bd = nuke.toNode('Backdrop_Adjust')

bd['bdwidth'].setValue(500)
bd['bdheight'].setValue(500)


m = nuke.toNode('Blur14')
print (m.screenHeight())

###

node_xpos = []
node_ypos = []
node_scrWidth = []
node_scrHeight = []
if nuke.selectedNodes():
    for s in nuke.selectedNodes():
        node_xpos.append(s['xpos'].value())
        node_ypos.append(s['ypos'].value())
        node_scrWidth.append(s.screenWidth())
        node_scrHeight.append(s.screenHeight())

print (&quot;\nnode_xpos: &quot; + str(node_xpos))
print (&quot;node_ypos: &quot; + str(node_ypos))
print (&quot;node_scrWidth: &quot; + str(node_scrWidth))
print (&quot;node_scrHeight: &quot; + str(node_scrHeight))

node_xpos_width = [sum(x) for x in zip(node_xpos, node_scrWidth)]

print (node_xpos_width)


####

nodes = nuke.selectedNodes()

# Calculate bounds for the backdrop node.
bdX = min([node.xpos() for node in nodes])
bdY = min([node.ypos() for node in nodes])
bdW = max([node.xpos() + node.screenWidth() for node in nodes]) - bdX
bdH = max([node.ypos() + node.screenHeight() for node in nodes]) - bdY

# Expand the bounds to leave a little border. Elements are offsets for left, top, right and bottom edges respectively
left, top, right, bottom = (-150, -200, 150, 150)
bdX += left
bdY += top
bdW += (right - left)
bdH += (bottom - top)

n = nuke.createNode(&quot;BackdropNode&quot;, inpanel=False)
n[&quot;xpos&quot;].setValue(bdX)
n[&quot;bdwidth&quot;].setValue(bdW)
n[&quot;ypos&quot;].setValue(bdY)
n[&quot;bdheight&quot;].setValue(bdH)



###################


oldText = nuke.toNode(&quot;Text2&quot;)

oldText_output = oldText[&quot;output&quot;].value()
oldText_premult = oldText[&quot;premult&quot;].value()
oldText_cliptype = oldText[&quot;cliptype&quot;].value()
oldText_replace = oldText[&quot;replace&quot;].value()
oldText_invert = oldText[&quot;invert&quot;].value()
oldText_opacity = oldText[&quot;opacity&quot;].value()
oldText_maskChannelMask = oldText[&quot;maskChannelMask&quot;].value()
oldText_maskChannelInput = oldText[&quot;maskChannelInput&quot;].value()
oldText_inject = oldText[&quot;inject&quot;].value()
oldText_invert_mask = oldText[&quot;invert_mask&quot;].value()
oldText_message = oldText[&quot;message&quot;].value()
#size - font_size
oldText_size = oldText[&quot;size&quot;].value()
#kerning - tracking
oldText_kerning = oldText[&quot;kerning&quot;].value()
oldText_leading = oldText[&quot;leading&quot;].value()
oldText_xjustify = oldText[&quot;xjustify&quot;].value()
oldText_yjustify = oldText[&quot;yjustify&quot;].value()
oldText_box = oldText[&quot;box&quot;].value()

oldText_translate = oldText[&quot;translate&quot;].value()
oldText_rotate = oldText[&quot;rotate&quot;].value()
oldText_scale = oldText[&quot;scale&quot;].value()
oldText_skewX = oldText[&quot;skewX&quot;].value()
oldText_skewY = oldText[&quot;skewY&quot;].value()
oldText_skew_order = oldText[&quot;skew_order&quot;].value()
oldText_center = oldText[&quot;center&quot;].value()

oldText_ramp = oldText[&quot;ramp&quot;].value()
oldText_color = oldText[&quot;color&quot;].value()

oldText_label = oldText[&quot;label&quot;].value()
oldText_note_font_size = oldText[&quot;note_font_size&quot;].value()
oldText_note_font_color = oldText[&quot;note_font_color&quot;].value()
oldText_hide_input = oldText[&quot;hide_input&quot;].value()
oldText_postage_stamp = oldText[&quot;postage_stamp&quot;].value()
oldText_disable = oldText[&quot;disable&quot;].value()

#print (oldText_output)

#newText = nuke.toNode(&quot;Text1&quot;)
#newText[&quot;output&quot;].setValue(oldText_output)
#newText[&quot;message&quot;].setValue(oldText_message)


newText = nuke.createNode(&quot;Text2&quot;)

newText[&quot;output&quot;].setValue(oldText_output)
newText[&quot;premult&quot;].setValue(oldText_premult)
newText[&quot;cliptype&quot;].setValue(oldText_cliptype)
newText[&quot;replace&quot;].setValue(oldText_replace)
newText[&quot;invert&quot;].setValue(oldText_invert)
newText[&quot;opacity&quot;].setValue(oldText_opacity)
newText[&quot;maskChannelMask&quot;].setValue(oldText_maskChannelMask)
newText[&quot;maskChannelInput&quot;].setValue(oldText_maskChannelInput)
newText[&quot;inject&quot;].setValue(oldText_inject)
newText[&quot;invert_mask&quot;].setValue(oldText_invert_mask)
newText[&quot;message&quot;].setValue(oldText_message)
#size - font_size
newText[&quot;font_size&quot;].setValue(oldText_size)
newText[&quot;global_font_scale&quot;].setValue(0.6)
#kerning - tracking
newText[&quot;tracking&quot;].setValue(oldText_kerning)
newText[&quot;leading&quot;].setValue(oldText_leading)
newText[&quot;xjustify&quot;].setValue(oldText_xjustify)
newText[&quot;yjustify&quot;].setValue(oldText_yjustify)
newText[&quot;box&quot;].setValue(oldText_box)


newText[&quot;translate&quot;].setValue(oldText_translate)
newText[&quot;rotate&quot;].setValue(oldText_rotate)
newText[&quot;scale&quot;].setValue(oldText_scale)
newText[&quot;skewX&quot;].setValue(oldText_skewX)
newText[&quot;skewY&quot;].setValue(oldText_skewY)
newText[&quot;skew_order&quot;].setValue(oldText_skew_order)
newText[&quot;center&quot;].setValue(oldText_center)

newText[&quot;group_animations&quot;].setValue(0)


newText[&quot;ramp&quot;].setValue(oldText_ramp)
newText[&quot;color&quot;].setValue(oldText_color)

newText[&quot;label&quot;].setValue(oldText_label)
newText[&quot;note_font_size&quot;].setValue(oldText_note_font_size)
newText[&quot;note_font_color&quot;].setValue(oldText_note_font_color)
newText[&quot;hide_input&quot;].setValue(oldText_hide_input)
newText[&quot;postage_stamp&quot;].setValue(oldText_postage_stamp)
newText[&quot;disable&quot;].setValue(oldText_disable)









oldText = nuke.toNode(&quot;Text4&quot;)

oldText_output = oldText[&quot;group_animations&quot;].value()

print (oldText_output)


### DEALING W KNOBS ###

# https://github.com/tianlunjiang/NukeModdingGuide/blob/master/_python/NukeModule.md

# https://learn.foundry.com/nuke/developers/120/pythonreference/nuke.KnobType-class.html

# https://gist.github.com/plasmax/bde3bd503fb6f496c7bb6aea4652e3ef

node = nuke.toNode('NoOp3')
knob = nuke.LookupCurves_Knob('lookup', 'lookup') 
#knob.setRange(1,10)
node.addKnob(knob)




index = nuke.tcl('knob', '-t', knob.node().name() + '.' + knob.name() )

nuke.knob(knobname, type = True) # Returns an int with the knob ID


knob = nuke.toNode('NoOp3').knob('functions').KnobType()
print(knob)




#1
knob = nuke.String_Knob('fRange', 'Track Range')

#3
knob = nuke.Int_Knob('pointNumber', 'Point Number')

#4
knob = nuke.Enumeration_Knob('element', 'element', ['Shapes', 'Strokes'])

#6
knob = nuke.Boolean_Knob('Boolean', '6_Boolean')

#7
knob = nuke.nuke.Double_Knob('Double', '7_Double') 
#knob.setRange(1,10)

#11
knob = nuke.nuke.Channel_Knob('Channel', '11_Channel') 

#15
knob = nuke.BBox_Knob('BBox','15_BBox')

#19
knob = nuke.AColor_Knob('AColor','19_AColor')

#20
knob = nuke.Tab_Knob('custom_tab', 'Custom Tab')

#22
knob = nuke.PyScript_Knob('update', 'Update')

#26
knob = nuke.Text_Knob('warning', '&lt;span style=&quot;color:red&quot;&gt;invalid index&lt;/span&gt;')

#31
knob = nuke.nuke.Box3_Knob('Box3', '31_Box3') 

#40
knob = nuke.ColorChip_Knob('ColorChip','10_ColorChip')

#41
knob = nuke.Link_Knob('test')
knob.setLink( 'root.Blur1.size' )

#43
knob = nuke.Multiline_Eval_String_Knob('info', 'Found')

#68
knob = nuke.nuke.CascadingEnumeration_Knob('CascadingEnum', '68_CascadingEnum', range(3))

#78
knob = nuke.Array_Knob('Array','78_Array')


CTrans['scale'].setSingleValue(False)
CTrans['scale'].setExpression(('Trans_COPY1.scale.w'),0)
CTrans['scale'].setExpression(('Trans_COPY1.scale.h'),1)

typeKnob.value()



# all knobs' name
node = nuke.selectedNode()
for i in range(node.numKnobs()):
    knob = node.knob(i)
    print knob.name()




knob = nuke.toNode('NoOp3').knob('BBox').KnobType()





nuke.pluginPath()


knob = nuke.toNode('NoOp3').knob('scale')

# https://pastebin.com/zNCUykk9
def getKnobType(knob):
    ''' Return a string that identifies the type of knob.
        Useful to distinguish between different types
        of Array and Enumeration knobs that are
        serialized with a different knob ID in tcl.
    '''  
    import re
 
    # Use knob.Class() and return early if Class() is not Array_Knob or Enumeration_Knob
    if knob.Class() not in ['Array_Knob', 'Enumeration_Knob']: 
        return knob.Class()
 
    knobName = knob.fullyQualifiedName()
    knobID = nuke.knob(knobName, type = True)
 
    # Get dict of knobtypes
    knobIDs = dict([(v,k) for (k,v) in nuke.KnobType.__dict__.items()])  
 
    # Also use knob.Class() if ID is not found in KnobTypes
    if not (knobID in knobIDs):
        return knob.Class()
 
    #return type as defined in KnobTypes, with some reformatting
    return re.sub( '(?&lt;!^)(?=[A-Z])', '_',  knobIDs[knobID].lstrip('e'))

getKnobType()



#### Print all nodes` name in a script in alphabetical order ####
list = []
for s in nuke.allNodes():
    list.append(s['name'].value())
sortedlist = sorted(list)
print (', '.join(sortedlist))









import os
for k,v in sorted(os.environ.items()):
    print k,&quot;: &quot;,v



















</script>

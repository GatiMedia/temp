#import random
#def randomColor():
#   color = random.randrange(0, 0xffffffff)
#   font = random.randrange(0, 100)
#   n = nuke.thisNode()
#   n['tile_color'].setValue(color)
#   n['note_font_size'].setValue(font)
#
#sel = nuke.selectedNodes()
#for n in sel:
#   n['knobChanged'].setValue('randomColor()')

#####

nuke.pluginPath()

#####

import webbrowser

sel = nuke.selectedNode()

site = 'https://imgur.com/search/score/?q=cat'

name = nuke.PyScript_Knob('button', 'Click', "webbrowser.open(site)")

sel.addKnob(name)

#####

merge_nodes = []
dictionary = {}

for node in nuke.allNodes('Merge2'):
    merge_nodes.append(node)

for i in merge_nodes:
    dictionary[i.name()] = i.knob('operation').value()

print dictionary.items()

######


iRepeats = 5
bfirstLoop = True

nDot = nuke.nodes.Dot()
w = nuke.toNode('Transform24')
b = nuke.toNode('Blur2')
nDot.setInput(0, w)

for i in range(iRepeats):
    nTrans = nuke.nodes.Transform(name = "t" + str(i))
    nMerge = nuke.nodes.Merge2(name = "m" + str(i))
    nMerge.setInput(1, nTrans)

    
    if bfirstLoop:
        bfirstLoop = False
        nTrans.setInput(0, nDot)
        nMerge.setInput(0, nDot)
    else:
        nTrans.setInput(0, nPrevMerge)
        nMerge.setInput(0, nPrevMerge)
        
    nPrevMerge = nMerge

p = nuke.toNode(

####

m = nuke.toNode('Transform22')
m.knob('invert_matrix').setExpression('Transform23.invert_matrix')

####

w = nuke.toNode('Transform25')
v = nuke.createNode('Transform')
p = nuke.createNode('Merge2')
v.setInput(0, v)
p.setInput(0, w)

####


ProxyNum = nuke.toNode('PROXY_MAIN').knob('copy1').getValue()

iRepeats = int(ProxyNum)
bfirstLoop = True

# Main Transform for Copy1
w = nuke.toNode('Trans_COPY1')

# Last Merge connected to this
b = nuke.toNode('Blur2')

# Dot would be connected to this and allows toggle between original and modified source 
s = nuke.toNode('Switch1')

nDot = nuke.nodes.Dot()
nDot.setInput(0, s)

for i in range(iRepeats):
    CTrans = nuke.nodes.Transform(name = "t" + str(i))
    CTrans.knob('translate').setExpression('Trans_COPY1.translate')
    CTrans.knob('rotate').setExpression('Trans_COPY1.rotate')
    CTrans.knob('scale').setExpression('Trans_COPY1.scale')
    CTrans.knob('skewX').setExpression('Trans_COPY1.skewX')
    CTrans.knob('skewY').setExpression('Trans_COPY1.skewY')
    CTrans.knob('skew_order').setExpression('Trans_COPY1.skew_order')
    CTrans.knob('center').setExpression('Trans_COPY1.center')
    CTrans.knob('invert_matrix').setExpression('Trans_COPY1.invert_matrix')
    CTrans.knob('filter').setExpression('Trans_COPY1.filter')
    nMerge = nuke.nodes.Merge2(name = "m" + str(i))
    nMerge.knob('also_merge').setValue('all')
    nMerge.setInput(1, CTrans)
    
    if bfirstLoop:
        bfirstLoop = False
        CTrans.setInput(0, nDot)
        nMerge.setInput(0, nDot)
    else:
        CTrans.setInput(0, nPrevMerge)
        nMerge.setInput(0, nPrevMerge)

    nPrevMerge = nMerge

MNum = int(iRepeats) - 1

p = nuke.toNode("m" + str(MNum))

b.setInput(0, p)


###############







#####Code for GM_Repeater#####


Rep = nuke.toNode('GM_ShapeRepeater')

Rep.begin()

nuke.toNode('PROXY_MAIN1').knob('knobChanged').setValue("""
m = nuke.thisNode()
kc = nuke.thisKnob()
if kc.name() in ["copy1"]:
    for n in nuke.allNodes():
        if "static" not in n['label'].getValue():
            nuke.delete(n)
    
    iRep = m.knob('copy1').getValue()
    iRepeats = int(iRep)-1
    bfirstLoop = True
    
    # Main Transform for Copy1
    w = nuke.toNode('Trans_COPY1')
    
    # Last Merge connected to this
    b = nuke.toNode('COPIES1_end')
    
    # Dot would be connected to this and allows toggle between original and modified source 
    s = nuke.toNode('Switch1')
    
    nDot = nuke.nodes.Dot()
    nDot.setInput(0, s)
    
    if (iRepeats+1) >= 2: 
    
        for i in range(iRepeats):
            CTrans = nuke.nodes.Transform(name = "t" + str(i))
            CTrans.knob('translate').setExpression('Trans_COPY1.translate')
            CTrans.knob('rotate').setExpression('Trans_COPY1.rotate')
            CTrans.knob('scale').setExpression('Trans_COPY1.scale')
            CTrans.knob('skewX').setExpression('Trans_COPY1.skewX')
            CTrans.knob('skewY').setExpression('Trans_COPY1.skewY')
            CTrans.knob('skew_order').setExpression('Trans_COPY1.skew_order')
            CTrans.knob('center').setExpression('Trans_COPY1.center')
            CTrans.knob('invert_matrix').setExpression('Trans_COPY1.invert_matrix')
            CTrans.knob('filter').setExpression('Trans_COPY1.filter')
            CTrans.knob('motionblur').setExpression('Trans_COPY1.motionblur')
            CTrans.knob('shutter').setExpression('Trans_COPY1.shutter')
            CTrans.knob('shutteroffset').setValue(0)
            nMerge = nuke.nodes.Merge2(name = "m" + str(i))
            nMerge.knob('also_merge').setValue('all')
            nMerge.setInput(1, CTrans)
            
            if bfirstLoop:
                bfirstLoop = False
                CTrans.setInput(0, nDot)
                nMerge.setInput(0, nDot)
            else:
                CTrans.setInput(0, nPrevTrans)
                nMerge.setInput(0, nPrevMerge)
        
            nPrevMerge = nMerge
            nPrevTrans = CTrans
        
        MNum = int(iRepeats) - 1
        
        p = nuke.toNode("m" + str(MNum))
        
        b.setInput(0, p)
    else:
        b.setInput(0, nDot)
""")


Rep.end()




####

((1/(M-1))*(M-m)) + ( ( 1- ((1/(M-1))*(M-m)) ) * X )

RepMax = int(iRep)

RepNum = int(i)

((1/(RepMax-1))*(RepMax-RepNum)) + ( ( 1- ((1/(RepMax-1))*(RepMax-RepNum)) ) * Trans_COPY1_proxy.fadeout )



#####Code for GM_ShapeRepeater#####


Rep = nuke.toNode('GM_ShapeRepeater1')

Rep.begin()

nuke.toNode('PROXY_MAIN1').knob('knobChanged').setValue("""
m = nuke.thisNode()
kc = nuke.thisKnob()
if kc.name() in ["copy1"]:
    for n in nuke.allNodes():
        if "static" not in n['label'].getValue():
            nuke.delete(n)
    
    iRep = m.knob('copy1').getValue()
    iRepeats = int(iRep)-1
    RepMax = int(iRep)
    bfirstLoop = True
    
    # Main Transform for Copy1
    w = nuke.toNode('Trans_COPY1')
    
    # Last Merge connected to this
    b = nuke.toNode('COPIES1_end')
    
    # Dot would be connected to this and allows toggle between original and modified source 
    s = nuke.toNode('Switch1')
    
    nDot = nuke.nodes.Dot()
    nDot.setInput(0, s)

    nMult = nuke.toNode('mu1t2_1')
    
    if (iRepeats+1) >= 2: 
    
        for i in range(iRepeats):
            RepNum = int(i)+1
            RepNum2 = int(i)+2
            nMult.knob('ReMax').setValue( RepMax )
            nMult.knob('value').setExpression('((1/(ReMax-1))*(ReMax-(ReMax-ReNum))) + ( ( 1- ((1/(ReMax-1))*(ReMax-(ReMax-ReNum))) ) * Trans_COPY1_proxy.fadein )')
            CTrans = nuke.nodes.Transform(name = "t" + str(i))
            CTrans.knob('translate').setExpression('Trans_COPY1.translate')
            CTrans.knob('rotate').setExpression('Trans_COPY1.rotate')
            CTrans.knob('scale').setExpression('Trans_COPY1.scale')
            CTrans.knob('skewX').setExpression('Trans_COPY1.skewX')
            CTrans.knob('skewY').setExpression('Trans_COPY1.skewY')
            CTrans.knob('skew_order').setExpression('Trans_COPY1.skew_order')
            CTrans.knob('center').setExpression('Trans_COPY1.center')
            CTrans.knob('invert_matrix').setExpression('Trans_COPY1.invert_matrix')
            CTrans.knob('filter').setExpression('Trans_COPY1.filter')
            CTrans.knob('motionblur').setExpression('Trans_COPY1.motionblur')
            CTrans.knob('shutter').setExpression('Trans_COPY1.shutter')
            CTrans.knob('shutteroffset').setValue(0)
            CMult1 = nuke.nodes.Multiply(name = "mu1_" + str(i))
            k = nuke.Int_Knob('ReMax', 'ReMax' )
            k2 = nuke.Int_Knob('ReNum', 'ReNum' )
            CMult1.addKnob(k)
            CMult1.addKnob(k2)
            CMult1.knob('ReMax').setValue( RepMax )
            CMult1.knob('ReNum').setValue( RepNum )
            CMult1.knob('value').setExpression('((1/(ReMax-1))*(ReMax-ReNum)) + ( ( 1- ((1/(ReMax-1))*(ReMax-ReNum)) ) * Trans_COPY1_proxy.fadeout )')
            CMult1.setInput(0, CTrans)
            CMult2 = nuke.nodes.Multiply(name = "mu1t2_" + str(RepNum2))
            k = nuke.Int_Knob('ReMax', 'ReMax' )
            k2 = nuke.Int_Knob('ReNum', 'ReNum' )
            CMult2.addKnob(k)
            CMult2.addKnob(k2)
            CMult2.knob('ReMax').setValue( RepMax )
            CMult2.knob('ReNum').setValue( RepNum )
            CMult2.knob('value').setExpression('((1/(ReMax-1))*(ReMax-(ReMax-ReNum))) + ( ( 1- ((1/(ReMax-1))*(ReMax-(ReMax-ReNum))) ) * Trans_COPY1_proxy.fadein )')
            CMult2.setInput(0, CMult1)
            nMerge = nuke.nodes.Merge2(name = "m" + str(i))
            nMerge.knob('also_merge').setValue('all')
            nMerge.setInput(1, CMult2)
            
            if bfirstLoop:
                bfirstLoop = False
                CTrans.setInput(0, nDot)
                CMult1.setInput(0, CTrans)
                CMult2.setInput(0, CMult1)
                nMerge.setInput(0, nMult)
            else:
                CTrans.setInput(0, nPrevTrans)
                CMult1.setInput(0, CTrans)
                CMult2.setInput(0, CMult1)
                nMerge.setInput(0, nPrevMerge)
 
            nPrevMerge = nMerge
            nPrevTrans = CTrans
            nPrevMult1 = CMult1
            nPrevMult2 = CMult2
        
        MNum = int(iRepeats) - 1
        
        p = nuke.toNode("m" + str(MNum))
        
        b.setInput(0, p)


    else:
        b.setInput(0, nDot)
""")


Rep.end()


##

m = nuke.toNode('ColorWheel1')

n = nuke.nodes.Multiply(name = "t")

n.setInput(0, m)


m = nuke.toNode('Blur1')
k = nuke.Int_Knob('userKnob', 'userKnob', )
m.addKnob(k)
m.knob('userKnob').setValue(int(95))

((1/(ReMax-1))*(ReMax-ReNum)) + ( ( 1- ((1/(ReMax-1))*(ReMax-ReNum)) ) * Trans_COPY1_proxy.fadeout )





####

nuke.pluginPath()

####

m = nuke.toNode('Merge9')

nodes = nuke.selectedNodes()

for node in nodes:
    node.setInput(0, m)

#####

m = nuke.toNode('Merge9')
x = range(0, 2)
nodes = nuke.selectedNodes()

m.setInput(0, nodes)



a = nuke.createNode('Merge9')
b = nuke.selectedNodes()
x=0
for i in b:
    if x==2:
        x+=1
    continue
        a.setInput(x,i)
        x+=1



m = nuke.selectedNodes()

for node in m:
    node.knob('colorspace').setValue(2)


####

m = nuke.toNode('Transform4')
m['scale'].setSingleValue(False)
m['scale'].setExpression(('Transform12.scale.w'),0)
m['scale'].setExpression(('Transform12.scale.h'),1)


k = nuke.toNode('Transform12')
p = k.knob('scale').getValue()
l = k.knob('scale').value()
print type(p)

m['scale'].setValue((-5, 5))


#####


#####Code for GM_ShapeRepeater#####


Rep = nuke.toNode('GM_ShapeRepeater')

Rep.begin()

nuke.toNode('PROXY_MAIN1').knob('knobChanged').setValue("""
m = nuke.thisNode()
kc = nuke.thisKnob()
if kc.name() in ["copy1"]:
    for n in nuke.allNodes():
        if "static" not in n['label'].getValue():
            nuke.delete(n)
    
    iRep = m.knob('copy1').getValue()
    iRepeats = int(iRep)-1
    RepMax = int(iRep)
    bfirstLoop = True
    
    # Main Transform for Copy1
    w = nuke.toNode('Trans_COPY1')
    
    # Last Merge connected to this
    b = nuke.toNode('COPIES1_end')
    
    # Dot would be connected to this and allows toggle between original and modified source 
    s = nuke.toNode('Switch1')
    
    nDot = nuke.nodes.Dot()
    nDot.setInput(0, s)

    nMult = nuke.toNode('mu1t2_1')
    
    if (iRepeats+1) >= 2: 
    
        for i in range(iRepeats):
            RepNum = int(i)+1
            RepNum2 = int(i)+2
            nMult.knob('ReMax').setValue( RepMax )
            nMult.knob('value').setExpression('((1/(ReMax-1))*(ReMax-(ReMax-ReNum))) + ( ( 1- ((1/(ReMax-1))*(ReMax-(ReMax-ReNum))) ) * Trans_COPY1_proxy.fadein )')
            CTrans = nuke.nodes.Transform(name = "t" + str(i))
            CTrans.knob('translate').setExpression('Trans_COPY1.translate')
            CTrans.knob('rotate').setExpression('Trans_COPY1.rotate')
            CTrans['scale'].setSingleValue(False)
            CTrans['scale'].setExpression(('Trans_COPY1.scale.w'),0)
            CTrans['scale'].setExpression(('Trans_COPY1.scale.h'),1)
            CTrans.knob('skewX').setExpression('Trans_COPY1.skewX')
            CTrans.knob('skewY').setExpression('Trans_COPY1.skewY')
            CTrans.knob('skew_order').setExpression('Trans_COPY1.skew_order')
            CTrans.knob('center').setExpression('Trans_COPY1.center')
            CTrans.knob('invert_matrix').setExpression('Trans_COPY1.invert_matrix')
            CTrans.knob('filter').setExpression('Trans_COPY1.filter')
            CTrans.knob('motionblur').setExpression('Trans_COPY1.motionblur')
            CTrans.knob('shutter').setExpression('Trans_COPY1.shutter')
            CTrans.knob('shutteroffset').setValue(0)
            CMult1 = nuke.nodes.Multiply(name = "mu1_" + str(i))
            k = nuke.Int_Knob('ReMax', 'ReMax' )
            k2 = nuke.Int_Knob('ReNum', 'ReNum' )
            CMult1.addKnob(k)
            CMult1.addKnob(k2)
            CMult1.knob('ReMax').setValue( RepMax )
            CMult1.knob('ReNum').setValue( RepNum )
            CMult1.knob('value').setExpression('((1/(ReMax-1))*(ReMax-ReNum)) + ( ( 1- ((1/(ReMax-1))*(ReMax-ReNum)) ) * Trans_COPY1_proxy.fadeout )')
            CMult1.setInput(0, CTrans)
            CMult2 = nuke.nodes.Multiply(name = "mu1t2_" + str(RepNum2))
            k = nuke.Int_Knob('ReMax', 'ReMax' )
            k2 = nuke.Int_Knob('ReNum', 'ReNum' )
            CMult2.addKnob(k)
            CMult2.addKnob(k2)
            CMult2.knob('ReMax').setValue( RepMax )
            CMult2.knob('ReNum').setValue( RepNum )
            CMult2.knob('value').setExpression('((1/(ReMax-1))*(ReMax-(ReMax-ReNum))) + ( ( 1- ((1/(ReMax-1))*(ReMax-(ReMax-ReNum))) ) * Trans_COPY1_proxy.fadein )')
            CMult2.setInput(0, CMult1)
            nMerge = nuke.nodes.Merge2(name = "m" + str(i))
            nMerge.knob('also_merge').setValue('all')
            nMerge.setInput(1, CMult2)
            
            if bfirstLoop:
                bfirstLoop = False
                CTrans.setInput(0, nDot)
                CMult1.setInput(0, CTrans)
                CMult2.setInput(0, CMult1)
                nMerge.setInput(0, nMult)
            else:
                CTrans.setInput(0, nPrevTrans)
                CMult1.setInput(0, CTrans)
                CMult2.setInput(0, CMult1)
                nMerge.setInput(0, nPrevMerge)
 
            nPrevMerge = nMerge
            nPrevTrans = CTrans
            nPrevMult1 = CMult1
            nPrevMult2 = CMult2
        
        MNum = int(iRepeats) - 1
        
        p = nuke.toNode("m" + str(MNum))
        
        b.setInput(0, p)


    else:
        b.setInput(0, nDot)
""")


Rep.end()

####

#####Code for GM_Repeater#####


Rep = nuke.toNode('GM_Repeater')

Rep.begin()

nuke.toNode('PROXY').knob('knobChanged').setValue("""
m = nuke.thisNode()
kc = nuke.thisKnob()
if kc.name() in ["copies"]:
    for n in nuke.allNodes():
        if "static" not in n['label'].getValue():
            nuke.delete(n)
    
    iRep = m.knob('copies').getValue()
    iRepeats = int(iRep)-1
    RepMax = int(iRep)
    bfirstLoop = True
    
    # Main Transform for Copy1
    w = nuke.toNode('Trans_COPY1')
    
    # Last Merge connected to this
    b = nuke.toNode('COPIES1_end')
    
    # Dot would be connected to this and allows toggle between original and modified source 
    s = nuke.toNode('Switch1')
    
    nDot = nuke.nodes.Dot()
    nDot.setInput(0, s)

    nMult = nuke.toNode('mu1t2_1')
    
    if (iRepeats+1) >= 2: 
    
        for i in range(iRepeats):
            RepNum = int(i)+1
            RepNum2 = int(i)+2
            nMult.knob('ReMax').setValue( RepMax )
            nMult.knob('value').setExpression('((1/(ReMax-1))*(ReMax-(ReMax-ReNum))) + ( ( 1- ((1/(ReMax-1))*(ReMax-(ReMax-ReNum))) ) * Trans_COPY1_proxy.fadein )')
            CTrans = nuke.nodes.Transform(name = "t" + str(i))
            CTrans.knob('translate').setExpression('Trans_COPY1.translate')
            CTrans.knob('rotate').setExpression('Trans_COPY1.rotate')
            CTrans['scale'].setSingleValue(False)
            CTrans['scale'].setExpression(('Trans_COPY1.scale.w'),0)
            CTrans['scale'].setExpression(('Trans_COPY1.scale.h'),1)
            CTrans.knob('skewX').setExpression('Trans_COPY1.skewX')
            CTrans.knob('skewY').setExpression('Trans_COPY1.skewY')
            CTrans.knob('skew_order').setExpression('Trans_COPY1.skew_order')
            CTrans.knob('center').setExpression('Trans_COPY1.center')
            CTrans.knob('invert_matrix').setExpression('Trans_COPY1.invert_matrix')
            CTrans.knob('filter').setExpression('Trans_COPY1.filter')
            CTrans.knob('motionblur').setExpression('Trans_COPY1.motionblur')
            CTrans.knob('shutter').setExpression('Trans_COPY1.shutter')
            CTrans.knob('shutteroffset').setValue(0)
            CMult1 = nuke.nodes.Multiply(name = "mu1_" + str(i))
            k = nuke.Int_Knob('ReMax', 'ReMax' )
            k2 = nuke.Int_Knob('ReNum', 'ReNum' )
            CMult1.addKnob(k)
            CMult1.addKnob(k2)
            CMult1.knob('ReMax').setValue( RepMax )
            CMult1.knob('ReNum').setValue( RepNum )
            CMult1.knob('value').setExpression('((1/(ReMax-1))*(ReMax-ReNum)) + ( ( 1- ((1/(ReMax-1))*(ReMax-ReNum)) ) * Trans_COPY1_proxy.fadeout )')
            CMult1.setInput(0, CTrans)
            CMult2 = nuke.nodes.Multiply(name = "mu1t2_" + str(RepNum2))
            k = nuke.Int_Knob('ReMax', 'ReMax' )
            k2 = nuke.Int_Knob('ReNum', 'ReNum' )
            CMult2.addKnob(k)
            CMult2.addKnob(k2)
            CMult2.knob('ReMax').setValue( RepMax )
            CMult2.knob('ReNum').setValue( RepNum )
            CMult2.knob('value').setExpression('((1/(ReMax-1))*(ReMax-(ReMax-ReNum))) + ( ( 1- ((1/(ReMax-1))*(ReMax-(ReMax-ReNum))) ) * Trans_COPY1_proxy.fadein )')
            CMult2.setInput(0, CMult1)
            nMerge = nuke.nodes.Merge2(name = "m" + str(i))
            nMerge.knob('also_merge').setValue('all')
            nMerge.knob('operation').setExpression('Merge_Proxy.operation1')
            nMerge.setInput(1, CMult2)
            
            if bfirstLoop:
                bfirstLoop = False
                CTrans.setInput(0, nDot)
                CMult1.setInput(0, CTrans)
                CMult2.setInput(0, CMult1)
                nMerge.setInput(0, nMult)
            else:
                CTrans.setInput(0, nPrevTrans)
                CMult1.setInput(0, CTrans)
                CMult2.setInput(0, CMult1)
                nMerge.setInput(0, nPrevMerge)
 
            nPrevMerge = nMerge
            nPrevTrans = CTrans
            nPrevMult1 = CMult1
            nPrevMult2 = CMult2
        
        MNum = int(iRepeats) - 1
        
        p = nuke.toNode("m" + str(MNum))
        
        b.setInput(0, p)
    else:
        b.setInput(0, nDot)

""")


Rep.end()



### GBK PYTHON SNIPPETS 101 ###


### FIRST STEP ###


print ("Hello World!")


### USING VARIABLE ###


name = 'Attila'
age = '30'
country = 'Hungary'
print ('Hello ' + name + '! I am ' + age + '. I am from ' + country)

name = 'Attila'
age = 30
country = 'Hungary'
print("Hello %s! I am %d. I am from %s." % (name, age, country))

# %d will truncate to integer, %s will maintain formatting, %f will print as float and %g is used for generic number

name = 'Attila'
age = 30
country = 'Hungary'
print("Hello {}! I am {}. I am from {}.".format(name, age, country))

### TYPE CONVERSION ###


# Interger - int(x)

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


nuke.createNode("Blur")

# Can check node's Class with the `i` hotkey
nuke.createNode("Tracker4")

# Can call nodes that are removed from GUI
nuke.createNode("Blocky")

# Set a value
nuke.createNode("Blur")['size'].setValue(80)

# Set multiple values using a variable
m = nuke.createNode("Blur")
m['channels'].setValue("rgb")
m['size'].setValue(50)
m['mix'].setValue(.5)
m['label'].setValue("Size: [value size]\nChannels: [value channels]\nMix: [value mix]")

# Creating node for scripting
nuke.nodes.Blur()

nuke.nodes.Blur(mix=.5,size=10)


### GETTING KNOB VALUE ###
## Functions: toNode, value, getValue, knob ###


# Calling knobs as list items
nuke.toNode('Blur1')["channels"].value()

# Calling knobs with a function
nuke.toNode('Blur1').knob("channels").value()

nuke.toNode('Blur1')["filter"].getValue()


### SETTING KNOB VALUE ###
## Functions: setValue ##

# Setting single value
nuke.toNode('Blur1')["size"].setValue(10)

# Setting multiple values
b = nuke.toNode('Blur1')
b["size"].setValue(20)
b["mix"].setValue(.8)
b["filter"].setValue(0)
b["channels"].setValue("rgb")



### SETTING EXPRESSION VALUE ###
## Functions: setExpression ##

nuke.toNode('Blur1')["size"].setExpression('Blur2.size * 2')

nuke.toNode('Transform1')["filter"].setExpression("Transform2.filter")


### REMOVE ANIMATION / EXPRESSION ###
## Functions: clearAnimated ##


nuke.toNode('Transform1')["filter"].clearAnimated()


### CREATE MULTIPLE NODES WITH `FOR LOOP` ###
## Functions: range ##


for i in range(15):
    i = nuke.createNode("Blur")
    i["channels"].setValue('rgb')
    i["size"].setExpression('Blur1.size')\


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
        node.knob("size").setValue(5)
    except Exception:
        pass


### RUN ON ALL NODES IN A SCRIPT ###
## Functions: allNodes ##


nodes = nuke.allNodes()
for node in nodes:
    try:
        node.knob("size").setValue(20)
    except Exception:
        pass


### RUN AN ALL SPECIFIED CLASSES ###


nodes = nuke.allNodes('Merge2')
for node in nodes:
    node.knob("mix").setValue(.5)


### RUN AN SELECTED SPECIFIED CLASSES ###


nodes = nuke.selectedNodes('Merge2')
for node in nodes:
    try:
        node.knob("mix").setValue(.8)
    except Exception:
        pass


### RUN ON ALL MULTIPLE CLASSES ###


nodes_classes = ["Read", "PostageStamp", "Constant", "ColorBars", "CheckerBoard2", "ColorWheel"]

for node in nuke.allNodes(group=nuke.root()):
    if node.Class() not in nodes_classes:
        continue
    try:
        node["postage_stamp"].setValue(False)
    except Exception:
        pass


### RUN ON SELECTED MULTIPLE CLASSES ###


nuke.root().begin()

nodes_classes = ["Read", "PostageStamp", "Constant", "ColorBars", "CheckerBoard2", "ColorWheel"]

for node in nuke.selectedNodes():
    if node.Class() not in nodes_classes:
        continue
    try:
        node["postage_stamp"].setValue(True)
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


# FUN

import webbrowser

sel = nuke.selectedNode()
site = 'https://imgur.com/search/score/?q=cat'
name = nuke.PyScript_Knob('button', '<font color=pink>Click HERE <font style="font-size:20px; color: orange;">🐈', "webbrowser.open(site)")
sel.addKnob(name)


# https://learn.foundry.com/nuke/developers/90/pythondevguide/performance.html

### NOTES ###

# For checkboxes the value can be True or False that equals to 1 or 0

# For dropdown menu values can be the name of the option or the serial number of the option starting with 0 from the top

# To find the Class of the node select it and press `i` over the NodeGraph

"""
Useful links
Foundry learn:
https://learn.foundry.com/nuke/developers/120/pythondevguide/index.html
Nuke API:
https://learn.foundry.com/nuke/developers/120/pythonreference/
Andrea Geremia Python tips:
http://www.andreageremia.it/tutorial_python_tcl.html
"""



nodes_classes = ["Blur", "Erode"]

for node in nuke.allNodes(group=nuke.root()):
    if node.Class() in nodes_classes:
        try:
            node["size"].setValue(node["size"].getValue() *2 )
        except Exception:
            pass



###

def RotoBlur_Shortcut():
    r = nuke.createNode('Roto', 'output rgba')
    y = int(r['ypos'].getValue()) + 60
    print (y)   
    b = nuke.createNode('Blur', 'size 2').hideControlPanel()
    #b['ypos'].setValue(y)

nuke.menu('Nodes').addMenu('Draw').addCommand('Create Roto and Blur node.', 'RotoBlur_Shortcut()', shortcut='o', icon='Roto.png')



###

r = nuke.toNode('Roto1')['ypos'].getValue()
print(r)
nuke.toNode('Blur1')['ypos'].setValue(r+60)



m = int(nuke.toNode('Roto2')['ypos'].getValue())
n = int(nuke.toNode('Blur2')['ypos'].getValue())

print (m , n)
print (n - m)

#### KEYS

n = sorted(nuke.toNode('Blur1').knobs().keys())
print (n)


m = sorted(nuke.toNode('Blur1').knobs().keys())
for i,knob in enumerate(m):
    print(i,knob)


####


a = nuke.selectedNode()
nodesToSelect = []
 
nodesToSelect.append(a)

def climb(node):
    print node.name()
    for n in node.dependencies():
        nodesToSelect.append(a)
        climb(n)
        n.setSelected('True')

climb(a)

s = nuke.selectedNodes()
b = nuke.allNodes()
for n in b:
    if n not in s:
        nuke.delete(n)


nuke.toNode('Write1')['file'].setExpression('[value [topnode].file]')


#####


def RotoBlur_Shortcut():
    y_offset = 60
    r = nuke.createNode('Roto', 'output alpha')
    y = int(r.ypos() + y_offset)
    b = nuke.nodes.Blur()
    b['size'].setValue(2)
    b['label'].setValue('Size: [value size]')
    b['xpos'].setValue(r.xpos())
    b['ypos'].setValue(y)
    b.setInput(0,r)
    b.hideControlPanel()

# nuke.menu('Nodes').addMenu('Draw').addCommand('Create Roto and Blur node.', 'RotoBlur_Shortcut()', shortcut='o', icon='Roto.png')

####

def SharpenSandwhich():
    y_offset = 60
    r = nuke.createNode('Sharpen')
    r['size'].setValue(4)
    r['label'].setValue('Size: [value size]')
    y = int(r.ypos() + y_offset)
    z = int(r.ypos() - y_offset)
    b = nuke.nodes.Log2Lin()
    b['operation'].setValue('log2lin')
    b['xpos'].setValue(r.xpos())
    b['ypos'].setValue(y)
    b.setInput(0,r)
    b.hideControlPanel()
    l = nuke.nodes.Log2Lin()
    l['operation'].setValue('lin2log')
    l['xpos'].setValue(r.xpos())
    l['ypos'].setValue(z)
    l.hideControlPanel()
    r.setInput(0,l)
    r.showControlPanel()


SharpenSandwhich()



##nuke.menu('Nodes').addMenu('Draw').addCommand('Create Roto and Blur node.', 'RotoBlur_Shortcut()', shortcut='o', icon='Roto.png')


def SharpenSandwhich():
    y_offset = 60
    Lo1 = nuke.createNode('Log2Lin')
    Lo1['operation'].setValue('lin2log')
    Lo1.hideControlPanel()
    ySh = int(Lo1.ypos() + y_offset)
    yLo = int(Lo1.ypos() + (90+y_offset))
    Sh = nuke.nodes.Sharpen()
    Sh['size'].setValue(3)
    Sh['label'].setValue('Size: [value size]')
    Sh['xpos'].setValue(Lo1.xpos())
    Sh['ypos'].setValue(ySh)
    Sh.setInput(0,Lo1)
    Lo2 = nuke.nodes.Log2Lin()
    Lo2['operation'].setValue('log2lin')
    Lo2['xpos'].setValue(Lo1.xpos())
    Lo2['ypos'].setValue(yLo)
    Lo2.setInput(0,Sh)
    Lo2.hideControlPanel()
    Sh.showControlPanel()

SharpenSandwhich()



    r['size'].setValue(4)
    r['label'].setValue('Size: [value size]')
    y = int(r.ypos() + y_offset)
    z = int(r.ypos() - y_offset)
    b = nuke.nodes.Log2Lin()
    b['operation'].setValue('log2lin')
    b['xpos'].setValue(r.xpos())
    b['ypos'].setValue(y)
    b.setInput(0,r)
    b.hideControlPanel()
    l = nuke.nodes.Log2Lin()
    l['operation'].setValue('lin2log')
    l['xpos'].setValue(r.xpos())
    l['ypos'].setValue(z)
    l.hideControlPanel()
    r.setInput(0,l)
    r.showControlPanel()


SharpenSandwhich()


node = nuke.createNode("Blur")
print node
print "---------------------TYPE--------------------------------------"
print type(node)
print "---------------------------------------------------------------"
print node.knob('size')
print "---------------------TYPE--------------------------------------"
print type(node.knob('size'))








### FIRST STEP ###


print ("Hello World!")


### USING VARIABLE ###


name = 'Attila'
age = '30'
country = 'Hungary'
print ('Hello ' + name + '! I am ' + age + '. I am from ' + country)

​

name = 'Attila'
age = 30
country = 'Hungary'
print("Hello %s! I am %d. I am from %s." % (name, age, country))

​

# %d will truncate to integer, %s will maintain formatting, %f will print as float and %g is used for generic number

​

name = 'Attila'
age = 30
country = 'Hungary'
print("Hello {}! I am {}. I am from {}.".format(name, age, country))

​

### TYPE CONVERSION ###


# Interger - int(x)

x = 12.8
print type(x)
x = int(x)
print type(x)
print x

​

# Float - float(x)

x = 12
print type(x)
x = float(x)
print type(x)
print x

​

# String - str(x)

x = 12.5
print type(x)
x = str(x)
print type(x)
print x


### CREATE A NODE ###
## Functions: createNode, setValue ##

​

# Can check node's Class with the `i` hotkey
nuke.createNode("Blur")

​

# Make sure you used a right Class

nuke.createNode("Tracker4")

​

# Can call nodes that are removed from GUI
nuke.createNode("Blocky")

​

# Set a value
nuke.createNode("Blur")['size'].setValue(80)

​

# Set multiple values using a variable
m = nuke.createNode("Blur")
m['channels'].setValue("rgb")
m['size'].setValue(50)
m['mix'].setValue(.5)
m['label'].setValue("Size: [value size]\nChannels: [value channels]\nMix: [value mix]")

​

# Creating node for scripting
nuke.nodes.Blur()

nuke.nodes.Blur(mix=.5,size=10)


### GETTING KNOB VALUE ###
## Functions: toNode, value, getValue, knob ###


# Calling knobs as list items
nuke.toNode('Blur1')["channels"].value()

​

# Calling knobs with a function
nuke.toNode('Blur1').knob("channels").value()

​

nuke.toNode('Blur1')["filter"].getValue()


### SETTING KNOB VALUE ###
## Functions: setValue ##

​

# Setting single value
nuke.toNode('Blur1')["size"].setValue(10)

​

# Setting multiple values
b = nuke.toNode('Blur1')
b["size"].setValue(20)
b["mix"].setValue(.8)
b["filter"].setValue(0)
b["channels"].setValue("rgb")

 

### SETTING EXPRESSION VALUE ###
## Functions: setExpression ##

​

nuke.toNode('Blur1')["size"].setExpression('Blur2.size * 2')

​

nuke.toNode('Transform1')["filter"].setExpression("Transform2.filter")


### REMOVE ANIMATION / EXPRESSION ###
## Functions: clearAnimated ##


nuke.toNode('Transform1')["filter"].clearAnimated()


### CREATE MULTIPLE NODES WITH `FOR LOOP` ###
## Functions: range ##


for i in range(15):
    i = nuke.createNode("Blur")
    i["channels"].setValue('rgb')
    i["size"].setExpression('Blur1.size')


### CONNECT MULTIPLE NODES TO A SINGLE NODE ###
## Functions: selectedNodes, setInput ##

​

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
        node.knob("size").setValue(5)
    except Exception:
        pass


### RUN ON ALL NODES IN A SCRIPT ###
## Functions: allNodes ##


nodes = nuke.allNodes()
for node in nodes:
    try:
        node.knob("size").setValue(20)
    except Exception:
        pass


### RUN AN ALL SPECIFIED CLASSES ###


nodes = nuke.allNodes('Merge2')
for node in nodes:
    node.knob("mix").setValue(.5)


### RUN AN SELECTED SPECIFIED CLASSES ###


nodes = nuke.selectedNodes('Merge2')
for node in nodes:
    try:
        node.knob("mix").setValue(.8)
    except Exception:
        pass


### RUN ON ALL MULTIPLE CLASSES ###


nodes_classes = ["Read", "PostageStamp", "Constant", "ColorBars", "CheckerBoard2", "ColorWheel"]

for node in nuke.allNodes(group=nuke.root()):
    if node.Class() not in nodes_classes:
        continue
    try:
        node["postage_stamp"].setValue(False)
    except Exception:
        pass


### RUN ON SELECTED MULTIPLE CLASSES ###


nuke.root().begin()

nodes_classes = ["Read", "PostageStamp", "Constant", "ColorBars", "CheckerBoard2", "ColorWheel"]

for node in nuke.selectedNodes():
    if node.Class() not in nodes_classes:
        continue
    try:
        node["postage_stamp"].setValue(True)
    except Exception:
        pass
nuke.root().end()


### PATH FOR YOUR NUKE FOLDER ###


nuke.pluginPath()


### PERFORMANCE TIMER ###

​

#start
nuke.startPerformanceTimers()

​

#reset
nuke.resetPerformanceTimers()

​

#stop
nuke.stopPerformanceTimers()


# https://learn.foundry.com/nuke/developers/90/pythondevguide/performance.html

​

### FUN ###

​

import webbrowser

sel = nuke.selectedNode()
site = 'https://imgur.com/search/score/?q=cat'
name = nuke.PyScript_Knob('button', '<font color=pink>Click HERE', "webbrowser.open(site)")
sel.addKnob(name)


### NOTES ###

​

# For checkboxes the value can be True or False that equals to 1 or 0

# For dropdown menu values can be the name of the option or the serial number of the option starting with 0 from the top

# To find the Class of the node select it and press `i` over the NodeGraph







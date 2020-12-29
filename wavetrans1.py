###################

## Add Random Wave
waveGr = nuke.toNode('RandGrade')

knob = waveGr['knobs'].value()
if knob == "lift":
    knob = "black"
if knob == "gain":
    knob = "white"
if knob == "offset":
    knob = "add"

chan = waveGr['channels_1'].value()
if chan == "all":
    waveGr[knob].setExpression("random((frame+offset)/waveLength) * (maxVal-minVal) + minVal")
if chan == "red":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("random((frame+offset)/waveLength) * (maxVal-minVal) + minVal", 0)
if chan == "green":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("random((frame+offset)/waveLength) * (maxVal-minVal) + minVal", 1)
if chan == "blue":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("random((frame+offset)/waveLength) * (maxVal-minVal) + minVal", 2)
if chan == "alpha":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("random((frame+offset)/waveLength) * (maxVal-minVal) + minVal", 3)




## Add Sine Wave
waveGr = nuke.toNode('WaveGrade')

knob = waveGr['knobs'].value()
if knob == "lift":
    knob = "black"
if knob == "gain":
    knob = "white"
if knob == "offset":
    knob = "add"

chan = waveGr['channels_1'].value()
if chan == "all":
    waveGr[knob].setExpression("(sin(2*pi*(frame+offset)/waveLength)+1)/2 * (maxVal-minVal) + minVal")
if chan == "red":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("(sin(2*pi*(frame+offset)/waveLength)+1)/2 * (maxVal-minVal) + minVal", 0)
if chan == "green":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("(sin(2*pi*(frame+offset)/waveLength)+1)/2 * (maxVal-minVal) + minVal", 1)
if chan == "blue":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("(sin(2*pi*(frame+offset)/waveLength)+1)/2 * (maxVal-minVal) + minVal", 2)
if chan == "alpha":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("(sin(2*pi*(frame+offset)/waveLength)+1)/2 * (maxVal-minVal) + minVal", 3)


## Add Triangle Wave
waveGr = nuke.toNode('WaveGrade')

knob = waveGr['knobs'].value()
if knob == "lift":
    knob = "black"
if knob == "gain":
    knob = "white"
if knob == "offset":
    knob = "add"

chan = waveGr['channels_1'].value()
if chan == "all":
    waveGr[knob].setExpression("(asin(sin(2*pi*(frame+offset)/waveLength))/pi+0.5) * (maxVal-minVal) + minVal")
if chan == "red":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("(asin(sin(2*pi*(frame+offset)/waveLength))/pi+0.5) * (maxVal-minVal) + minVal", 0)
if chan == "green":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("(asin(sin(2*pi*(frame+offset)/waveLength))/pi+0.5) * (maxVal-minVal) + minVal", 1)
if chan == "blue":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("(asin(sin(2*pi*(frame+offset)/waveLength))/pi+0.5) * (maxVal-minVal) + minVal", 2)
if chan == "alpha":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("(asin(sin(2*pi*(frame+offset)/waveLength))/pi+0.5) * (maxVal-minVal) + minVal", 3)



## Add Square Wave
waveGr = nuke.toNode('WaveGrade')

knob = waveGr['knobs'].value()
if knob == "lift":
    knob = "black"
if knob == "gain":
    knob = "white"
if knob == "offset":
    knob = "add"

chan = waveGr['channels_1'].value()
if chan == "all":
    waveGr[knob].setExpression("int(sin(2*pi*(frame+offset)/waveLength)+1) * (maxVal-minVal) + minVal")
if chan == "red":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("int(sin(2*pi*(frame+offset)/waveLength)+1) * (maxVal-minVal) + minVal", 0)
if chan == "green":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("int(sin(2*pi*(frame+offset)/waveLength)+1) * (maxVal-minVal) + minVal", 1)
if chan == "blue":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("int(sin(2*pi*(frame+offset)/waveLength)+1) * (maxVal-minVal) + minVal", 2)
if chan == "alpha":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("int(sin(2*pi*(frame+offset)/waveLength)+1) * (maxVal-minVal) + minVal", 3)


## Add Sawtooth Wave
waveGr = nuke.toNode('WaveGrade')

knob = waveGr['knobs'].value()
if knob == "lift":
    knob = "black"
if knob == "gain":
    knob = "white"
if knob == "offset":
    knob = "add"

chan = waveGr['channels_1'].value()
if chan == "all":
    waveGr[knob].setExpression("((frame+offset) % waveLength)/waveLength * (maxVal-minVal) + minVal")
if chan == "red":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("((frame+offset) % waveLength)/waveLength * (maxVal-minVal) + minVal", 0)
if chan == "green":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("((frame+offset) % waveLength)/waveLength * (maxVal-minVal) + minVal", 1)
if chan == "blue":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("((frame+offset) % waveLength)/waveLength * (maxVal-minVal) + minVal", 2)
if chan == "alpha":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("((frame+offset) % waveLength)/waveLength * (maxVal-minVal) + minVal", 3)


## Add Bounce Wave
waveGr = nuke.toNode('WaveGrade')

knob = waveGr['knobs'].value()
if knob == "lift":
    knob = "black"
if knob == "gain":
    knob = "white"
if knob == "offset":
    knob = "add"

chan = waveGr['channels_1'].value()
if chan == "all":
    waveGr[knob].setExpression("abs(sin(pi*(frame + offset)/waveLength))* (maxVal-minVal) + minVal")
if chan == "red":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("abs(sin(pi*(frame + offset)/waveLength))* (maxVal-minVal) + minVal", 0)
if chan == "green":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("abs(sin(pi*(frame + offset)/waveLength))* (maxVal-minVal) + minVal", 1)
if chan == "blue":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("abs(sin(pi*(frame + offset)/waveLength))* (maxVal-minVal) + minVal", 2)
if chan == "alpha":
    waveGr[knob].setSingleValue(False)
    waveGr[knob].setExpression("abs(sin(pi*(frame + offset)/waveLength))* (maxVal-minVal) + minVal", 3)



## Set to default
waveGr = nuke.toNode('WaveGrade')

waveGr['blackpoint'].clearAnimated()
waveGr['blackpoint'].setValue(0)
waveGr['whitepoint'].clearAnimated()
waveGr['whitepoint'].setValue(1)
waveGr['black'].clearAnimated()
waveGr['black'].setValue(0)
waveGr['white'].clearAnimated()
waveGr['white'].setValue(1)
waveGr['multiply'].clearAnimated()
waveGr['multiply'].setValue(1)
waveGr['add'].clearAnimated()
waveGr['add'].setValue(0)
waveGr['gamma'].clearAnimated()
waveGr['gamma'].setValue(1)


# Add Random Wave
waveMul = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Random Wave":
    knob1 = waveMul['random_wave']
    knob1.setLabel("<font color=#20bd2b>Random Wave Added")

    knob2 = waveMul['sine_wave']
    knob2.setLabel("<font color=#cccccc>Add Sine Wave")

    knob3 = waveMul['triangle_wave']
    knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

    knob4 = waveMul['square_wave']
    knob4.setLabel("<font color=#cccccc>Add Square Wave")

    knob5 = waveMul['sawtooth_wave']
    knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

    knob6 = waveMul['bounce_wave']
    knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

    waveMul['value'].clearAnimated()
    waveMul['value'].setExpression("random((frame+offset)/waveLength) * (maxVal-minVal) + minVal")

else:
    nuke.message("""<center><b><font color=orange>Random Wave is already added!""")


# Add Sine Wave
waveMul = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Sine Wave":
    knob1 = waveMul['random_wave']
    knob1.setLabel("<font color=#cccccc>Add Random Wave")

    knob2 = waveMul['sine_wave']
    knob2.setLabel("<font color=#20bd2b>Sine Wave Added")

    knob3 = waveMul['triangle_wave']
    knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

    knob4 = waveMul['square_wave']
    knob4.setLabel("<font color=#cccccc>Add Square Wave")

    knob5 = waveMul['sawtooth_wave']
    knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

    knob6 = waveMul['bounce_wave']
    knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

    waveMul['value'].clearAnimated()
    waveMul['value'].setExpression("(sin(2*pi*(frame+offset)/waveLength)+1)/2 * (maxVal-minVal) + minVal")

else:
    nuke.message("""<center><b><font color=orange>Sine Wave is already added!""")


# Add Triangle Wave
waveMul = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Triangle Wave":
    knob1 = waveMul['random_wave']
    knob1.setLabel("<font color=#cccccc>Add Random Wave")

    knob2 = waveMul['sine_wave']
    knob2.setLabel("<font color=#cccccc>Add Sine Wave")

    knob3 = waveMul['triangle_wave']
    knob3.setLabel("<font color=#20bd2b>Triangle Wave Added")

    knob4 = waveMul['square_wave']
    knob4.setLabel("<font color=#cccccc>Add Square Wave")

    knob5 = waveMul['sawtooth_wave']
    knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

    knob6 = waveMul['bounce_wave']
    knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

    waveMul['value'].clearAnimated()
    waveMul['value'].setExpression("(asin(sin(2*pi*(frame+offset)/waveLength))/pi+0.5) * (maxVal-minVal) + minVal")

else:
    nuke.message("""<center><b><font color=orange>Triangle Wave is already added!""")


# Add Square Wave
waveMul = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Square Wave":
    knob1 = waveMul['random_wave']
    knob1.setLabel("<font color=#cccccc>Add Random Wave")

    knob2 = waveMul['sine_wave']
    knob2.setLabel("<font color=#cccccc>Add Sine Wave")

    knob3 = waveMul['triangle_wave']
    knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

    knob4 = waveMul['square_wave']
    knob4.setLabel("<font color=#20bd2b>Square Wave Added")

    knob5 = waveMul['sawtooth_wave']
    knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

    knob6 = waveMul['bounce_wave']
    knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

    waveMul['value'].clearAnimated()
    waveMul['value'].setExpression("int(sin(2*pi*(frame+offset)/waveLength)+1) * (maxVal-minVal) + minVal")

else:
    nuke.message("""<center><b><font color=orange>Square Wave is already added!""")



# Add Sawtooth Wave
waveMul = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Sawtooth Wave":
    knob1 = waveMul['random_wave']
    knob1.setLabel("<font color=#cccccc>Add Random Wave")

    knob2 = waveMul['sine_wave']
    knob2.setLabel("<font color=#cccccc>Add Sine Wave")

    knob3 = waveMul['triangle_wave']
    knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

    knob4 = waveMul['square_wave']
    knob4.setLabel("<font color=#cccccc>Add Square Wave")

    knob5 = waveMul['sawtooth_wave']
    knob5.setLabel("<font color=#20bd2b>Sawtooth Wave Added")

    knob6 = waveMul['bounce_wave']
    knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

    waveMul['value'].clearAnimated()
    waveMul['value'].setExpression("((frame+offset) % waveLength)/waveLength * (maxVal-minVal) + minVal")

else:
    nuke.message("""<center><b><font color=orange>Sawtooth Wave is already added!""")



# Add Bounce Wave
waveMul = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Bounce Wave":
    knob1 = waveMul['random_wave']
    knob1.setLabel("<font color=#cccccc>Add Random Wave")

    knob2 = waveMul['sine_wave']
    knob2.setLabel("<font color=#cccccc>Add Sine Wave")

    knob3 = waveMul['triangle_wave']
    knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

    knob4 = waveMul['square_wave']
    knob4.setLabel("<font color=#cccccc>Add Square Wave")

    knob5 = waveMul['sawtooth_wave']
    knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

    knob6 = waveMul['bounce_wave']
    knob6.setLabel("<font color=#20bd2b>Bounce Wave Added")

    waveMul['value'].clearAnimated()
    waveMul['value'].setExpression("abs(sin(pi*(frame + offset)/waveLength))* (maxVal-minVal) + minVal")

else:
    nuke.message("""<center><b><font color=orange>Bounce Wave is already added!""")


# Set to 1
waveMul = nuke.thisNode()
knob1 = waveMul['random_wave']
knob1.setLabel("<font color=#cccccc>Add Random Wave")

knob2 = waveMul['sine_wave']
knob2.setLabel("<font color=#cccccc>Add Sine Wave")

knob3 = waveMul['triangle_wave']
knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

knob4 = waveMul['square_wave']
knob4.setLabel("<font color=#cccccc>Add Square Wave")

knob5 = waveMul['sawtooth_wave']
knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

knob6 = waveMul['bounce_wave']
knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

waveMul['value'].clearAnimated()
waveMul['value'].setValue(1)



################################

# Add Random Wave
waveTrans = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Random Wave":
    knob1 = waveTrans['random_wave']
    knob1.setLabel("<font color=#20bd2b>Random Wave Added")

    knob2 = waveTrans['sine_wave']
    knob2.setLabel("<font color=#cccccc>Add Sine Wave")

    knob3 = waveTrans['triangle_wave']
    knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

    knob4 = waveTrans['square_wave']
    knob4.setLabel("<font color=#cccccc>Add Square Wave")

    knob5 = waveTrans['sawtooth_wave']
    knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

    knob6 = waveTrans['bounce_wave']
    knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

    waveTrans['translate'].setExpression("random((frame+offset)/waveLength) * (maxVal-minVal) + minVal", 0)
    waveTrans['translate'].setExpression("random((frame+offset+x_y_offset)/waveLength) * (maxVal-minVal) + minVal", 1)

else:
    nuke.message("""<center><b><font color=orange>Random Wave is already added!""")


# Add Sine Wave
waveTrans = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Sine Wave":
    knob1 = waveTrans['random_wave']
    knob1.setLabel("<font color=#cccccc>Add Random Wave")

    knob2 = waveTrans['sine_wave']
    knob2.setLabel("<font color=#20bd2b>Sine Wave Added")

    knob3 = waveTrans['triangle_wave']
    knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

    knob4 = waveTrans['square_wave']
    knob4.setLabel("<font color=#cccccc>Add Square Wave")

    knob5 = waveTrans['sawtooth_wave']
    knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

    knob6 = waveTrans['bounce_wave']
    knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

    waveTrans['translate'].setExpression("(sin(2*pi*(frame+offset)/waveLength)+1)/2 * (maxVal-minVal) + minVal", 0)
    waveTrans['translate'].setExpression("(sin(2*pi*(frame+offset+x_y_offset)/waveLength)+1)/2 * (maxVal-minVal) + minVal", 1)

else:
    nuke.message("""<center><b><font color=orange>Sine Wave is already added!""")



# Add Triangle Wave
waveTrans = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Triangle Wave":
    knob1 = waveTrans['random_wave']
    knob1.setLabel("<font color=#cccccc>Add Random Wave")

    knob2 = waveTrans['sine_wave']
    knob2.setLabel("<font color=#cccccc>Add Sine Wave")

    knob3 = waveTrans['triangle_wave']
    knob3.setLabel("<font color=#20bd2b>Triangle Wave Added")

    knob4 = waveTrans['square_wave']
    knob4.setLabel("<font color=#cccccc>Add Square Wave")

    knob5 = waveTrans['sawtooth_wave']
    knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

    knob6 = waveTrans['bounce_wave']
    knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

    waveTrans['translate'].setExpression("(asin(sin(2*pi*(frame+offset)/waveLength))/pi+0.5) * (maxVal-minVal) + minVal", 0)
    waveTrans['translate'].setExpression("(asin(sin(2*pi*(frame+offset+x_y_offset)/waveLength))/pi+0.5) * (maxVal-minVal) + minVal", 1)

else:
    nuke.message("""<center><b><font color=orange>Triangle Wave is already added!""")



# Add Square Wave
waveTrans = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Square Wave":
    knob1 = waveTrans['random_wave']
    knob1.setLabel("<font color=#cccccc>Add Random Wave")

    knob2 = waveTrans['sine_wave']
    knob2.setLabel("<font color=#cccccc>Add Sine Wave")

    knob3 = waveTrans['triangle_wave']
    knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

    knob4 = waveTrans['square_wave']
    knob4.setLabel("<font color=#20bd2b>Square Wave Added")

    knob5 = waveTrans['sawtooth_wave']
    knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

    knob6 = waveTrans['bounce_wave']
    knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

    waveTrans['translate'].setExpression("int(sin(2*pi*(frame+offset)/waveLength)+1) * (maxVal-minVal) + minVal", 0)
    waveTrans['translate'].setExpression("int(sin(2*pi*(frame+offset+x_y_offset)/waveLength)+1) * (maxVal-minVal) + minVal", 1)

else:
    nuke.message("""<center><b><font color=orange>Square Wave is already added!""")



# Add Sawtooth Wave
waveTrans = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Sawtooth Wave":
    knob1 = waveTrans['random_wave']
    knob1.setLabel("<font color=#cccccc>Add Random Wave")

    knob2 = waveTrans['sine_wave']
    knob2.setLabel("<font color=#cccccc>Add Sine Wave")

    knob3 = waveTrans['triangle_wave']
    knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

    knob4 = waveTrans['square_wave']
    knob4.setLabel("<font color=#cccccc>Add Square Wave")

    knob5 = waveTrans['sawtooth_wave']
    knob5.setLabel("<font color=#20bd2b>Sawtooth Wave Added")

    knob6 = waveTrans['bounce_wave']
    knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

    waveTrans['translate'].setExpression("((frame+offset) % waveLength)/waveLength * (maxVal-minVal) + minVal", 0)
    waveTrans['translate'].setExpression("((frame+offset+x_y_offset) % waveLength)/waveLength * (maxVal-minVal) + minVal", 1)

else:
    nuke.message("""<center><b><font color=orange>Sawtooth Wave is already added!""")



# Add Bounce Wave
waveTrans = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Bounce Wave":
    knob1 = waveTrans['random_wave']
    knob1.setLabel("<font color=#cccccc>Add Random Wave")

    knob2 = waveTrans['sine_wave']
    knob2.setLabel("<font color=#cccccc>Add Sine Wave")

    knob3 = waveTrans['triangle_wave']
    knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

    knob4 = waveTrans['square_wave']
    knob4.setLabel("<font color=#cccccc>Add Square Wave")

    knob5 = waveTrans['sawtooth_wave']
    knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

    knob6 = waveTrans['bounce_wave']
    knob6.setLabel("<font color=#20bd2b>Bounce Wave Added")

    waveTrans['translate'].setExpression("abs(sin(pi*(frame + offset)/waveLength))* (maxVal-minVal) + minVal", 0)
    waveTrans['translate'].setExpression("abs(sin(pi*(frame + offset+x_y_offset)/waveLength))* (maxVal-minVal) + minVal", 1)

else:
    nuke.message("""<center><b><font color=orange>Bounce Wave is already added!""")


# Set to Default
waveTrans = nuke.thisNode()
knob1 = waveTrans['random_wave']
knob1.setLabel("<font color=#cccccc>Add Random Wave")

knob2 = waveTrans['sine_wave']
knob2.setLabel("<font color=#cccccc>Add Sine Wave")

knob3 = waveTrans['triangle_wave']
knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

knob4 = waveTrans['square_wave']
knob4.setLabel("<font color=#cccccc>Add Square Wave")

knob5 = waveTrans['sawtooth_wave']
knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

knob6 = waveTrans['bounce_wave']
knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

waveTrans['translate'].clearAnimated()
waveTrans['translate'].setValue(0)

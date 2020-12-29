# Add Random Wave
waveTrans = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Random Wave":
    knob1 = waveTrans['random_wave_2']
    knob1.setLabel("<font color=#20bd2b>Random Wave Added")

    knob2 = waveTrans['sine_wave_2']
    knob2.setLabel("<font color=#cccccc>Add Sine Wave")

    knob3 = waveTrans['triangle_wave_2']
    knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

    knob4 = waveTrans['square_wave_2']
    knob4.setLabel("<font color=#cccccc>Add Square Wave")

    knob5 = waveTrans['sawtooth_wave_2']
    knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

    knob6 = waveTrans['bounce_wave_2']
    knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

    waveTrans['rotate'].setExpression("random((frame+offset2)/waveLength2) * (maxVal2-minVal2) + minVal2")

else:
    nuke.message("""<center><b><font color=orange>Random Wave is already added!""")


# Add Sine Wave
waveTrans = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Sine Wave":
    knob1 = waveTrans['random_wave_2']
    knob1.setLabel("<font color=#cccccc>Add Random Wave")

    knob2 = waveTrans['sine_wave_2']
    knob2.setLabel("<font color=#20bd2b>Sine Wave Added")

    knob3 = waveTrans['triangle_wave_2']
    knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

    knob4 = waveTrans['square_wave_2']
    knob4.setLabel("<font color=#cccccc>Add Square Wave")

    knob5 = waveTrans['sawtooth_wave_2']
    knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

    knob6 = waveTrans['bounce_wave_2']
    knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

    waveTrans['rotate'].setExpression("(sin(2*pi*(frame+offset2)/waveLength2)+1)/2 * (maxVal2-minVal2) + minVal2")

else:
    nuke.message("""<center><b><font color=orange>Sine Wave is already added!""")


# Add Triangle Wave
waveTrans = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Triangle Wave":
    knob1 = waveTrans['random_wave_2']
    knob1.setLabel("<font color=#cccccc>Add Random Wave")

    knob2 = waveTrans['sine_wave_2']
    knob2.setLabel("<font color=#cccccc>Add Sine Wave")

    knob3 = waveTrans['triangle_wave_2']
    knob3.setLabel("<font color=#20bd2b>Triangle Wave Added")

    knob4 = waveTrans['square_wave_2']
    knob4.setLabel("<font color=#cccccc>Add Square Wave")

    knob5 = waveTrans['sawtooth_wave_2']
    knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

    knob6 = waveTrans['bounce_wave_2']
    knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

    waveTrans['rotate'].setExpression("(asin(sin(2*pi*(frame+offset2)/waveLength2))/pi+0.5) * (maxVal2-minVal2) + minVal2")

else:
    nuke.message("""<center><b><font color=orange>Triangle Wave is already added!""")


# Add Square Wave
waveTrans = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Square Wave":
    knob1 = waveTrans['random_wave_2']
    knob1.setLabel("<font color=#cccccc>Add Random Wave")

    knob2 = waveTrans['sine_wave_2']
    knob2.setLabel("<font color=#cccccc>Add Sine Wave")

    knob3 = waveTrans['triangle_wave_2']
    knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

    knob4 = waveTrans['square_wave_2']
    knob4.setLabel("<font color=#20bd2b>Square Wave Added")

    knob5 = waveTrans['sawtooth_wave_2']
    knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

    knob6 = waveTrans['bounce_wave_2']
    knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

    waveTrans['rotate'].setExpression("int(sin(2*pi*(frame+offset2)/waveLength2)+1) * (maxVal2-minVal2) + minVal2")

else:
    nuke.message("""<center><b><font color=orange>Square Wave is already added!""")


# Add Sawtooth Wave
waveTrans = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Sawtooth Wave":
    knob1 = waveTrans['random_wave_2']
    knob1.setLabel("<font color=#cccccc>Add Random Wave")

    knob2 = waveTrans['sine_wave_2']
    knob2.setLabel("<font color=#cccccc>Add Sine Wave")

    knob3 = waveTrans['triangle_wave_2']
    knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

    knob4 = waveTrans['square_wave_2']
    knob4.setLabel("<font color=#cccccc>Add Square Wave")

    knob5 = waveTrans['sawtooth_wave_2']
    knob5.setLabel("<font color=#20bd2b>Sawtooth Wave Added")

    knob6 = waveTrans['bounce_wave_2']
    knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

    waveTrans['rotate'].setExpression("((frame+offset2) % waveLength2)/waveLength2 * (maxVal2-minVal2) + minVal2")

else:
    nuke.message("""<center><b><font color=orange>Sawtooth Wave is already added!""")


# Add Bounce Wave
waveTrans = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Bounce Wave":
    knob1 = waveTrans['random_wave_2']
    knob1.setLabel("<font color=#cccccc>Add Random Wave")

    knob2 = waveTrans['sine_wave_2']
    knob2.setLabel("<font color=#cccccc>Add Sine Wave")

    knob3 = waveTrans['triangle_wave_2']
    knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

    knob4 = waveTrans['square_wave_2']
    knob4.setLabel("<font color=#cccccc>Add Square Wave")

    knob5 = waveTrans['sawtooth_wave_2']
    knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

    knob6 = waveTrans['bounce_wave_2']
    knob6.setLabel("<font color=#20bd2b>Bounce Wave Added")

    waveTrans['rotate'].setExpression("abs(sin(pi*(frame + offset2)/waveLength2))* (maxVal2-minVal2) + minVal2")

else:
    nuke.message("""<center><b><font color=orange>Bounce Wave is already added!""")


# Set to Default
waveTrans = nuke.thisNode()
knob1 = waveTrans['random_wave_2']
knob1.setLabel("<font color=#cccccc>Add Random Wave")

knob2 = waveTrans['sine_wave_2']
knob2.setLabel("<font color=#cccccc>Add Sine Wave")

knob3 = waveTrans['triangle_wave_2']
knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

knob4 = waveTrans['square_wave_2']
knob4.setLabel("<font color=#cccccc>Add Square Wave")

knob5 = waveTrans['sawtooth_wave_2']
knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

knob6 = waveTrans['bounce_wave_2']
knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

waveTrans['rotate'].clearAnimated()
waveTrans['rotate'].setValue(0)



#######################################


# Add Random Wave
waveTrans = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Random Wave":
    knob1 = waveTrans['random_wave_3']
    knob1.setLabel("<font color=#20bd2b>Random Wave Added")

    knob2 = waveTrans['sine_wave_3']
    knob2.setLabel("<font color=#cccccc>Add Sine Wave")

    knob3 = waveTrans['triangle_wave_3']
    knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

    knob4 = waveTrans['square_wave_3']
    knob4.setLabel("<font color=#cccccc>Add Square Wave")

    knob5 = waveTrans['sawtooth_wave_3']
    knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

    knob6 = waveTrans['bounce_wave_3']
    knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

    waveTrans['scale'].setExpression("random((frame+offset3)/waveLength3) * (maxVal3-minVal3) + minVal3")

else:
    nuke.message("""<center><b><font color=orange>Random Wave is already added!""")


# Add Sine Wave
waveTrans = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Sine Wave":
    knob1 = waveTrans['random_wave_3']
    knob1.setLabel("<font color=#cccccc>Add Random Wave")

    knob2 = waveTrans['sine_wave_3']
    knob2.setLabel("<font color=#20bd2b>Sine Wave Added")

    knob3 = waveTrans['triangle_wave_3']
    knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

    knob4 = waveTrans['square_wave_3']
    knob4.setLabel("<font color=#cccccc>Add Square Wave")

    knob5 = waveTrans['sawtooth_wave_3']
    knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

    knob6 = waveTrans['bounce_wave_3']
    knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

    waveTrans['scale'].setExpression("(sin(2*pi*(frame+offset3)/waveLength3)+1)/2 * (maxVal3-minVal3) + minVal3")

else:
    nuke.message("""<center><b><font color=orange>Sine Wave is already added!""")


# Add Triangle Wave
waveTrans = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Triangle Wave":
    knob1 = waveTrans['random_wave_3']
    knob1.setLabel("<font color=#cccccc>Add Random Wave")

    knob2 = waveTrans['sine_wave_3']
    knob2.setLabel("<font color=#cccccc>Add Sine Wave")

    knob3 = waveTrans['triangle_wave_3']
    knob3.setLabel("<font color=#20bd2b>Triangle Wave Added")

    knob4 = waveTrans['square_wave_3']
    knob4.setLabel("<font color=#cccccc>Add Square Wave")

    knob5 = waveTrans['sawtooth_wave_3']
    knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

    knob6 = waveTrans['bounce_wave_3']
    knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

    waveTrans['scale'].setExpression("(asin(sin(2*pi*(frame+offset3)/waveLength3))/pi+0.5) * (maxVal3-minVal3) + minVal3")

else:
    nuke.message("""<center><b><font color=orange>Triangle Wave is already added!""")



# Add Square Wave
waveTrans = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Square Wave":
    knob1 = waveTrans['random_wave_3']
    knob1.setLabel("<font color=#cccccc>Add Random Wave")

    knob2 = waveTrans['sine_wave_3']
    knob2.setLabel("<font color=#cccccc>Add Sine Wave")

    knob3 = waveTrans['triangle_wave_3']
    knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

    knob4 = waveTrans['square_wave_3']
    knob4.setLabel("<font color=#20bd2b>Square Wave Added")

    knob5 = waveTrans['sawtooth_wave_3']
    knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

    knob6 = waveTrans['bounce_wave_3']
    knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

    waveTrans['scale'].setExpression("int(sin(2*pi*(frame+offset3)/waveLength3)+1) * (maxVal3-minVal3) + minVal3")

else:
    nuke.message("""<center><b><font color=orange>Square Wave is already added!""")


# Add Sawtooth Wave
waveTrans = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Sawtooth Wave":
    knob1 = waveTrans['random_wave_3']
    knob1.setLabel("<font color=#cccccc>Add Random Wave")

    knob2 = waveTrans['sine_wave_3']
    knob2.setLabel("<font color=#cccccc>Add Sine Wave")

    knob3 = waveTrans['triangle_wave_3']
    knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

    knob4 = waveTrans['square_wave_3']
    knob4.setLabel("<font color=#cccccc>Add Square Wave")

    knob5 = waveTrans['sawtooth_wave_3']
    knob5.setLabel("<font color=#20bd2b>Sawtooth Wave Added")

    knob6 = waveTrans['bounce_wave_3']
    knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

    waveTrans['scale'].setExpression("((frame+offset3) % waveLength3)/waveLength3 * (maxVal3-minVal3) + minVal3")

else:
    nuke.message("""<center><b><font color=orange>Sawtooth Wave is already added!""")


# Add Bounce Wave
waveTrans = nuke.thisNode()
knob = nuke.thisKnob()

if knob.label() == "<font color=#cccccc>Add Bounce Wave":
    knob1 = waveTrans['random_wave_3']
    knob1.setLabel("<font color=#cccccc>Add Random Wave")

    knob2 = waveTrans['sine_wave_3']
    knob2.setLabel("<font color=#cccccc>Add Sine Wave")

    knob3 = waveTrans['triangle_wave_3']
    knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

    knob4 = waveTrans['square_wave_3']
    knob4.setLabel("<font color=#cccccc>Add Square Wave")

    knob5 = waveTrans['sawtooth_wave_3']
    knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

    knob6 = waveTrans['bounce_wave_3']
    knob6.setLabel("<font color=#20bd2b>Bounce Wave Added")

    waveTrans['scale'].setExpression("abs(sin(pi*(frame + offset3)/waveLength3))* (maxVal3-minVal3) + minVal3")

else:
    nuke.message("""<center><b><font color=orange>Bounce Wave is already added!""")


# Set to Default
waveTrans = nuke.thisNode()
knob1 = waveTrans['random_wave_3']
knob1.setLabel("<font color=#cccccc>Add Random Wave")

knob2 = waveTrans['sine_wave_3']
knob2.setLabel("<font color=#cccccc>Add Sine Wave")

knob3 = waveTrans['triangle_wave_3']
knob3.setLabel("<font color=#cccccc>Add Triangle Wave")

knob4 = waveTrans['square_wave_3']
knob4.setLabel("<font color=#cccccc>Add Square Wave")

knob5 = waveTrans['sawtooth_wave_3']
knob5.setLabel("<font color=#cccccc>Add Sawtooth Wave")

knob6 = waveTrans['bounce_wave_3']
knob6.setLabel("<font color=#cccccc>Add Bounce Wave")

waveTrans['scale'].clearAnimated()
waveTrans['scale'].setValue(1)

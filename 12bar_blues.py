import music, random

synthBass = synth.PatchSynth(num_voices=1, patch=0)
synthMelody = synth.PatchSynth(num_voices=4, patch=128)
synthMelody.note_on(48, 0.6)
synthMelody.note_on(52, 0.6)
synthMelody.note_on(55, 0.6)
synthMelody.note_on(58, 0.6)
synthBass.note_on(36, 2)
for i in range(3000):
    print(i)
synthBass.note_off(36)
synthBass.all_notes_off()
synthBass.note_on(40, 2)
for i in range(3000):
    print(i)
synthBass.note_off(40)
synthBass.note_on(43, 2)
for i in range(3000):
    print(i)
synthBass.note_off(43)
synthBass.note_on(45, 2)
for i in range(3000):
    print(i)
synthBass.note_off(45)
synthBass.note_on(46, 2)
for i in range(3000):
    print(i)
synthBass.note_off(46)
synthBass.note_on(45, 2)
for i in range(3000):
    print(i)
synthBass.note_off(45)
synthBass.note_on(43, 2)
for i in range(3000):
    print(i)
synthBass.note_off(43)
synthBass.note_on(40, 2)
for i in range(3000):
    print(i)
synthBass.note_off(40)
synthMelody.note_off(48)
synthMelody.note_off(52)
synthMelody.note_off(55)
synthMelody.note_off(58)
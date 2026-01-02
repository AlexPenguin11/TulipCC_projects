import music, random

measures = 12
beats = 4
note_count = 4

seq = sequencer.AMYSequence(measures * beats, note_count)
#This starts at 1, not 0

synthBass = synth.PatchSynth(num_voices=1, patch=142)
synthMelody = synth.PatchSynth(num_voices=4, patch=128)

notes = [[[36, 40, 43, 40], [48, 52, 55, 58]],
         [[36, 40, 43, 40], [48, 52, 55, 58]],
         [[36, 40, 43, 40], [48, 52, 55, 58]],
         [[36, 40, 43, 40], [48, 52, 55, 58]],
         [[41, 45, 48, 45], [53, 57, 60, 63]],
         [[41, 45, 48, 45], [53, 57, 60, 63]],
         [[36, 40, 43, 40], [48, 52, 55, 58]],
         [[36, 40, 43, 40], [48, 52, 55, 58]],
         [[43, 47, 50, 47], [55, 59, 62, 65]],
         [[41, 45, 48, 45], [53, 57, 60, 63]],
         [[36, 40, 43, 40], [48, 52, 55, 58]],
         [[36, 40, 43, 40], [48, 52, 55, 58]] ]

for i in range(12):
    for j in  range (4):
        # since there is only one voice, no need to turn notes back off
        #if j == 0 and i == 0:
        #    note_off = measures*beats-1
        #    note_idx = j+3
        #else:
        #    note_off = i*beats+j-1
        #    note_idx = j-1
        #seq.add(note_off, synthBass.note_off, [notes[i][0][note_idx]])
        seq.add(i*beats+j + 1, synthBass.note_on, [notes[i][0][j]])
        print("I: ",i,"J: ",j,"Add: ",notes[i][0][j] )
    for k in range(4):
        #seq.add(i*beats, synthMelody.note_off, [notes[i-1][k+1]])
        seq.add(i*beats + 1, synthMelody.note_on, [notes[i][1][k],0.2])
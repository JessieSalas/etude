#creates a lily file for later exectution
import os
import random
from chords import songs

lily_file = open("raw.lily", "w")
title = "How High The Moon" #depends on what the user selects
subtitle = "personalized practice" #we may not include a subtitile
instrument = "Tenor Saxophone" #defined by user
arranger = "Etude"
tagline = "Created by Etude, the personalized practice engine."


sax_notes = ["bes8", "b8", "c'8","cis'8","d'8","dis'8","e'8","f'8","fis'8","g'8","gis'8","a'8","ais'8","b'8","c''8","cis''8", "d''8", "dis''8", "e''8","f''8", "fis''8", "g''8", "gis''8", "a''8", "ais''8", "b''8","c'''8", "cis'''8", "d'''8", "dis'''8", "e'''8", "f'''8"] #for saxes

trumpet_notes = ["fis","g8", "aes8", "a8","bes8", "b8", "c'8","cis'8","d'8","dis'8","e'8","f'8","fis'8","g'8","gis'8","a'8","ais'8","b'8","c''8","cis''8", "d''8", "dis''8", "e''8","f''8", "fis''8", "g''8", "gis''8", "a''8", "ais''8", "b''8","c'''8"] #for trumpet

clarinet_notes = ["e8", "f8","fis8","g8", "aes8", "a8","bes8", "b8", "c'8","cis'8","d'8","dis'8","e'8","f'8","fis'8","g'8","gis'8","a'8","ais'8","b'8","c''8","cis''8", "d''8", "dis''8", "e''8","f''8", "fis''8", "g''8", "gis''8", "a''8", "ais''8", "b''8","c'''8", "cis'''8", "d'''8", "dis'''8", "e'''8", "f'''8", "fis'''8", "g'''8", "gis'''", "a'''8"] #for clarinet

flute_notes = ["c'8","cis'8","d'8","dis'8","e'8","f'8","fis'8","g'8","gis'8","a'8","ais'8","b'8","c''8","cis''8", "d''8", "dis''8", "e''8","f''8", "fis''8", "g''8", "gis''8", "a''8", "ais''8", "b''8","c'''8", "cis'''8", "d'''8", "dis'''8", "e'''8", "f'''8", "fis'''8", "g'''8", "gis'''", "a'''8", "ais'''8", "b'''8", "c''''8"] #for flute 

guitar_notes = ["e8", "f8","fis8","g8", "aes8", "a8","bes8", "b8", "c'8","cis'8","d'8","dis'8","e'8","f'8","fis'8","g'8","gis'8","a'8","ais'8","b'8","c''8","cis''8", "d''8", "dis''8", "e''8","f''8", "fis''8", "g''8", "gis''8", "a''8", "ais''8", "b''8","c'''8", "cis'''8", "d'''8", "dis'''8", "e'''8", "f'''8", "fis'''8", "g'''8", "gis'''", "a'''8", "ais'''8", "b'''8", "c''''8"]  #for clarinet

chordstream = songs["Giant Steps"] #user will set this
instrument = sax_notes #user
notestream = []


#clean this up!
def clean(note):
#returns clean version of input string
    cleansed = ""
    noise = ["'", "8", "7", "2", "8", "2"] 
    for char in note:
        if char not in noise:
            cleansed += char
    return cleansed

def generate_scale(kind, instrument_notes, starting_note):
    minor_pattern = [2,1,2,2,2,1,2]
    major_pattern = [2,2,1,2,2,2,1]
    dom_pattern = [2,2,1,2,2,1,2]  #the patterns that define each scale 
    if kind == "minor":
        pattern = minor_pattern
    elif kind == "major":
        pattern = major_pattern
    elif kind == "dominant":
        pattern = dom_pattern
    scale = []
    for note in instrument_notes:
        if clean(note) == starting_note:
            pointer = instrument_notes.index(note)
            i = 0
            while pointer+2 < len(instrument_notes):
                scale.append(instrument_notes[pointer])
                pointer += pattern[i%7]
                i += 1
    return scale

#parse the user's chords!
for chord in chordstream:
    if len( chord.split() ) > 1:
        for symbol in chord.split():
            starting_note = (symbol[0]).lower()
            if symbol[1:3] == "is":
                starting_note += "is"
            elif symbol[1:3] == "es":
                starting_note += "es"
            for i in range(0, len(symbol)):
                if symbol[i] == "7":
                    notes = generate_scale("major", instrument, starting_note)[0:4]
                    if random.choice([True, False]):
                        random.shuffle(notes)
                    notestream.extend(notes)
                    break
                elif symbol[i] == "i":
                    notes = generate_scale("minor", instrument, starting_note)[0:4]
                    notestream.extend(notes)
                    break
                elif symbol[i] == "a":
                    notes = generate_scale("dominant", instrument, starting_note)[0:4]
                    if random.choice([True, False]):
                        notes.reverse()
                    notestream.extend(notes)
                    break

    else:
        starting_note = (chord[0]).lower()
        if chord[1:3] == "is":
            starting_note += "is"
        elif chord[1:3] == "es":
            starting_note += "es"
        for i in range(0, len(chord)):
            if chord[i] == "7":
                notes = generate_scale("major", instrument, starting_note)[0:8]
                if random.choice([True, False]):
                    random.shuffle(notes)
                notestream.extend(notes)
                continue
            elif chord[i] == "i":
                print(chordstream)
                notes = generate_scale("minor", instrument, starting_note)[0:8]
                if random.choice([True, False]):
                    notes.reverse()
                notestream.extend(notes)
                continue
            elif chord[i] == "a":
                notes = generate_scale("dominant", instrument, starting_note)[0:8]
                if random.choice([True, False]):
                    notes.reverse()
                notestream.extend(notes)
                continue




tab = "    "

lily_file.write('\\version "2.16.0" \n ')
lily_file.write('\\header { \n')
lily_file.write(' title= "{0}" \n subtitle= "{1}" \n instrument = "{2}" \n arranger = "{3}" \n tagline = "{4}" \n '.format(title, subtitle, "Tenor Sax!", arranger, tagline))
lily_file.write('} \n')
lily_file.write('<< \n')

lily_file.write('\chords { \n')
for chord in chordstream:
    lily_file.write(tab + chord + "  \n") #output to file in nice format
lily_file.write('} \n')

lily_file.write('{ \clef treble \n')
for note in notestream[0: len(notestream)-1]:
    lily_file.write(tab + note + " \n")
lily_file.write(tab + "({0})".format(notestream[len(notestream)-1]) + "\n") #special formatting to indicate last note
lily_file.write('} \n')
lily_file.write('>>')


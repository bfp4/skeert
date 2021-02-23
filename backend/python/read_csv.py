import csv
import math

notes = {
    "A": 27.50,
    "AS": 29.14,
    "B": 30.87,
    "C": 16.35,
    "CS": 17.32,
    "D": 18.35,
    "DS": 19.45,
    "E": 20.60,
    "F": 21.83,
    "FS": 23.12,
    "G": 24.50,
    "GS": 25.96
}

def read_freq():
    resultsDict = {}

    with open("../csv/output.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            stamp = row[0]
            if row[1] == "freq":
                continue
            freq = round(float(row[1]), 2)
            if freq <= 0:
                continue

            lowest_diff = math.inf
            the_note = ""
            for note in notes:
                note_num = notes[note]
                octave = notes[note]
                counter = 0
                while octave < freq:
                    octave += octave
                    counter += 1

                note_log = math.log(note_num, octave)
                freq_log = math.log(note_num, freq)

                note_m_freq = note_log - freq_log
                freq_m_note = freq_log - note_log

                difference = note_m_freq if note_m_freq < freq_m_note else freq_m_note
                
                if difference < lowest_diff:
                    lowest_diff = difference
                    the_note = note
            resultsDict[stamp] = {}
            resultsDict[stamp]["note"] = the_note
            resultsDict[stamp]["octave"] = counter

    updatedDict = {}
    first_stamp = ""
    curr_note = {}
    for stamp in resultsDict:
        note = resultsDict[stamp]
        if curr_note == {}:
            curr_note = note
            first_stamp = stamp
        if note != curr_note:
            updatedDict[first_stamp] = {}
            updatedDict[first_stamp] = curr_note
            curr_note = note
            first_stamp = stamp

    with open("../csv/notes.csv", "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(["time", "freq", "octave"])
        for stamp in updatedDict:
            writer.writerow([stamp, updatedDict[stamp]["note"], updatedDict[stamp]["octave"]])
    return updatedDict
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
import tensorflow
import crepe
from scipy.io import wavfile
import csv
import numpy as np
    
def get_freq(filename):
    outputDict = {}
    
    sr, audio = wavfile.read(filename)
    time, frequency, confidence, activation = crepe.predict(audio, sr, viterbi=True, step_size = 10)

    for stamp in time:
        index = np.where(time == stamp)[0][0]
        outputDict[stamp] = frequency[index]

    with open("../csv/output.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["time", "freq"])
        for stamp in outputDict:
            writer.writerow([stamp, outputDict[stamp]])
    print("Done get_freq.")
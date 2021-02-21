from get_freq import get_freq
from read_csv import read_freq
from spleeter import run_spleeter

music_file = "../lilpeep.mp3"

run_spleeter(music_file)
get_freq("../output")
read_freq()
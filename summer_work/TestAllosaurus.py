from allosaurus.app import read_recognizer
from getPhones import *

# load your model by the <model name>, will use 'latest' if left empty
model = read_recognizer()

##Record file
filename = "test.wav"
create_wav_file(filename)

# run inference on <audio_file> with <lang>, lang will be 'ipa' if left empty
print(model.recognize(filename, "eng"))
import scipy.signal
import pyaudio
import wave
import sys

# number of frames to read at a time
CHUNK = 1024

# open the wave file
wf = wave.open(sys.argv[1], 'rb')

# make an instance of PyAudio
pya = pyaudio.PyAudio()

# open a PyAudio stream
stream = pya.open(format=pya.get_format_from_width(wf.getsampwidth()),
                  channels=wf.getnchannels(),
                  rate=wf.getframerate(),
                  output=True)

# read data
data = wf.readframes(CHUNK)

# do stuff in here
while len(data) > 0:
    stream.write(data)
    # Right in this section
    ##

    ##
    #
    data = wf.readframes(CHUNK)

# stop and close the stream
stream.stop_stream()
stream.close()

# close pyaudio
pya.terminate()


from pypianoroll import read, to_pretty_midi, StandardTrack
from pydub import AudioSegment, playback
import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np

sample_rate = 44100

multitrack = read("fur-elise.mid")
multitrack.trim(0, 12 * multitrack.resolution)
print(multitrack)
multitrack.plot()
plt.show()

drum_beat = np.zeros((multitrack.get_max_length(), 128), dtype=np.uint8)
drum_beat[multitrack.downbeat[:,0], 70] = 30
drum_track = StandardTrack("drum", is_drum=True, pianoroll=drum_beat, program=0)
multitrack.append(drum_track)

wave = to_pretty_midi(multitrack).fluidsynth(sf2_path="soundfont.sf2", fs=sample_rate)
plt.plot(wave)
plt.show()

sf.write("fur-elise.wav", wave, sample_rate)
segment = AudioSegment.from_wav("fur-elise.wav")
playback.play(segment)
import wave
import numpy as np
import simpleaudio as sa

_Frames = 0
_Channels = 0


with wave.open('Audio.wav', 'rb') as WaveAudioFile:
    # Get the number of frames and channels
    _Frames = WaveAudioFile.getnframes()
    _Channels = WaveAudioFile.getnchannels()
    _selfFrames = WaveAudioFile.readframes(_Frames)
Audio = np.frombuffer(_selfFrames, dtype=np.int16)
Audio = np.reshape(Audio, (_Frames, _Channels))


outputAudio = []
for i in range (len(Audio)):
    if i==0:
        continue
    List = []
    for j in range (2):
        List.append(Audio[i][j] - Audio[i-1][j])
        #_FinalAudio.append(audio_array[i][j] - audio_array[i-1][j])
    outputAudio.append(List)

Y = len(Audio)
X = len(outputAudio)
print(Y,' ',X)


nextWaveAudio = wave.open('SignalAudio.wav', 'wb')
nextWaveAudio.setnchannels(_Channels)
nextWaveAudio.setsampwidth(2)
nextWaveAudio.setframerate(44100)
nextWaveAudio.writeframes(np.array(outputAudio).tobytes())
nextWaveAudio.close()


wave_obj = sa.WaveObject.from_wave_file('SignalAudio.wav')
play_obj = wave_obj.play()
play_obj.wait_done()

import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import os

# 음성 파일 로드
base_dir = ""
file_path = 'data/SilentNight.mp3'
y, sr = librosa.load(file_path, sr=None)

# 시간축 생성
time = np.linspace(0, len(y) / sr, len(y))

# 음성 신호 시각화
plt.figure(figsize=(10, 4))
plt.plot(time, y)
plt.title('Waveform')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()
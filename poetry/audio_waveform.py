import os
import numpy as np
import matplotlib.pyplot as plt
import librosa

# 현재 스크립트 파일 기준으로 .base_dir 경로 확인
current_file_dir = os.path.dirname(os.path.abspath(__file__))
base_dir_path = os.path.abspath(os.path.join(current_file_dir, '../.base_dir'))

# .base_dir 파일이 실제로 존재하는지 확인
if not os.path.exists(base_dir_path):
    raise FileNotFoundError(f".base_dir file does not exist: {base_dir_path}")

# .base_dir 파일이 있는 디렉토리를 루트 디렉토리로 설정
BASE_DIR = os.path.abspath(os.path.dirname(base_dir_path))
print(f"BASE_DIR (relative): {os.path.relpath(BASE_DIR, start=current_file_dir)}")

# 데이터 파일 경로 설정
file_path = os.path.join(BASE_DIR, 'data', 'SilentNight.mp3')

if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found (relative): {os.path.relpath(file_path, start=current_file_dir)}")

print(f"file_path (relative): {os.path.relpath(file_path, start=current_file_dir)}")

# 음성 파일 로드
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

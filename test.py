import os
import subprocess

# folder = r"D:\桌面\whisper_conformer\datasets\ASVspoof2021\DF\ASVspoof2021_DF_eval_part00\ASVspoof2021_DF_eval\flac"

# for filename in os.listdir(folder):
#     if filename.endswith(".flac"):
#         filepath = os.path.join(folder, filename)
#         # 正确的临时文件名
#         tmpfile = filepath.replace('.flac', '_tmp.flac')
#         # ffmpeg修复到临时文件
#         cmd = f'ffmpeg -y -i "{filepath}" "{tmpfile}"'
#         subprocess.run(cmd, shell=True)
#         # 用修复后的文件覆盖原文件
#         if os.path.exists(tmpfile):
#             os.replace(tmpfile, filepath)
#             print(f"{filename} 修复并覆盖完成")
#         else:
#             print(f"{filename} 修复失败，未生成临时文件")
#         print(f"{filename} 修复并覆盖完成")

import torchaudio
import os

folder = r"D:\桌面\whisper_conformer\datasets\ASVspoof2021\DF\ASVspoof2021_DF_eval_part00\ASVspoof2021_DF_eval\flac"

for filename in os.listdir(folder):
    if filename.endswith(".flac"):
        filepath = os.path.join(folder, filename)
        try:
            waveform, sample_rate = torchaudio.load(filepath)
            print(f"{filename} 读取成功, 采样率: {sample_rate}, 波形shape: {waveform.shape}")
        except Exception as e:
            print(f"{filename} 读取失败: {e}")
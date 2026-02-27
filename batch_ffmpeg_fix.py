import os
import subprocess
from tqdm import tqdm
import time

folders = [
    r"D:\Desktop\周子皓\deepfake-whisper-features-main\datasets\ASVspoof2021\DF\ASVspoof2021_DF_eval\flac",
    
]  
# r"D:\Desktop\周子皓\deepfake-whisper-features-main\datasets\ASVspoof2021\DF\ASVspoof2021_DF_eval_part01\ASVspoof2021_DF_eval\flac",
    # r"D:\Desktop\周子皓\deepfake-whisper-features-main\datasets\ASVspoof2021\DF\ASVspoof2021_DF_eval_part02\ASVspoof2021_DF_eval\flac",
    # r"D:\Desktop\周子皓\deepfake-whisper-features-main\datasets\ASVspoof2021\DF\ASVspoof2021_DF_eval_part03\ASVspoof2021_DF_eval\flac"

# 收集所有文件路径
all_files = []
for folder in folders:
    for filename in os.listdir(folder):
        if filename.endswith(".flac"):
            all_files.append(os.path.join(folder, filename))

total_files = len(all_files)
start_time = time.time()

with tqdm(total=total_files, ncols=100, unit="file") as pbar:
    for idx, filepath in enumerate(all_files, 1):
        tmpfile = filepath.replace('.flac', '_tmp.flac')
        cmd = f'ffmpeg -y -i "{filepath}" "{tmpfile}"'
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if os.path.exists(tmpfile):
            os.replace(tmpfile, filepath)
        elapsed = time.time() - start_time
        speed = idx / elapsed if elapsed > 0 else 0
        remain = (total_files - idx) / speed if speed > 0 else 0
        pbar.set_postfix({
            "速度": f"{speed:.2f}个/秒",
            "剩余": f"{remain/60:.1f}分钟",
            "已完成": f"{idx}/{total_files}"
        })
        pbar.update(1)
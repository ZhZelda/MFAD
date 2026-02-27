### 项目使用说明 (中文)

#### 1. 准备工作

##### 1.1 Whisper

要下载训练中使用的Whisper编码器，请运行 `download_whisper.py` 脚本。

##### 1.2 数据集

下载适当的数据集：

* **ASVspoof2021 DF 子集**（请注意：我们使用的是此 `keys&metadata` 文件，目录结构请参见此文档）
* **In-The-Wild 数据集**

##### 1.3 安装依赖

我们假设您正在使用conda，并且目标环境已经激活。安装所需的依赖项：

```bash
bash install.sh
```

以下是依赖项列表：

* python=3.8
* pytorch==1.11.0
* torchaudio==0.11
* asteroid-filterbanks==0.4.0
* librosa==0.9.2
* openai whisper (git+[https://github.com/openai/whisper.git@7858aa9c08d98f75575035ecd6481f462d66ca27](https://github.com/openai/whisper.git@7858aa9c08d98f75575035ecd6481f462d66ca27))

#### 2. 支持的模型

以下是支持的模型及其名称：

* **Whisper**：SpecRNet - `whisper_specrnet`
* **Whisper + LFCC/MFCC**：SpecRNet - `whisper_frontend_specrnet`

要选择适当的前端，请在配置文件中指定。

#### 3. 预训练模型

本文中报告的所有模型都可以从[此处](#)下载。

#### 4. 配置文件

训练和评估脚本使用CLI和`.yaml`配置文件进行配置。例如：

```yaml
data:
  seed: 42

checkpoint: 
  path: "trained_models/lcnn/ckpt.pth"

model:
  name: "lcnn"
  parameters:
    input_channels: 1
    frontend_algorithm: ["lfcc"]
  optimizer:
    lr: 0.0001
    weight_decay: 0.0001
```

其他示例配置文件可在 `configs/training/` 文件夹下找到。

#### 5. 完整的训练和测试管道

要执行完整的训练和测试流程，请使用 `train_and_test.py` 脚本。

```bash
usage: train_and_test.py [-h] [--asv_path ASV_PATH] [--in_the_wild_path IN_THE_WILD_PATH] [--config CONFIG] [--train_amount TRAIN_AMOUNT] [--test_amount TEST_AMOUNT] [--batch_size BATCH_SIZE] [--epochs EPOCHS] [--ckpt CKPT] [--cpu]

参数:
  --asv_path          ASVSpoof2021 DF 根目录路径
  --in_the_wild_path  In-The-Wild 根目录路径
  --config            配置文件路径
  --train_amount      训练样本数量（默认：100000）
  --valid_amount      验证样本数量（默认：25000）
  --test_amount       测试样本数量（默认：None - 所有样本）
  --batch_size        批量大小（默认：8）
  --epochs            训练轮次（默认：10）
  --ckpt              保存模型路径（默认：'trained_models'）
  --cpu               强制使用CPU
```

#### 6. 训练流程

使用配置文件指定训练和测试的路径以及相关参数。以下是启动训练的示例命令：

```bash
python train_and_test.py --asv_path /path/to/ASVspoof2021/ --in_the_wild_path /path/to/InTheWild/ --config /path/to/config.yaml
```

#### 7. 常见问题

* **Whisper下载问题**：确保您在运行 `download_whisper.py` 脚本时有足够的网络带宽和磁盘空间。
* **数据集下载问题**：请确保您已正确下载并解压了ASVspoof2021 DF和In-The-Wild数据集。
* **训练问题**：如果遇到GPU显存不足问题，可以尝试降低批量大小或使用CPU进行训练。

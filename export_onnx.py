import torch
import os
import sys

# 请根据实际模型结构导入
from src.models.whisper_conformer import WhisperMultiFrontConformer

def main():
    # 权重文件路径
    ckpt_path = r"trained_models/model__whisper_multifront_conformer__1747204144.2161572/ckpt.pth"
    # ONNX导出路径
    onnx_path = r"trained_models/model__whisper_multifront_conformer__1747204144.2161572/model.onnx"
    device = "cpu"
    # 构建模型结构（参数需与训练时一致）
    model = WhisperMultiFrontConformer(
        input_channels=2,  # 根据训练时的input_channels
        freeze_encoder=False,  # 根据训练时配置
        frontend_algorithm="lfcc",  # 根据训练时配置
        device=device
    )
    # 加载权重
    checkpoint = torch.load(ckpt_path, map_location=device)
    if "state_dict" in checkpoint:
        model.load_state_dict(checkpoint["state_dict"])
    elif "model_state_dict" in checkpoint:
        model.load_state_dict(checkpoint["model_state_dict"])
    else:
        model.load_state_dict(checkpoint)
    model.eval()
    # 构造示例输入（需与模型forward一致）
    dummy_input = torch.randn(1, 30*16000, device=device)  # 30秒音频，单通道
    # 导出ONNX
    torch.onnx.export(
        model,
        dummy_input,
        onnx_path,
        export_params=True,
        opset_version=14,
        do_constant_folding=True,
        input_names=["input"],
        output_names=["output"],
        dynamic_axes={"input": {0: "batch_size", 1: "audio_length"}, "output": {0: "batch_size"}}
    )
    print(f"ONNX模型已导出到: {onnx_path}")

if __name__ == "__main__":
    main()
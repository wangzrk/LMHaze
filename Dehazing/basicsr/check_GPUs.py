import torch

if torch.cuda.is_available():
    for i in range(torch.cuda.device_count()):
        print(f"Device ID: {i}, Device Name: {torch.cuda.get_device_name(i)}")
else:
    print("CUDA is not available. No GPU devices found.")

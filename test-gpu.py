import torch
print(torch.__version__)  # Should show 2.7.0 or similar
print(torch.cuda.is_available())  # Should return True
print(torch.cuda.get_device_name(0))  # Should show your GPU

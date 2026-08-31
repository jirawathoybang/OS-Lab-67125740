# ==========================================
# OS-Lab 01: System Profiler
# Student ID: [Enter your ID here]
# ==========================================
import os
import psutil
import platform

print(f"OS Name: {platform.system()} {platform.release()}")
print(f"Number of CPU Cores: {psutil.cpu_count(logical=True)}")
print(f"Total RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB")

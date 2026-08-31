# ipc_pipe.py
import os
import time

def main():
    r, w = os.pipe() 
    pid = os.fork()

    if pid > 0: # PARENT PROCESS
        os.close(w)
        r_file = os.fdopen(r)
        print(f"[Trainer PID:{os.getpid()}] Waiting for data from DataLoader...")
        data = r_file.read() # รอรอบข้อมูล
        print(f"[Trainer PID:{os.getpid()}] Received Data: '{data}'")
        print(f"[Trainer PID:{os.getpid()}] Training complete.")
        os.wait()

    elif pid == 0: # CHILD PROCESS
        os.close(r)
        w_file = os.fdopen(w, 'w')
        print(f"  -> [DataLoader PID:{os.getpid()}] Loading image from disk...")
        time.sleep(2) # จำลอง I/O delay 2 วินาที
        image_data = "Image_Tensor_Batch_01"
        print(f"  -> [DataLoader PID:{os.getpid()}] Sending data through OS Pipe...")
        w_file.write(image_data)
        w_file.close()

if __name__ == "__main__":
    main()
# producer_consumer.py
import threading
import time
import random

BUFFER_SIZE = 5
buffer = [None] * BUFFER_SIZE
in_index = 0
out_index = 0

mutex = threading.Lock()               # ล็อกเพื่อป้องกัน Critical Section
empty = threading.Semaphore(BUFFER_SIZE) # นับช่องว่างใน Buffer
full = threading.Semaphore(0)            # นับช่องที่มีข้อมูลแล้ว

def data_loader_producer():
    global in_index
    for i in range(10):
        item = f"Image_Batch_{i}"
        time.sleep(random.uniform(0.1, 0.3))

        empty.acquire() # รอถ้า Buffer เต็ม
        mutex.acquire() # ล็อก Buffer

        # --- CRITICAL SECTION ---
        buffer[in_index] = item
        print(f"[Producer] Loaded: {item} into slot {in_index}")
        in_index = (in_index + 1) % BUFFER_SIZE
        # ------------------------

        mutex.release() # ปลดล็อก
        full.release()  # ส่งสัญญาณว่ามีข้อมูลใหม่แล้ว

def gpu_trainer_consumer():
    global out_index
    for i in range(10):
        full.acquire()  # รอถ้า Buffer ว่างเปล่า
        mutex.acquire() # ล็อก Buffer

        # --- CRITICAL SECTION ---
        item = buffer[out_index]
        print(f"    -> [Consumer] Training on: {item} from slot {out_index}")
        out_index = (out_index + 1) % BUFFER_SIZE
        # ------------------------

        mutex.release() # ปลดล็อก
        empty.release() # ส่งสัญญาณว่ามีช่องว่างเพิ่มขึ้น

        time.sleep(random.uniform(0.2, 0.5))

def main():
    print("--- Starting ML Data Pipeline (Bounded Buffer) ---")
    producer_thread = threading.Thread(target=data_loader_producer)
    consumer_thread = threading.Thread(target=gpu_trainer_consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
    print("--- Pipeline Execution Completed Successfully ---")

if __name__ == "__main__":
    main()
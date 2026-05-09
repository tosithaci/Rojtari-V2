import subprocess
import time
import json
import requests
from concurrent.futures import ThreadPoolExecutor
from prometheus_client import start_http_server, Gauge

# --- KONFIGURIMI ---
TOKEN = "8638165258:AAHz08mNPPlNaljdDTrfZU0_tLJXYyi5VMY"
CHAT_ID = "5800020502"
JSON_PATH = "/app/shared_data/status.json"
METRICS_PORT = 8000 

devices = {
    "Google DNS": "8.8.8.8",
    "Cloudflare": "1.1.1.1",
    "Gateway": "192.168.1.1",
    "Telefoni": "192.168.100.213",
    "localhost": "127.0.0.1"
}

# 1 = ONLINE, 0 = OFFLINE
device_status_metric = Gauge('device_status', 'Statusi i pajisjes (1=Online, 0=Offline)', ['device_name', 'ip_address'])

last_status = {}

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": CHAT_ID, "text": msg}, timeout=5)
    except:
        pass

def check_device(name_ip):
    name, ip = name_ip
    res = subprocess.run(['ping', '-c', '1', '-W', '1', ip], capture_output=True)
    status = "ONLINE" if res.returncode == 0 else "OFFLINE"
    
    # Update Prometheus
    metric_value = 1 if status == "ONLINE" else 0
    device_status_metric.labels(device_name=name, ip_address=ip).set(metric_value)
    
    global last_status
    if name in last_status and last_status[name] != status:
        icon = "✅" if status == "ONLINE" else "🚨"
        send_telegram(f"{icon} {name} ({ip}) është tani {status}")
    
    last_status[name] = status
    return {
        "name": name, 
        "ip": ip, 
        "status": status, 
        "last_update": time.strftime("%H:%M:%S")
    }

def monitor():
    start_http_server(METRICS_PORT)
    print(f"📊 Prometheus metrics server u nis në portën {METRICS_PORT}")
    send_telegram("🚀 Rojtari V2 (Observability Mode) u nis!")
    
    while True:
        with ThreadPoolExecutor(max_workers=len(devices)) as executor:
            results = list(executor.map(check_device, devices.items()))
        
        try:
            with open(JSON_PATH, "w") as f:
                json.dump(results, f, indent=4)
        except Exception as e:
            print(f"Gabim JSON: {e}")
            
        time.sleep(10)

if __name__ == "__main__":
    monitor()
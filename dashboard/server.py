#!/usr/bin/env python3
import json
import subprocess
import time
from datetime import datetime

from flask import Flask, jsonify, send_from_directory
import psutil

app = Flask(__name__)
HOST = "0.0.0.0"
PORT = 8080
THERMAL_PATH = "/sys/class/thermal/thermal_zone0/temp"


def get_cpu_temp():
    try:
        with open(THERMAL_PATH) as f:
            return round(int(f.read().strip()) / 1000.0, 1)
    except (OSError, ValueError):
        return 0.0


def get_throttle_status():
    try:
        result = subprocess.run(
            ["vcgencmd", "get_throttled"],
            capture_output=True,
            text=True,
            timeout=2,
        )
        if result.returncode == 0 and "0x0" in result.stdout:
            return "CLEAN"
        if result.returncode == 0:
            return "THROTTLED"
        return "UNKNOWN"
    except (OSError, subprocess.SubprocessError):
        return "UNKNOWN"


def get_tailscale_status():
    try:
        result = subprocess.run(
            ["tailscale", "status", "--json"],
            capture_output=True,
            text=True,
            timeout=4,
        )
        if result.returncode != 0:
            return {"online": False, "error": "not running"}
        data = json.loads(result.stdout)
        if data.get("BackendState") == "Running":
            peers = data.get("Peer") or {}
            return {
                "online": True,
                "peers": len(peers) if isinstance(peers, dict) else 0,
            }
        return {
            "online": False,
            "error": data.get("BackendState") or "not connected",
        }
    except (OSError, subprocess.SubprocessError, json.JSONDecodeError) as e:
        return {"online": False, "error": str(e)}


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/api/status")
def api_status():
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    net = psutil.net_io_counters()
    return jsonify(
        {
            "timestamp": datetime.now().isoformat(),
            "system": {
                "cpu_percent": round(psutil.cpu_percent(interval=0.3), 1),
                "cpu_count": psutil.cpu_count(),
                "memory_total_gb": round(mem.total / (1024**3), 1),
                "memory_used_gb": round(mem.used / (1024**3), 1),
                "memory_percent": mem.percent,
                "disk_total_gb": round(disk.total / (1024**3), 1),
                "disk_used_gb": round(disk.used / (1024**3), 1),
                "disk_percent": disk.percent,
                "temperature": get_cpu_temp(),
                "throttle_status": get_throttle_status(),
                "uptime_seconds": int(time.time() - psutil.boot_time()),
            },
            "network": {
                "bytes_sent": net.bytes_sent,
                "bytes_recv": net.bytes_recv,
            },
            "tailscale": get_tailscale_status(),
            "openclaw": {"status": "running"},
        }
    )


if __name__ == "__main__":
    print(f"ELMER Dashboard starting on {HOST}:{PORT}")
    app.run(host=HOST, port=PORT, threaded=True)

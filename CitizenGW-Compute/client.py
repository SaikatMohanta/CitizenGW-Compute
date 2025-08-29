"""
CitizenGW-Compute: Client Prototype v-1.0.0
--------------------------------------------------------------------
This python script monitors for GW alerts, runs deterministic workloads,
and logs throughput anomalies for distributed correlation.

Usage:
    python client.py --server http://127.0.0.1:5000/upload
"""

import argparse
import time
import json
import csv
import os
import requests
import numpy as np

try:
    import torch
except ImportError:
    torch = None


def run_dummy_ann(iterations=1000, size=512):
    """
    Run a deterministic ANN-like workload.
    If PyTorch is installed, use it; otherwise fallback to NumPy.
    """
    if torch:
        x = torch.ones((size, size))
        w = torch.eye(size)
        y = x @ w
        for _ in range(iterations):
            y = torch.relu(y @ w)
        return y.sum().item()
    else:
        x = np.ones((size, size))
        w = np.eye(size)
        y = x @ w
        for _ in range(iterations):
            y = np.maximum(y @ w, 0)
        return float(np.sum(y))


def log_result(filename, data):
    """
    Append a row to CSV and JSON log files.
    """
    csvfile = filename + ".csv"
    jsonfile = filename + ".jsonl"

    # Write CSV
    file_exists = os.path.isfile(csvfile)
    with open(csvfile, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

    # Write JSON
    with open(jsonfile, "a") as f:
        f.write(json.dumps(data) + "\n")


def upload_to_server(server_url, data):
    """
    Upload log data to a central server.
    """
    try:
        resp = requests.post(server_url, json=data, timeout=5)
        print(f"Upload response: {resp.status_code}")
    except Exception as e:
        print(f"Upload failed: {e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--server", type=str, default=None,
                        help="Central server URL to upload results")
    parser.add_argument("--alert-endpoint", type=str, default=None,
                        help="Optional GW alert API endpoint")
    args = parser.parse_args()

    print("CitizenGW-Compute client-script started. Waiting for GW event alert...")

    while True:
        # Placeholder: poll LIGO/Virgo or custom API
        if args.alert_endpoint:
            try:
                #r = requests.get(args.alert_endpoint, timeout=5)
                import requests
                r = requests.get("https://gwosc.org/api/v2/runs", timeout=5)
                r.json()
                if r.status_code == 200 and "event" in r.text.lower():
                    print("GW ALERT received!")
                    proceed = input("Switch system to logging mode? (y/n): ")
                    if proceed.lower() == "y":
                        start_time = time.time()
                        result = run_dummy_ann()
                        duration = time.time() - start_time
                        data = {
                            "timestamp": time.time(),
                            "duration": duration,
                            "result": result
                        }
                        log_result("gw_logs", data)
                        if args.server:
                            upload_to_server(args.server, data)
            except Exception as e:
                print(f"Error! Alert check failed: {e}")

        time.sleep(10)


if __name__ == "__main__":
    main()

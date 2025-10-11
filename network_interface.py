# network_interface.py
# Python interface for network operations (Termux compatible)

import sys
import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        print(f"Status: {response.status_code}")
        print(response.text[:200])  # Print first 200 chars
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fetch_data(sys.argv[1])
    else:
        print("Usage: python3 network_interface.py <url>")

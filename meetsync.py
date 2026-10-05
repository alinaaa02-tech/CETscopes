import requests
from bs4 import BeautifulSoup

def sync_data(url="https://cetscope.ai.studio/"):
    print(f"Syncing data from {url}...")
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("Successfully connected and synced.")
            return response.text
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error during sync: {e}")

if __name__ == "__main__":
    sync_data()

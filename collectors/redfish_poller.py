import requests
import json
import time

REDFISH_ENDPOINT = "https://example.com/redfish/v1"
USERNAME = "your_username"
PASSWORD = "your_password"

def get_data(endpoint):
    url = f"{REDFISH_ENDPOINT}/{endpoint}"
    try:
        response = requests.get(url, auth=(USERNAME, PASSWORD), verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def poll_telemetry():
    thermal_data = get_data("/Chasis/1/Thermal")
    power_data = get_data("/Chasis/1/Power")
    cpu_data = get_data("/Systems/1/Processors")

    print("Telemetry Data:")
    if thermal_data:
        print("Thermal Data:", json.dumps(thermal_data, indent=2))
    if power_data:
        print("Power Data:", json.dumps(power_data, indent=2))
    if cpu_data:
        print("CPU Data:", json.dumps(cpu_data, indent=2))

def main():
    while True:
        poll_telemetry()
        time.sleep(60)  # Poll every 60 seconds
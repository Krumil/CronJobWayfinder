import requests
import os

def update_addresses():
    api_url = os.environ.get('API_URL', 'https://promptcachingdashboardserver.onrender.com/update_addresses')
    try:
        response = requests.post(api_url)
        if response.status_code == 200:
            print("Address update completed successfully")
        else:
            print(f"Failed to update addresses. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    update_addresses()
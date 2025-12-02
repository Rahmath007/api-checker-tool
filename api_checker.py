import requests

def check_api(url):
    try:
        response = requests.get(url, timeout=5)
        print("\nURL:", url)
        print("Status code:", response.status_code)

        if response.status_code == 200:
            print("API is working ✅")
        else:
            print("API returned a problem ⚠️")

    except requests.exceptions.Timeout:
        print("Request timed out ⏱")
    except requests.exceptions.ConnectionError:
        print("Connection error ❌")
    except Exception as e:
        print("Unexpected error:", e)

if __name__ == "__main__":
    url = input("Enter API URL: ")
    check_api(url)
    
    
    
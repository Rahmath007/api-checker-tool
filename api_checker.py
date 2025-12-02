import requests

# url = "https://api.github.com"

# repsonse = requests.get(url)

# print("Status Code:",repsonse.status_code)


def check_api(url):
    try:
        repsonse = requests.get(url, timeout=5)
        print("URL:", url)
        print("Status Code:", repsonse.status_code)
        
        
        if repsonse.status_code == 200:
            print("API is working properly.")
        else:
            print("API returned an error.")
            
    
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API.")
    except Exception as e:
        print("An unexpected error occurred:") 
    
    
if __name__ == "__main__":
    url = input("Enter the API URL to check: ")
    check_api(url)
    
    
    
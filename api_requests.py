import requests
import json
import time

def send_getrequest(req_url, f_name):
    try:
        headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)", "Cookie": "abc123xyz"}
        req1 = requests.get(req_url, headers= headers)
        with open(f_name, "w") as file:
            file.write(req1.text)
        
    except Exception as e:
        print(f"1st exception caught: {e}")

def send_postrequest(req_url):
    try:
        payload = json.dumps({
          "name": "Apple MacBook Pro 16",
          "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
          }
        })
        headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)", "Content-Type": "application/json"}
        for i in range(3):
            req1 = requests.post(req_url, data=payload, headers=headers)
            print(f"{req1.status_code}")
            if req1.status_code != 200:
                time.sleep(3)
            else:
                break

    except Exception as e:
        print(f"2nd exception caught: {e}")

def print_request(f_name):
    try:
        with open(f_name, "r") as file:
            api_data = json.loads(file.read())
            
        for i in api_data:
            for key,value in i.items():
                print(f"{key}:{value}")
            
    except Exception as e:
        print(f"3rd exception caught: {e}")
        
if __name__ == "__main__":
    url = "https://api.restful-api.dev/objects"
    f_name = "api_req_res.txt"
    send_postrequest(url)
    send_getrequest(url, f_name)
    print_request(f_name)

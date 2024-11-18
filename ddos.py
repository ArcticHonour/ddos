import requests
import time

def send_requests_continuously(ip, port, endpoint, data=None, delay=1):
    counter = 0  # Initialize the request counter
    url = f"http://{128.116.119.4}:{80}/"  # Construct the URL
    
    while True:
        try:
            counter += 1
            print(f"Sending Request #{counter} to {url}...")
            
            # Send a GET request (or POST if data is provided)
            if data:
                response = requests.post(url, json=data)
            else:
                response = requests.get(url)
            
            # Check if the response status code is 200
            if response.status_code != 200:
                print(f"Error: Request #{counter} failed with Status Code {response.status_code}")
                print(f"Response Body: {response.text}")
                break  # Stop the loop if status code is not 200

            # Print the successful response details
            print(f"Response #{counter}: Status Code {response.status_code}")
            print(f"Response Body: {response.text}\n")
            
            # Optional delay between requests
            time.sleep(delay)
        except requests.RequestException as e:
            print(f"An error occurred on Request #{counter}: {e}")
            break  # Stop the loop if there is a request exception
        except KeyboardInterrupt:
            print("\nStopped by user.")
            break  # Stop the loop on user interruption

if __name__ == "__main__":
    # Replace with the target IP, port, endpoint, and optional data
    target_ip = "127.0.0.1"
    target_port = 8080
    endpoint = ""  # Specify an endpoint, e.g., 'api/v1/resource'
    data_to_send = None  # Use None for GET requests or set as {"key": "value"}
    delay_between_requests = 0
    
    send_requests_continuously(target_ip, target_port, endpoint, data_to_send, delay_between_requests)

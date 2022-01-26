from prometheus_client import start_http_server, Summary
import random
import time
import requests 

# Create a metric to track time spent and requests made.
response = reqs.get('https://httpstat.us') 
print(response.status_code) 

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


@REQUEST_TIME.time()
def sample_request(t):
    time.sleep(t)

if __name__ == '__main__':
    
    start_http_server(8000)
    
    while True:
        sample_request(random.random())
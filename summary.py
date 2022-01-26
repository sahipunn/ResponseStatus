from prometheus_client import start_http_server, Summary
import random
import time
import requests 

# Metric for processing time
response = reqs.get('https://httpstat.us') 
print(response.status_code) 

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


@REQUEST_TIME.time()
def sample_request(t):
    time.sleep(t)

if __name__ == '__main__':
    
    # metrics are located at https://locahost:8000
    start_http_server(8000)
    
    while True:
        sample_request(random.random())

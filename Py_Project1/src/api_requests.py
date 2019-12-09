import requests
import requests_cache
import json

requests_cache.install_cache('demo_cache')
#requests_cache.clear()

def get_request(url, params, use_cache=False):
    
    if not use_cache: requests_cache.clear()
    resp = requests.get(url, params=params)
    print(f"From cache: {resp.from_cache}, {resp.url}")
    return resp.json()  # Return a python object (a list of dictionaries in this case)

parameters = {"term": "Miami", "entity": "podcast", "max": "3"}
url = "https://itunes.apple.com/search"
response = get_request(url, parameters, True)
 
[print(result['trackName']) for result in response['results']]

parameters = {'rel_rhy': 'funny'}
resp = get_request("https://api.datamuse.com/words", parameters, True)
[print(v['word']) for v in resp]

#py_data = json.loads(iTunes_response.text)
# for r in py_data['results']:
#     print(r['trackName'])
#[print(result['trackName']) for result in py_data['results']]


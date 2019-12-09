import requests
import requests_cache

requests_cache.install_cache('demo_cache')
#requests_cache.clear()
# import statements for necessary Python modules
import sys, json, requests

def get_rhymes(words, use_cache=False):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["max"] = "3" # get at most n results
    
    new_lst, rhy_lst = [], []
    new_lst = words.strip('.').split()

    #print(resp.from_cache)
    for word in new_lst:
        if not use_cache: requests_cache.clear()
        params_diction["rel_rhy"] = word
        resp = requests.get(baseurl, params=params_diction)

        word_ds = resp.json()  # Return a python object (a list of dictionaries in this case)
        rhy_lst.append([d['word'] for d in word_ds])
    return rhy_lst

#requests_cache.clear()

parameters = {"term": "Miami", "entity": "podcast", "max": "3"}
iTunes_response = requests.get("https://itunes.apple.com/search", params = parameters)
print(f"From cache: {iTunes_response.from_cache}")

py_data = json.loads(iTunes_response.text)
# for r in py_data['results']:
#     print(r['trackName'])
[print(result['trackName']) for result in py_data['results']]
sys.exit()

#lst = list(map(lambda word: get_rhymes(word), [word for word in ['Jack be nimble be quick.']]))
para = 'Jack be nimble be quick.'
print([get_rhymes(word) for word in [para]])


# it's not found in the permanent cache
kval_pairs = {'rel_rhy': 'funny'}
res = requests.get("https://api.datamuse.com/words", params=kval_pairs)
print('Cache', res.from_cache)
results = res.json()
print(res.text)

#print([v for value in results for (k,v) in value.items() if k == 'word'])

print([v['word'] for v in results])
#res = requests.get("https://api.datamuse.com/words", params=kval_pairs)
#print(res.text, res.from_cache)

#res = requests.get("https://api.datamuse.com/words", params=kval_pairs)
# print(res.text, res.from_cache)

#res = requests.get("https://api.datamuse.com/words?rel_rhy=happy", permanent_cache_file="datamuse_cache.txt")
# print(res.text[:100])
# 
# 
# # this time it will be found in the temporary cache
# res = web_requests_caching.get("https://api.datamuse.com/words?rel_rhy=happy", permanent_cache_file="datamuse_cache.txt")
# # This one is in the permanent cache.
# res = web_requests_caching.get("https://api.datamuse.com/words?rel_rhy=funny", permanent_cache_file="datamuse_cache.txt")
# 
# web_requests_caching.
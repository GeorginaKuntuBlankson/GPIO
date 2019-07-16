import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=ghana&'
       'apiKey=58cf5cb108cb493eb6e82291ad58c3f6')
requests = requests.get(url)
print (requests())

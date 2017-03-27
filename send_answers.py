#Import the necessary libraries to POST the answers in the specified host
import requests
import json

#Type the host you are going to print the answers
url='http://localhost:9200/edu/quiz/4'

#Get the url
r = requests.get(url)

#Open the json
with open('introduction_quiz.json') as df:       
        ans = json.load(df)

#Send the json to the specified url
r = requests.post(url, data =json.dumps(ans))
a = requests.get(url+'?pretty')
print(a.text)


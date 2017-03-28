#Import the necessary libraries to POST the answers in the specified host
import requests
import json

#Type the host you are going to print the answers
url=''

#Get the url
r = requests.get(url)

#Open the json
with open('introduction_quiz.json') as df:       
        ans = json.load(df)

#Send the json to the specified url
r = requests.post(url, data =json.dumps(ans))

#Get the values just entered in order to check if it was done correctly but you have to put the full URL
#a = requests.get(url)
#answers = a.text
#Print the answers in the console
#print(answers)

#Print the result of the POST
print(r.text)


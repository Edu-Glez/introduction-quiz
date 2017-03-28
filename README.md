# introduction-quiz
Answers to the questions of the json in Jorge's repo and the script to send a POST to a given host
# Instructions
* The script uses the json and requests libraries which are a default after python 2.7.5 so there is no need to install them. If there is a problem, create a virtual environment with python 3.6 adding the two libraries:
  * sudo virtualenv -p python3.6 env
  * source env/bin/activate
  * sudo pip install json
  * sudo pip install requests
* The script needs an URL that has to be introduced by the user in the location he wants the json info to be stored
* The script outputs the json that was posted, if you want to see it "pretty" write the command like this "python send_answers.py | python -m json.tool"


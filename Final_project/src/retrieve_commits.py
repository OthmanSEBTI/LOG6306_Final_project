import requests
import json
import csv

def commits_extraction (pattern) :
    url = "https://api.github.com/search/commits"
    parameters = {"q": "org:microsoft " + pattern +" pattern"}
    response = requests.get(url, params=parameters)
    data = json.loads(response.text)['items']

    csv_file = open('/mnt/c/Users/Othman/Desktop/TP-LOG6306/Final_project/Data_collection/commits-'+pattern+'.csv', mode='w')  
    writer = csv.writer(csv_file)
    writer.writerow(['sha','message', 'html_url','repository_id', 'repository_full_name','repository_private','repository_fork'])

    for commit in data:
        writer.writerow([commit['sha'],commit['commit']['message'].replace('\n','/').replace('\r','/'), commit['html_url'], commit['repository']['id'], commit['repository']['full_name'],commit['repository']['private'],commit['repository']['fork']])


for pattern in [
                'command','strategy','mediator']:
  
    commits_extraction(pattern)
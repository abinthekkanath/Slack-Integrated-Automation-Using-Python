from slackclient import SlackClient
import time
import os
import requests


token = 'xoxp-24300212688-687202158725-772714060887-daa243e3f375d477c854b38fd5f1b7d2'
# token = os.environ.get('SLACKBOT_LUMBERGH_TOKEN')


def runner():

    sc = SlackClient(token)
    request = sc.api_call("users.list")
    identification = {}
    if request['ok']:
        for item in request['members']:
            identification[item['id']] = item['name']

    if sc.rtm_connect():

        while True:
            events = sc.rtm_read()

            if events:

                for event in events:

                    if ('channel' in event and event.get('files') and event.get('type') == 'message'):
                        print(event)

                        channel = event['user']
                        directory = identification[channel]

                        if not os.path.exists(directory):
                            os.makedirs(directory)
                        try:
                            file_id = event['files'][0]['id']
                        except:
                            file_id = ''

                        url = "https://slack.com/api/files.info"
                        r = requests.get(
                            url, {"token": token, "file": file_id})
                        r.raise_for_status
                        response = r.json()
                        assert response["ok"]
                        file_name = response["file"]["name"]
                        file_url = response["file"]["url_private"]

                        # download file
                        r = requests.get(file_url, headers={
                                         'Authorization': 'Bearer %s' % token})
                        r.raise_for_status
                        file_data = r.content   # get binary content

                        # save file to disk
                        file_name = os.getcwd()+'/'+directory + '/' + \
                            event['files'][0]['name']
                        with open(file_name, 'w+b') as f:
                            f.write(bytearray(file_data))

                #         # os.system("wget "+url+" -P "+channel)

                        message = "ith enthina"

                        sc.api_call(
                            'chat.postMessage',
                            channel=channel,
                            text=message,
                            as_user='true:')


runner()

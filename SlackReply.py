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
    # link = '<https://cdn.meme.am/instances/400x/33568413.jpg|That would be great>'
    WishingList = ['hy', 'hello', 'bro', 'hi', 'abin', 'da', 'daa', 'hai']
    oklist = ['ok', 'k', 'kk']
    Badwords = ['patti', 'thendi', 'oole', 'ninte thala']
    podaList = ['poda', 'venda', 'enthada']
    killList = ['kill', 'stop']
    if sc.rtm_connect():
        while True:
            events = sc.rtm_read()

            if events:
                # print(events)
                for event in events:
                    if (
                        'channel' in event and
                        'text' in event and
                            event.get('type') == 'message' and event['user'] != 'UL75Y4NMB'):
                        channel = event['channel']
                        text = event['text'].lower()

                        # sc.api_call('chat.postMessage', channel=channel,
                        #             text=text, as_user=True)

                        if text in WishingList:
                            message = "Entha karyam..?"
                            sc.api_call(
                                'chat.postMessage',
                                channel=channel,
                                text=message,
                                as_user='true:')
                        if text in Badwords:
                            message = "Athu thanum thnate mattolum ..."
                            sc.api_call('chat.postMessage',
                                        channel=channel,
                                        text=message,
                                        as_user='true:')
                        if text in oklist:
                            message = "Double Ok"
                            sc.api_call(
                                'chat.postMessage',
                                channel=channel,
                                text=message,
                                as_user='true:')
                        if text in podaList:
                            message = "than podo"
                            sc.api_call(
                                'chat.postMessage',
                                channel=channel,
                                text=message,
                                as_user='true:')
                        if 'nirth' in text:
                            message = "thaniku venamengil than nirthi podo"
                            sc.api_call(
                                'chat.postMessage',
                                channel=channel,
                                text=message,
                                as_user='true:')
                        if text in killList:
                            message = "urappano..?..njan killum.."
                            sc.api_call(
                                'chat.postMessage',
                                channel=channel,
                                text=message,
                                as_user='true:')
                        if 'run' in text:
                            if len(text.split()) == 1:
                                message = "Entha Run cheyande..?"
                                sc.api_call(
                                    'chat.postMessage',
                                    channel=channel,
                                    text=message,
                                    as_user='true:')
                            elif len(text.split()) == 2:
                                message = "PATH kittiyal kollamayirunu\n also Tor or Storm ..?"
                                sc.api_call(
                                    'chat.postMessage',
                                    channel=channel,
                                    text=message,
                                    as_user='true:')
                            # else:
                            #     message = "oru ..5mts"
                            #     sc.api_call(
                            #         'chat.postMessage',
                            #         channel=channel,
                            #         text=message,
                            #         as_user='true:')
                        # elif 'missing' in text:
                        #     message = "Don't Worry I'm on it.."

    else:
        print('Connection failed, invalid token?')


while(True):
    try:
        runner()
    except:
        print("Connection Error")
        time.sleep(3)
        runner()

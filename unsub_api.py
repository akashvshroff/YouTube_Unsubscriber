import shelve
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow


def load():
    s = shelve.open(r'C:\Users\akush\Desktop\Programming\Datasets\Takeout\unsub_data.db')
    try:
        unsub = s['data']
    finally:
        s.close()
    return (unsub)


def unsub(unsub_list):
    i = 1
    for name, id in unsub_list.items():
        req = youtube.subscriptions().delete(id=id)
        req.execute()
        print("{}. {} unsubscribed".format(i, name))
        i += 1


    api_key = "AIzaSyDO-fRc6vZFpgxu2Rzw-Q-MwDQlpaCDtaY"
if __name__ == '__main__':

    CLIENT_SECRET_FILE = r'C:\Users\akush\Desktop\Programming\Projects\Automation\YouTube\client_secret.json'
    SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_console()
    youtube = build('youtube', 'v3', developerKey=api_key, credentials=credentials)
    unsub_list = load()
    unsub(unsub_list)

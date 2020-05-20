import json
import os
import shelve

def watched_json(filename):
    with open(filename, errors = 'ignore') as f:
        data = json.load(f)
    watched = {} #watched videos in the past 30 days
    for video in data:
        try:
            name = video['subtitles'][0]["name"]
            watched[name] = watched.get(name,0) + 1
        except:
            continue
    keep = {}
    for ch in watched.keys():
        if not watched[ch] <= 2:
            keep[ch] = watched[ch]
    sub_to_rem(keep)

def sub_to_rem(watched):
    unsub = {}
    with open('subscriptions.json', errors = 'ignore' ) as fhand:
        data = json.load(fhand)
    for sub in data:
        try:
            name = sub['snippet']["title"]
            id = sub["id"]
            if not name in watched.keys():
                unsub[name] = id
        except:
            continue
    print(len(unsub))
    print(unsub)
    shelve_data(unsub)

def shelve_data(unsubs):
    s = shelve.open(r'C:\Users\akush\Desktop\Programming\Datasets\Takeout\unsub_data.db')
    try:
        s['data'] = unsubs
    finally:
        s.close()


if __name__ == '__main__':
    os.chdir(r'C:\Users\akush\Desktop\Programming\Datasets\Takeout')
    fname = 'watch-history.json'
    watched_json(fname)

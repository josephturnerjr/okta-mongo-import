import pymongo
import sys
import simplejson as json
import datetime

if __name__ == "__main__":
    client = pymongo.MongoClient()
    db = client.adobe
    events = db.events
    events.create_index("published")
    events.create_index("actors.login")
    events.create_index("actors.ipAddress")
    events.create_index("targets.login")
    events.create_index("action.objectType")
    for filename in sys.stdin:
        with open(filename) as f:
            print "Importing file %s" % f
            blob = json.loads(f.read())
            for h in blob:
                h['published'] = datetime.strptime(h['published'], "%Y-%m-%dT%H:%M:%S.%fZ")
            events.insert_many(blob)

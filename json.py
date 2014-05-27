import urllib2
import simplejson

url = "https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name=twitterapi&count=2"

if __name__ == "__main__":
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    f = opener.open(req)
    json = simplejson.load(f)

    for item in json:
        print item.get('created_at')
        print item.get('test')


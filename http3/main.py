from pprint import pprint
from datetime import datetime
from datetime import timedelta
import time
import requests


def find_questions():
    todate = datetime.now().date()
    fromdate = todate - timedelta(2)
    todate = str(round(time.mktime(todate.timetuple())))
    fromdate = str(round(time.mktime(fromdate.timetuple())))

    url = 'https://api.stackexchange.com/2.3/questions'
    params = {'todate': todate, 'fromdate': fromdate, 'tagged': 'Python', 'order': 'desc',
              'sort': 'creation', 'site': 'stackoverflow'}
    r = requests.get(url, params=params)
    return r.json()


if __name__ == '__main__':
    pprint(find_questions())

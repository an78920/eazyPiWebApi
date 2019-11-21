from EazyApi import *
from EazyApi.WebID import *


class Interpoolated:
    def __init__(self, webid):
        self._webid = webid
        self._startTime = None
        self._endTime = None
        self._interval = None
        self._params = {}

    @property
    def startTime(self):
        return self._startTime

    @startTime.setter
    def startTime(self, value):
        self._startTime = value
        self._params.update({
            'startTime': value
        })

    @property
    def endTime(self):
        return self._endTime

    @endTime.setter
    def endTime(self, value):
        self._endTime = value
        self._params.update({
            'endTime': value
        })

    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, value):
        self._interval = value
        self._params.update({
            'interval': value
        })

    def query(self):
        url = endpoint + f'/streams/{self._webid}/interpolated'
        resp = eazy_requests(url, self._params)
        return resp.json()


class Recorded:
    def __init__(self, webid):
        self._webid = webid
        self._startTime = None
        self._endTime = None
        self._maxCount = None
        self._params = {}

    @property
    def startTime(self):
        return self._startTime

    @startTime.setter
    def startTime(self, value):
        self._startTime = value
        self._params.update({
            'startTime': value
        })

    @property
    def endTime(self):
        return self._endTime

    @endTime.setter
    def endTime(self, value):
        self._endTime = value
        self._params.update({
            'endTime': value
        })

    @property
    def maxCount(self):
        return self._maxCount

    @maxCount.setter
    def maxCount(self, value):
        self._maxCount = value
        self._params.update({
            'maxCount': value
        })

    def query(self):
        url = endpoint + f'/streams/{self._webid}/recorded'
        resp = eazy_requests(url, self._params)
        return resp.json()


class Summary:
    def __init__(self, webid):
        self._webid = webid
        self._startTime = None
        self._endTime = None
        self._summaryDuration = None
        self._summaryType = None
        self._params = {}

    @property
    def startTime(self):
        return self._startTime

    @startTime.setter
    def startTime(self, value):
        self._startTime = value
        self._params.update({
            'startTime': value
        })

    @property
    def endTime(self):
        return self._endTime

    @endTime.setter
    def endTime(self, value):
        self._endTime = value
        self._params.update({
            'endTime': value
        })

    @property
    def summaryDuration(self):
        return self._summaryDuration

    @summaryDuration.setter
    def summaryDuration(self, value):
        self._summaryDuration = value
        self._params.update({
            'summaryDuration': value
        })

    @property
    def summaryType(self):
        return self._summaryType

    @summaryType.setter
    def summaryType(self, value):
        self._summaryType = value
        self._params.update({
            'summaryType': value
        })

    def query(self):
        url = endpoint + f'/streams/{self._webid}/summary'
        resp = eazy_requests(url, self._params)
        return resp.json()


class Value:
    def __init__(self, webid):
        self._webid = webid

    def query(self):
        url = endpoint + f'/streams/{self._webid}/value'
        resp = eazy_requests(url)
        return resp.json()


if __name__ == '__main__':
    webid = WebID.points('3QT-PI-101-PL')

    interpolated = Interpoolated(webid)
    print(interpolated.query())

    recorded = Recorded(webid)
    print(recorded.query())

    value = Value(webid)
    print(value.query())

    summary = Summary(webid)
    summary.summaryDuration = '6h'
    summary.summaryType = 'Average'
    print(summary.query())



import time


class Search:
    def __init__(self, Qz, query, limit=10):
        self.Total = []
        self.IDs = []
        self.Types = []
        self.Tracks = Qz.search_tracks(query, limit)['tracks']['items']
        self.Albums = Qz.search_albums(query, limit)['albums']['items']

    def seconds(self, duration):
        return time.strftime("%M:%S", time.gmtime(duration))

    def isHRes(self, item):
        if item:
            return 'HI-RES'
        else:
            return 'Lossless'

    def appendInfo(self, i, bool):
        self.IDs.append(i['id'])
        self.Types.append(bool)

    def itResults(self, iterable):
        for i in iterable:
            try:
                items = (i['artist']['name'], i['title'],
                         self.seconds(i['duration']), self.isHRes(i['hires']))
                self.Total.append('[RELEASE] {} - {} - {} [{}]'.format(*items))
                self.appendInfo(i, True)
            except KeyError:
                items = (i['performer']['name'], i['title'],
                         self.seconds(i['duration']), self.isHRes(i['hires']))
                self.Total.append('[TRACK] {} - {} - {} [{}]'.format(*items))
                self.appendInfo(i, False)

    def getResults(self, tracks=False):
        self.itResults(self.Albums)
        if tracks:
            self.itResults(self.Tracks)

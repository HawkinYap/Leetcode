
class RecentCounter:
    def __init__(self):
        self.pings = []
    def ping(self, t:int) -> int:
        self.pings.append(t)
        while self.pings[0] < t - 3000:
            self.pings.pop(0)
        print(len(self.pings))

 

recentcounter = RecentCounter()
recentcounter.ping(1)
recentcounter.ping(100)
recentcounter.ping(3001)
recentcounter.ping(3002)


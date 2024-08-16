class RecentCounter:
    def __init__(self):
        self.values=[]

    def ping(self, t: int) -> int:
        self.values.append(t)
        count=0
        while(self.values[0]<t-3000):
            self.values.pop(0)
        return len(self.values)
recentCounter=RecentCounter()
print(recentCounter.ping(1))
print(recentCounter.ping(100))
print(recentCounter.ping(3001))
print(recentCounter.ping(3002))
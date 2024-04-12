import time
class StopWatch:
    def __init__(self):
        self.__startTime=time.time()
    def getStartTime(self):
        return self.__startTime
    def getEndTime(self):
        return self.__endTime
    def start(self):
        self.__startTime = time.time()
    def stop(self):
        self.__endTime = time.time()
    def getElapsedTime(self):
        return int((self.__endTime - self.__startTime)*1000)

s = StopWatch()
result=0

for i in range(1,1000000+1):
    result+=i
s.stop()
print('1부터 1000000까지',s.getElapsedTime())
import time


class Counter:
    def __init__(self, value=0, base=0) -> None:
        self.value = value
        self.On = False
        self.baseValue = base
    def UpdateCounter(self, add=1):
        self.value = self.value + add
    def GetValue(self):
        return self.value
    def Reset(self):
        self.value = self.baseValue



class PTimer:
    def __init__(self, Timer={}) -> None:
        self.startTime = time.time()
        self.lastTime = self.startTime
        self.TimerManager = Timer
        self.TimerIsStarted = False
        self.ElapsedTime = 0
    def TimerIsStateredGet(self):
        return self.TimerIsStarted
    def TimerIsStartedSet(self, bool):
        self.TimerIsStarted = bool
    
    def StartTimer(self):
        self.TimerIsStarted = True
        self.ResetClock()

    def GetElapsedTimeSinceLastUpdate(self):
        NewTime = time.time() - self.lastTime 
        return NewTime
    def GetElapsedTimeSinceStart(self):
        NewTime = time.time() - self.startTime 
        return NewTime
    def ResetClock(self):
        self.startTime = time.time()
        self.lastTime = self.startTime
    def UpdateElapsedTime(self):
        self.lastTime = time.time()
    def ResetStartTime(self):
        self.startTime = time.time()
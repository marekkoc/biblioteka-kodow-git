import datetime as dt

class Shift:
    def get_shift_info(self):
        return f"{self.start_time:%H:%M} to {self.end_time:%H:%M}"
    
class MorningShift(Shift):
    start_time = dt.time(8, 00)
    end_time = dt.time(14, 00)

class AfternoonShift(Shift):
    start_time = dt.time(12, 00)
    end_time = dt.time(20, 00)

class NightShift(Shift):
    start_time = dt.time(14, 00)
    end_time = dt.time(22, 00)
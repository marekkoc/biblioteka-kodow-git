import datetime as dt

class Shift:
    # This is an abstract class, we will never instatiate it
    # start_time and end_time will come from subclass
    def get_shift_info(self):
        return f"{self.start_time:%H:%M} to {self.end_time:%H:%M}"
    
class MorningShift(Shift):
    # these are class variables
    start_time = dt.time(8,00)
    end_time = dt.time(14,00)

class AfternoonShift(Shift):
    start_time = dt.time(12, 00)
    end_time = dt.time(20, 00)

class NightShift(Shift):
    start_time = dt.time(14, 00)
    end_time = dt.time(22, 00)
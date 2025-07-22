class Request:
    def __init__(self):
        self._initialYear = 0
        self._initialMonth = 0
        self._initialDay = 0
        self._initialHour = 0
        self._initialMinute = 0
        self._initialSecond = 0
        self._finalYear = 0
        self._finalMonth = 0
        self._finalDay = 0
        self._finalHour = 0
        self._finalMinute = 0
        self._finalSecond = 0
        self._intialDate = ""
        self._finalDate = ""
        self._station= ""
        
        
#Getters and Setters 
    def get_initial_date(self):
        return self._intialDate
    
    def set_initial_date(self, year, month, day, hour, minute, second):
        self._initialYear = year
        self._initialMonth = month
        self._initialDay = day
        self._initialHour = hour
        self._initialMinute = minute
        self._initialSecond = second
        self._intialDate = f"{year}-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:{second:02d}"
        
    def get_final_date(self):
        return self._finalDate
    
    def set_final_date(self, year, month, day, hour, minute, second):
        self._finalYear = year
        self._finalMonth = month
        self._finalDay = day
        self._finalHour = hour
        self._finalMinute = minute
        self._finalSecond = second
        self._finalDate = f"{year}-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:{second:02d}"
    
    def get_station(self):
        return self._station
    
    def set_station(self, station):
        self._station = station
        
        
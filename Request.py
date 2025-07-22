class Request:
    def __init__(self):
        self._intialDate = ""
        self._finalDate = ""
        self._station= 0
        self._aggregation = 0 
        self._speed = True 
        self._temperature = True
        self._pressure = True
        
#Getters and Setters 
    def get_initial_date(self):
        return self._intialDate
    
    def set_initial_date(self, Date):
        self._intialDate = Date

    def get_final_date(self):
        return self._finalDate
    
    def set_final_date(self, Date):
        self._finalDate = Date

    def get_station(self):
        return self._station
    
    def set_station(self, station):
        self._station = station
    
    def get_aggregation(self):
        return self._aggregation
   
    def set_aggregation(self, aggregation):
        self._aggregation = aggregation

    def get_speed(self):
        return self._speed
    
    def set_speed(self, speed):
        self._speed = speed
    
    def get_temperature(self):
        return self._temperature
    
    def set_temperature(self, temperature):
        self._temperature = temperature
    
        
    
        
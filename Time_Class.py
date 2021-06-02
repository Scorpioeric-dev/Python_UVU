# class Time:
#   """ Blueprint for a Time object"""
#   def __init__(self):
#      self.hour = 0
#      self.minute = 0
#      self.second = 0
#
#   def set_time(self, hour, minute, second):
#      self.hour = hour
#      self.minute = minute
#      self.second = second
#
#   def print_time(self):
#      print (self.hour, ":", self.minute, ":", self.second)


# Python has features to ensure no errors come about with your class variables while it
# doesn't have a const as in JS the following is a example of setting and getting the variable to manipulate the data

class Time:
    """ Blueprint for a Time object"""

    def __init__(self):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0

    def tick(self):
        self.__second = self.__second + 1
        if self.__second == 60:
            self.__second = 0
            self.__minute = self.__minute + 1
            if self.__minute == 60:
                self.__minute = 0
                self.__hour = self.__hour + 1
                if self.__hour == 24:
                    self.__hour = 0

    def set_time(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def print_time(self):
        print(self.__hour, ":", self.__minute, ":", self.__second)

    #  Sets the second error catcher
    def set_second(self, second):
        if 0 <= second <= 59:
            self.__second = second
        else:
            self.__second = 0

    def get_second(self):
        return self.__second

    #  Sets the minute error catcher
    def set_minute(self, minute):
        if 0 <= minute <= 59:
            self.__minute = minute
        else:
            self.__minute = 0

    def get_minute(self):
        return self.__minute

    #  Sets the hour error catcher
    def set_hour(self, hour):
        if 0 <= hour <= 23:
            self.__hour = hour
        else:
            self.__hour = 0

    def get_hour(self):
        return self.__hour

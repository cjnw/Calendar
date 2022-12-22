###########################################################

    #  Event class:

    #    initializes the information of the event
    
    #    gets the time range of the event
    
    #    or displays the event in a way visible to the user
    
    #    or determines whether two events are equal

###########################################################

CAL_TYPE = ["meeting", "event", "appointment", "other"]


class P11_Event(object):

    # defines attributes and determines whether the event is valid or not
    def __init__(self, date=None, time="9:00", duration=60, cal_type="meeting"):
        if date != None:
            if "/" in date:
                date_lis = date.split("/")
                if int(date_lis[0]) >= 1 and int(date_lis[0]) <= 12:
                    if int(date_lis[1]) >= 1 and int(date_lis[1]) <= 31:
                        if int(date_lis[2]) >= 0 and int(date_lis[2]) <= 9999:
                            self.date = date
                        else:
                            self.date = None
                    else:
                        self.date = None
                else:
                    self.date = None
            else:
                self.date = None
        else:
            self.date = None
        if ":" in time:
            if int(time.split(":")[0]) >= 0 and int(time.split(":")[0]) <= 23:
                self.hour = int(time.split(":")[0])
                if int(time.split(":")[1]) >= 0 and int(time.split(":")[1]) <= 59:
                    self.minute = int(time.split(":")[1])
                    self.time = "{}:{:02d}".format(self.hour, self.minute)
                else:
                    self.time = None
            else:
                self.time = None
        else:
            self.time = None

        try:
            if duration > 0:
                self.duration = duration
            else:
                self.duration = None
        except TypeError:
            self.duration = None

        if cal_type in CAL_TYPE:
            self.cal_type = cal_type
        else:
            self.cal_type = None
        if (
            self.date == None
            or self.time == None
            or self.duration == None
            or self.cal_type == None
        ):
            self.valid = False
        else:
            self.valid = True

    # returns the date of the event
    def get_date(self):
        return self.date

    # returns the time of the event
    def get_time(self):
        return self.time

    # finds the range of time in which the event occurs
    def get_time_range(self):

        min_range = self.minute + self.duration
        if min_range > 60:  # if the event will end in the next hour
            start_mins = (self.hour * 60) + self.minute
            hrs_passed = min_range // 60  # finds how many hours had passed during event
            hr_range = (
                self.hour + hrs_passed
            )  # the hour of the day that the event ended
            min_range = min_range - 60
            end_mins = hr_range * 60
            end_mins = min_range + end_mins
        else:
            start_mins = (self.hour * 60) + self.minute
            end_mins = min_range
            end_mins = (self.hour * 60) + end_mins
        return (start_mins, end_mins)

    # returns a string of the event class object
    def __str__(self):
        if self.valid == True:
            out_str = "{}: start: {}:{:02d}; duration: {}".format(
                self.date, self.hour, self.minute, self.duration
            )
            return out_str
        else:
            return "None"

    # similar to __str__ for the class
    def __repr__(self):
        if self.date and self.time and self.duration:
            return self.date + ";" + self.time + "+" + str(self.duration)
        else:
            return "None"

    # returns true if the event's time is less than a given time
    def __lt__(self, e):
        if self.time == None or e.time == None:
            return False
        else:
            self_mins = (self.hour * 60) + self.minute
            e_mins = (e.hour * 60) + e.minute
            if self_mins < e_mins:
                return True
            else:
                return False

    # determines whether two events are equal
    def __eq__(self, e):
        return (
            self.date == e.date
            and self.time == e.time
            and self.duration == e.duration
            and self.cal_type == e.cal_type
        )  # and self.status == e.status

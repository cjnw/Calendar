###########################################################

    #  Calendar class:

    #    initialize a list
    
    #    adds event to list
    
    #    or removes event from list
    
    #    or displays the events in a given day
    
    #    or determines whether all events are equal

###########################################################

 

class P11_Calendar():
    def __init__(self):
        self.event_list = []
    
# adds an event to the calendar class object
    def add_event(self,e):
         punc = ''';,'''
         ran = e.get_time_range()
         if self.event_list == []:
             self.event_list.append(e)
             return True
         for i in self.event_list:
             b = str(self.event_list[-1])
             for char in b: # to remove unwanted punctuation
                 if char in punc:
                     b = b.replace(char,'')
             elem_list = b.split(' ')
             time_list = elem_list[2].split(':') # list of the hour and minutes
             start_time = int(time_list[0]) * 60
             end_time = start_time + int(time_list[1]) + int(elem_list[4])
             date = elem_list[0].replace(':', '')
             if date == e.date:
                 if (start_time < ran[0] and end_time < ran[0]) or (start_time > ran[1] and end_time > ran[1]):
                     self.event_list.append(e)
                     break
                 else:
                     return False
             else:
                self.event_list.append(e)
                break
            
# removes an event from the calendar class object
    def delete_event(self,date,time):
        punc = ''';,'''
        for ind,i in enumerate(self.event_list):
            b = str(i)
            for char in b:
                if char in punc:
                    b = b.replace(char,'')
            elem_list = b.split(' ') # the list of event information
            cal_time = elem_list[2]
            cal_date = elem_list[0].replace(':','')
            if cal_date == date and cal_time == cal_time == time:
                del self.event_list[ind]
                return  True
        return False
    

# forms list of events on a given day, in ascending order by time
    def day_schedule(self,date):
        day_list = []
        punc = ''';,'''
        for ind,i in enumerate(self.event_list): # to form the list
            b = str(i) # converts the event class to a string
            for char in b:
                if char in punc:
                    b = b.replace(char,'')
            elem_list = b.split(' ')
            cal_time = elem_list[2]
            cal_date = elem_list[0].replace(':','')
            if cal_date == date:
                day_list.append(i)
                
        schedule_dict = {}
        for i in day_list: # makes a dictionary of the events for each time
            b = str(i)
            for char in b:
                if char in punc:
                    b = b.replace(char,'')
            elem_list = b.split(' ')  
            cal_time = elem_list[2].split(':')
            minutes = (int(cal_time[0]) * 60) + int(cal_time[1])
            schedule_dict[minutes] = i
            
        sorted_mins = sorted(schedule_dict)
        final_list = []
        for p in sorted_mins: # appends the sorted values to a list
            final_list.append(schedule_dict[p])
        return final_list

# returns the calendar in the form of a string
    def __str__(self):
        out_str = 'Events in Calendar:\n'
        for i in self.event_list:
            out_str += '{}\n'.format(str(i))
        return out_str
 
# similar to __str__ but for the kernel
    def __repr__(self):
        s = ''
        for e in self.event_list:
            s += e.__repr__() + ";"
        return s[:-1]

# decides whether all events in the calendar are the same.
    def __eq__(self,cal):
        '''PROVIDED: returns True if all events are the same.'''
        if not isinstance(cal,P11_Calendar):
            return False
        if len(self.event_list) != len(cal.event_list):
            return False
        L_self = sorted(self.event_list)
        L_e = sorted(cal.event_list)
        for i,e in enumerate(L_self):
            if e != L_e[i]:
                return False
        return True

from datetime import datetime

class NationalPark:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, 'name'):
            self._name = name
        else:
            raise ValueError("National Park's name must be a string more than 2 characters long")
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list({trip.visitor for trip in Trip.all if trip.national_park == self})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visit_by_visitor = {}
        for trip in Trip.all:
            if trip.national_park == self:
                visit_by_visitor[trip.visitor] = visit_by_visitor.get(trip.visitor, 0) + 1
        
        max_visit = -1
        max_visitor = None
        for visitor in visit_by_visitor:
            cur_visit = visit_by_visitor[visitor]
            if cur_visit > max_visit:
                max_visit = cur_visit
                max_visitor = visitor
        
        return max_visitor
    
    @classmethod
    def most_visited(cls):
        visits_by_park = {}
        for trip in Trip.all:
            visits_by_park[trip.national_park] = visits_by_park.get(trip.national_park, 0) + 1
        
        max_visit = -1
        res_park = None
        for park in visits_by_park:
            visit = visits_by_park[park]
            if visit > max_visit:
                max_visit = visit
                res_park = park
        
        return res_park

class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)

    def check_date_format(self, date_str):
        NUMS = ('0th', '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th')

        if isinstance(date_str, str) and len(date_str) >= 7:
            try:
                date = datetime.strptime(date_str[:-2], '%B %d')
            except:
                return False
            ordinal = date_str[-3:]
            return ordinal in NUMS
        else:
            return False

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if self.check_date_format(start_date):
            self._start_date = start_date
        else:
            raise ValueError("Start date must be in 'September 1st' format")
        
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if self.check_date_format(end_date):
            self._end_date = end_date
        else:
            raise ValueError("End date must be in 'September 1st' format")
        
    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise ValueError('Visitor must be an instance of Visitor class')
    
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise ValueError('National Park must be an instance of NationalPark class')

class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Visitor's name must be a string between 1 and 15 characters inclusive")
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list({trip.national_park for trip in Trip.all if trip.visitor == self})
    
    def total_visits_at_park(self, park):
        return len([trip for trip in Trip.all if trip.visitor == self and trip.national_park == park])
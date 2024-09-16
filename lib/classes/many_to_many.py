class NationalPark:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("National Park name must be a string of at least 3 characters.")
        self._name = name
        self._trips = []

    @property
    def name(self):
        return self._name

    def trips(self):
        return self._trips

    def visitors(self):
        unique_visitors = {trip.visitor for trip in self._trips}
        return list(unique_visitors)

    def total_visits(self):
        return len(self._trips)

    def best_visitor(self):
        if not self._trips:
            return None
        visitor_visits = {}
        for trip in self._trips:
            if trip.visitor in visitor_visits:
                visitor_visits[trip.visitor] += 1
            else:
                visitor_visits[trip.visitor] = 1
        best_visitor = max(visitor_visits, key=visitor_visits.get)
        return best_visitor


class Trip:
    def __init__(self, visitor, national_park, start_date, end_date):
        if not isinstance(visitor, Visitor):
            raise ValueError("visitor must be an instance of Visitor.")
        if not isinstance(national_park, NationalPark):
            raise ValueError("national_park must be an instance of NationalPark.")
        if not (isinstance(start_date, str) and len(start_date) >= 7):
            raise ValueError("start_date must be a string of at least 7 characters.")
        if not (isinstance(end_date, str) and len(end_date) >= 7):
            raise ValueError("end_date must be a string of at least 7 characters.")
        self._visitor = visitor
        self._national_park = national_park
        self._start_date = start_date
        self._end_date = end_date

        # Register trip with the national park and visitor
        national_park._trips.append(self)
        visitor._trips.append(self)

    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date

    @property
    def visitor(self):
        return self._visitor

    @property
    def national_park(self):
        return self._national_park


class Visitor:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 1 or len(name) > 15:
            raise ValueError("Visitor name must be a string between 1 and 15 characters.")
        self._name = name
        self._trips = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or len(new_name) < 1 or len(new_name) > 15:
            raise ValueError("Visitor name must be a string between 1 and 15 characters.")
        self._name = new_name

    def trips(self):
        return self._trips

    def national_parks(self):
        unique_parks = {trip.national_park for trip in self._trips}
        return list(unique_parks)

    def total_visits_at_park(self, park):
        if not isinstance(park, NationalPark):
            raise ValueError("park must be an instance of NationalPark.")
        return sum(1 for trip in self._trips if trip.national_park == park)

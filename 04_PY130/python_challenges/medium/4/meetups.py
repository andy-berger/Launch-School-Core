from datetime import date, timedelta

class Meetup:
    DAY_OF_WEEK = {
        "sunday": 6,
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
    }

    SCHEDULE_START_DAY = {
        "first": 1,
        "second": 8,
        "third": 15,
        "fourth": 22,
        "fifth": 29,
        "teenth": 13,
        "last": None,
    }

    def __init__(self, year, month):
        self.year = year
        self.month = month

        if self.month == 12:
            self.days_in_month = (date(self.year + 1, 1, 1) - timedelta(days=1)).day
        else:
            self.days_in_month = (date(self.year, self.month + 1, 1) - timedelta(days=1)).day

    def day(self, weekday, schedule):
        weekday = weekday.lower()
        schedule = schedule.lower()

        first_possible_day = self.first_day_to_search(schedule)
        last_possible_day = min(first_possible_day + 6, self.days_in_month)

        day_of_week = self.DAY_OF_WEEK[weekday]

        for day in range(first_possible_day, last_possible_day + 1):
            current_date = date(self.year, self.month, day)

            if current_date.weekday() == day_of_week:
                return current_date
        
        return None
    
    def first_day_to_search(self, schedule):
        return self.SCHEDULE_START_DAY[schedule] or (self.days_in_month - 6)
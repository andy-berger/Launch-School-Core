class Clock:
    MINUTES_PER_DAY = 24 * 60

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    @classmethod
    def at(cls, hours, minutes=0):
        return cls(hours, minutes)
    
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    def __add__(self, delta_minutes):
        current_total = self.hours * 60 + self.minutes
        new_total = (current_total + delta_minutes) % self.MINUTES_PER_DAY
        hours, minutes = divmod(new_total, 60)
        return Clock.at(hours, minutes)
    
    def __sub__(self, delta_minutes):
        current_total = self.hours * 60 + self.minutes
        new_total = (current_total - delta_minutes) % self.MINUTES_PER_DAY
        hours, minutes = divmod(new_total, 60)
        return Clock.at(hours, minutes)
    
    def __eq__(self, other):
        if not isinstance(other, Clock):
            return NotImplemented

        return self.hours == other.hours and self.minutes == other.minutes
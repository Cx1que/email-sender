from datetime import date, timedelta

class Bill:
    def __init__(self, name, due_date, email):
        self.name = name
        self.due_date = date.fromisoformat(due_date)
        self.email = email

    def is_due_today(self, today: date) -> bool:
        return self.due_date == today
    
    def is_due_in_days(self, today: date, days: int) -> bool:
        return self.due_date - timedelta(days=days) == today
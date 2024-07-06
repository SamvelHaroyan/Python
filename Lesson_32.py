class Restaurant:
    def __init__(self, rest_name, max_tables):
        self.rest_name = rest_name
        self.max_tables = max_tables
        self.dates = {}

    def make_reservation(self, name, tables, date):
        if date not in self.dates:
            if tables <= self.max_tables:
                print(f"Reservation made for {name}, at {date}.")
                self.dates[date] = self.max_tables - tables

    def order_food(self, *args):
        return f"Order with {', '.join(args)} placed!"

class FastFoodRestaurant(Restaurant):
    def __init__(self, rest_name):
        super().__init__(rest_name, None)

    def make_reservation(self, *args):
        return "We don't take reservations."



class Locomotive:

    def __init__(self, loc_number, max_wagons):
        self.loc_number = loc_number
        self.max_wagons = max_wagons

    # Check for better way
    def __str__(self):
        print("{Loc " + self.loc_number + "}")



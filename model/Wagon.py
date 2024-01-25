from abc import ABC


class Wagon(ABC):

    def __init__(self, wagon_id):
        self.wagon_id = wagon_id
        self.previous_wagon = None
        self.next_wagon = None

    def get_last_wagon_attached(self):
        temp_next_wagon = self.next_wagon
        if temp_next_wagon is None:
            return self

        while temp_next_wagon is not None:
            temp_next_wagon = temp_next_wagon.next_wagon

        return temp_next_wagon

    def set_next_wagon(self, next_wagon):
        self.next_wagon = next_wagon

    def get_previous_wagon(self):
        return self.previous_wagon

    def set_previous_wagon(self, previous_wagon):
        self.previous_wagon = previous_wagon

    def get_number_of_wagons_attached(self):
        temp_next_wagon = self.next_wagon
        number_of_wagons = 0
        while temp_next_wagon is not None:
            number_of_wagons += 1
            temp_next_wagon = temp_next_wagon.next_wagon

        return number_of_wagons

    def has_next_wagon(self):
        return self.next_wagon is not None

    def has_previous_wagon(self):
        return self.previous_wagon is not None

    def __str__(self):
        return str(self.wagon_id)

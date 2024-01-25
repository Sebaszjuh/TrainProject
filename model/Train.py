from model.FreightWagon import FreightWagon
from model.PassengerWagon import PassengerWagon
from model.Wagon import Wagon


class Train:

    def __init__(self, engine, origin, destination):
        self.engine = engine
        self.destination = destination
        self.origin = origin
        self.first_wagon = None
        self.number_of_wagons = 0

    def is_passenger_train(self):
        if self.has_no_wagons():
            return None

        return self.first_wagon == isinstance(self.first_wagon, PassengerWagon)

    def is_freight_train(self):
        if self.has_no_wagons():
            return None
        return self.first_wagon == isinstance(self.first_wagon, FreightWagon)

    def resetNumberOfWagons(self):
        self.number_of_wagons = 0

    def has_no_wagons(self):
        return self.first_wagon is None

    def get_position_of_wagon(self, wagonId):
        wagon: Wagon = self.first_wagon
        current_wagon_id = wagon.wagon_id
        counter = 1
        while current_wagon_id != wagonId:
            counter += 1
            wagon = wagon.next_wagon
            if wagon is None:
                return -1
            current_wagon_id = wagon.wagon_id
        return counter

    def get_wagon_on_position(self, position):
        current_position = 1
        current_wagon: Wagon = self.first_wagon
        while current_position < position:
            current_position += 1
            current_wagon = current_wagon.next_wagon
            if current_wagon is None:
                raise IndexError

        return current_wagon

    def get_number_of_seats(self):
        if self.is_freight_train():
            return 0
        number_of_seats = 0
        wagon: PassengerWagon = self.first_wagon
        while wagon is not None:
            number_of_seats += wagon.number_of_seats
            wagon = wagon.next_wagon
        return number_of_seats

    def get_total_max_weight(self):
        if self.is_passenger_train():
            return 0
        total_weight = 0
        wagon: FreightWagon = self.first_wagon
        while wagon is not None:
            total_weight += wagon.max_weight
            wagon = wagon.next_wagon

        return total_weight

    def get_engine(self):
        return self.engine

    def __str__(self):
        print("TO BE DONE")

from model.Wagon import Wagon


class PassengerWagon(Wagon):
    def __init__(self, wagon_id, number_of_seats):
        super().__init__(wagon_id)
        self.number_of_seats = number_of_seats

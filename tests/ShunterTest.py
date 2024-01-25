import unittest

from model.Locomotive import Locomotive
from model.Wagon import Wagon
from model.Shunter import Shunter
from model.PassengerWagon import PassengerWagon
from model.Train import Train


class ShunterTest(unittest.TestCase):

    def setUp(self):
        self.pwList = [
            PassengerWagon(3, 100),
            PassengerWagon(24, 100),
            PassengerWagon(17, 140),
            PassengerWagon(32, 150),
            PassengerWagon(38, 140),
            PassengerWagon(11, 100),
        ]

    def make_trains(self):
        thomas = Locomotive(2453, 7)
        gordon = Locomotive(5377, 8)

        self.firstPassengerTrain = Train(thomas, "Amsterdam", "Haarleem")

        for w in self.pwList:
            Shunter.hook_wagon_on_train_rear(self.firstPassengerTrain, w)

        self.secondPassengerTrain = Train(gordon, "Joburg", "Cape Town")

    def test_check_number_of_wagons_on_train(self):
        self.make_trains()
        self.assertEqual(6, self.firstPassengerTrain.number_of_wagons)

    def test_check_number_of_seats_on_train(self):
        self.make_trains()
        self.assertEqual(730, self.firstPassengerTrain.get_number_of_seats())

    def test_check_position_of_wagons(self):
        self.make_trains()
        position = 1
        for pw in self.pwList:
            self.assertEqual(position, self.firstPassengerTrain.get_position_of_wagon(pw.wagon_id))
            position += 1

    def test_check_hook_one_wagon_on_train_front(self):
        self.make_trains()
        Shunter.hook_wagon_on_train_front(self.firstPassengerTrain, PassengerWagon(21, 140))
        self.assertEqual(7, self.firstPassengerTrain.number_of_wagons)
        self.assertEqual(1, self.firstPassengerTrain.get_position_of_wagon(21))

    def test_check_hook_row_wagons_on_train_read_false(self):
        self.make_trains()
        w1: Wagon = PassengerWagon(11, 100)
        Shunter.hook_wagon_on_wagon(w1, PassengerWagon(43, 140))
        Shunter.hook_wagon_on_train_rear(self.firstPassengerTrain, w1)
        self.assertEqual(6, self.firstPassengerTrain.number_of_wagons)
        self.assertEqual(-1, self.firstPassengerTrain.get_position_of_wagon(43))

    def test_check_move_one_wagon(self):
        self.make_trains()
        Shunter.move_one_wagon(self.firstPassengerTrain, self.secondPassengerTrain, self.pwList[3])
        self.assertEqual(5, self.firstPassengerTrain.number_of_wagons)
        self.assertEqual(-1, self.firstPassengerTrain.get_position_of_wagon(32))
        self.assertEqual(1, self.secondPassengerTrain.number_of_wagons)
        self.assertEqual(1, self.secondPassengerTrain.get_position_of_wagon(32))

    def test_check_move_row_of_wagons(self):
        self.make_trains()
        w1 = PassengerWagon(11, 100)
        Shunter.hook_wagon_on_wagon(w1, PassengerWagon(43, 140))
        Shunter.hook_wagon_on_train_rear(self.secondPassengerTrain, w1)
        Shunter.move_all_from_train(self.firstPassengerTrain, self.secondPassengerTrain, self.pwList[2])
        self.assertEqual(2, self.firstPassengerTrain.number_of_wagons)
        self.assertEqual(2, self.firstPassengerTrain.get_position_of_wagon(24))
        self.assertEqual(6, self.secondPassengerTrain.number_of_wagons)
        self.assertEqual(4, self.secondPassengerTrain.get_position_of_wagon(32))

if __name__ == '__main__':
    unittest.main()

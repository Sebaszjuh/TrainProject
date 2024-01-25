from model.FreightWagon import FreightWagon
from model.Locomotive import Locomotive
from model.PassengerWagon import PassengerWagon
from model.Train import Train
from model.Wagon import Wagon


class Shunter:

    @staticmethod
    def is_suitable_wagon(train: Train, wagon: Wagon):
        if isinstance(wagon, PassengerWagon) and train.is_passenger_train:
            return True
        elif isinstance(wagon, FreightWagon) and train.is_freight_train:
            return True
        else:
            return False

    @staticmethod
    def is_suitable_wagons(one: Wagon, two: Wagon):
        return isinstance(one, type(two))

    @staticmethod
    def has_place_for_wagon(train: Train, wagon: Wagon):
        if not Shunter.is_suitable_wagon(train, wagon):
            return False

        loc: Locomotive = train.get_engine()
        if loc.max_wagons < train.number_of_wagons + wagon.get_number_of_wagons_attached() + 1:
            return False

        return True

    @staticmethod
    def has_place_for_one_wagon(train, wagon):
        if wagon.get_number_of_wagons_attached() > 1:
            raise BaseException("Wrong method called for more than 1 wagon")
        if not Shunter.is_suitable_wagon(train, wagon):
            return False
        if train.number_of_wagons + 1 > train.get_engine().max_wagons:
            return False

        return True

    @staticmethod
    def hook_wagon_on_train_rear(train: Train, wagon: Wagon):
        number_of_new_wagons = wagon.get_number_of_wagons_attached() + 1
        if Shunter.has_place_for_wagon(train, wagon):
            if train.number_of_wagons == 0:
                train.first_wagon = wagon
            else:
                last_wagon = train.get_wagon_on_position(train.number_of_wagons)
                last_wagon.next_wagon = wagon
                wagon.previous_wagon = last_wagon
            train.number_of_wagons += number_of_new_wagons
            return True

        return False

    @staticmethod
    def hook_wagon_on_train_front(train, wagon):
        if train.has_no_wagons() and Shunter.has_place_for_wagon(train, wagon):
            train.first_wagon = wagon
            train.number_of_wagons += wagon.get_number_of_wagons_attached() + 1
        if not Shunter.is_suitable_wagons(train.first_wagon, wagon):
            return False
        if not Shunter.has_place_for_wagon(train, wagon):
            return False

        first_wagon: Wagon = train.first_wagon
        train.first_wagon = wagon
        wagon.next_wagon = first_wagon
        train.number_of_wagons += 1

        return True

    @staticmethod
    def hook_wagon_on_wagon(first: Wagon, second: Wagon):
        if not Shunter.is_suitable_wagons(first, second):
            return False
        first.next_wagon = second
        second.previous_wagon = first
        return True

    @staticmethod
    def detach_all_from_train(train, wagon):
        position_of_wagon = train.get_position_of_wagon(wagon.wagon_id)
        if position_of_wagon == -1:
            return False

        found_wagon: Wagon = train.get_wagon_on_position(position_of_wagon)
        prev_wagon: Wagon = found_wagon.previous_wagon
        prev_wagon.next_wagon = None
        number_of_removed_wagons = train.number_of_wagons - position_of_wagon
        train.number_of_wagons -= number_of_removed_wagons
        return True

    @staticmethod
    def detach_one_wagon(train, wagon):
        position_of_wagon = train.get_position_of_wagon(wagon.wagon_id)
        if position_of_wagon == -1:
            return False
        wagon: Wagon = train.get_wagon_on_position(position_of_wagon)
        prev_wagon = wagon.previous_wagon
        prev_wagon.next_wagon = wagon.next_wagon
        train.number_of_wagons -= 1
        wagon.next_wagon = None
        wagon.previous_wagon = None
        return True

    @staticmethod
    def move_all_from_train(fron: Train, to: Train, wagon: Wagon):
        if not Shunter.is_suitable_wagon(to, wagon):
            return False

        position_of_wagon = fron.get_position_of_wagon(wagon.wagon_id)

        if position_of_wagon == -1:
            return False
        wagon: Wagon = fron.get_wagon_on_position(position_of_wagon)
        prev_wagon: Wagon = wagon.previous_wagon
        prev_wagon.next_wagon = None
        wagon.previous_wagon = None
        fron.number_of_wagons -= (wagon.get_number_of_wagons_attached() + 1)

        Shunter.hook_wagon_on_train_rear(to, wagon)
        return False

    @staticmethod
    def move_one_wagon(fron: Train, to: Train, wagon: Wagon):
        Shunter.detach_one_wagon(fron, wagon)
        Shunter.hook_wagon_on_train_rear(to, wagon)

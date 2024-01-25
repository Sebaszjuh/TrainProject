from model.Wagon import Wagon


class FreightWagon(Wagon):

    def __init__(self, wagon_id, max_weight):
        super().__init__(wagon_id)
        self.max_weight = max_weight


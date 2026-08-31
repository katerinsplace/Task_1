from praktikum.bun import Bun

class TestBun:

    @classmethod
    def setup_method(cls):
        cls.name, cls.price = 'кунжутная', 1266.5
        cls.my_bun = Bun(cls.name, cls.price)

    def test_get_name_correct(self):
        assert self.my_bun.get_name() == self.name

    def test_get_price_correct(self):
        assert self.my_bun.get_price() == self.price



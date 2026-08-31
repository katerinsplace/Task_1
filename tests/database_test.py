from praktikum.database import Database

class TestDataBase:

    def setup_method(self):
        self.db = Database()

    def test_get_available_buns(self):
        available_buns = self.db.available_buns()
        assert len(available_buns) == 3

    def test_get_available_ingredients(self):
        available_ingredients = self.db.available_ingredients()
        assert len(available_ingredients) == 6




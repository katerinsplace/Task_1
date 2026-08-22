import praktikum.ingredient_types
from unittest.mock import Mock
from praktikum.burger import Burger, Bun, Ingredient
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE

class TestBurger:

    @classmethod
    def setup_method(cls):
        cls.my_burger = Burger()

    def test_set_buns(self):
        my_bun = Bun('кунжутная', 1266.5)
        self.my_burger.set_buns(my_bun)

        assert self.my_burger.bun == my_bun

    def test_add_ingredient(self):
        mock_ingredient = Mock()
        self.my_burger.add_ingredient(mock_ingredient)

        assert mock_ingredient in self.my_burger.ingredients

    def test_remove_ingredient(self):
        mock_ingredient = Mock()
        self.my_burger.add_ingredient(mock_ingredient)
        self.my_burger.remove_ingredient(0)

        assert mock_ingredient not in self.my_burger.ingredients

    def test_move_ingredient(self):
        mock_ingredient = Mock()
        mock_ingredient_2 = Mock()
        self.my_burger.add_ingredient(mock_ingredient)
        self.my_burger.add_ingredient(mock_ingredient_2)
        old_id, new_id = 0, 1
        self.my_burger.move_ingredient(old_id, new_id)
        
        assert mock_ingredient == self.my_burger.ingredients[new_id]

    def test_get_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 10
        self.my_burger.set_buns(mock_bun)

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 15.1
        self.my_burger.add_ingredient(mock_ingredient)

        expected_total = 10*2 + 15.1
        assert self.my_burger.get_price() == expected_total

    def test_get_receipt(self):

        mock_bun = Mock()
        mock_bun.get_name.return_value = "black"
        self.my_burger.set_buns(mock_bun)


        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = "chili"
        self.my_burger.add_ingredient(mock_ingredient)
  
        self.my_burger.get_price = Mock(return_value=35.1)

        expected_receipt = (
            "(==== black ====)\n"
            "= sauce chili =\n"
            "(==== black ====)\n\n"
            "Price: 35.1"
        )

        actual_receipt = self.my_burger.get_receipt()

        assert actual_receipt == expected_receipt


import data

class TestIngredient:
    def test_ingredient_get_name(self, ingredient):
        assert ingredient.get_name() == data.INGREDIENT_NAME

    def test_ingredient_get_price(self, ingredient):
        assert ingredient.get_price() == data.INGREDIENT_PRICE

    def test_ingredient_get_type(self, ingredient):
        assert ingredient.get_type() == data.INGREDIENT_TYPE

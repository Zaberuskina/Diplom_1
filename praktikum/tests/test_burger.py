import data

class TestBurger:
    def test_burger_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_burger_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == mock_ingredient

    def test_burger_remove_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_burger_move_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient and burger.ingredients[1] == mock_ingredient

    def test_burger_get_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == data.BUN_PRICE * 2 + data.INGREDIENT_PRICE

    def test_burger_get_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        assert (
            f"(==== {data.BUN_NAME} ====)" in receipt and
            f"= {data.INGREDIENT_TYPE.lower()} {data.INGREDIENT_NAME} =" in receipt and
            f"Price: {data.BUN_PRICE * 2 + data.INGREDIENT_PRICE}" in receipt
        )

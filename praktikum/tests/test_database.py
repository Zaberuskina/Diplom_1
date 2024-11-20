import pytest

class TestDatabase:
    @pytest.mark.parametrize("expected_buns", [
        [("black bun", 100), ("white bun", 200), ("red bun", 300)]
    ])
    def test_database_available_buns(self, database, expected_buns):
        buns = database.available_buns()
        assert len(buns) == len(expected_buns)
        for bun, (name, price) in zip(buns, expected_buns):
            assert bun.get_name() == name and bun.get_price() == price

    def test_database_available_ingredients(self, database):
        ingredients = database.available_ingredients()
        assert (
            len(ingredients) == 6 and
            ingredients[0].get_name() == "hot sauce" and
            ingredients[1].get_name() == "sour cream" and
            ingredients[2].get_name() == "chili sauce" and
            ingredients[3].get_name() == "cutlet" and
            ingredients[4].get_name() == "dinosaur" and
            ingredients[5].get_name() == "sausage"
        )

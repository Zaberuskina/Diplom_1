import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.database import Database
import data

@pytest.fixture
def mock_bun():
    mock = Mock(spec=Bun)
    mock.get_name.return_value = data.BUN_NAME
    mock.get_price.return_value = data.BUN_PRICE
    return mock

@pytest.fixture
def mock_ingredient():
    mock = Mock(spec=Ingredient)
    mock.get_name.return_value = data.INGREDIENT_NAME
    mock.get_price.return_value = data.INGREDIENT_PRICE
    mock.get_type.return_value = data.INGREDIENT_TYPE
    return mock

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def ingredient():
    return Ingredient(data.INGREDIENT_TYPE, data.INGREDIENT_NAME, data.INGREDIENT_PRICE)

@pytest.fixture
def database():
    return Database()

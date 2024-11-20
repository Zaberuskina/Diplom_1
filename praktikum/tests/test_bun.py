import pytest
from praktikum.bun import Bun
import data

class TestBun:
    @pytest.fixture
    def bun(self):
        return Bun(data.BUN_NAME, data.BUN_PRICE)

    def test_bun_get_name(self, bun):
        assert bun.get_name() == data.BUN_NAME

    def test_bun_get_price(self, bun):
        assert bun.get_price() == data.BUN_PRICE

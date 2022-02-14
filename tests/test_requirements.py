"""Test requirements module template"""
from project_name import BaseClass, base_function
from . import BaseClassRequirements
from pytest import fixture


class TestBaseClass(BaseClassRequirements):
    @fixture(scope="class", autouse=True)
    def base(self):
        return BaseClass()


def test_base_function():
    assert base_function() == "hello from base function"

"""Initialization tests for common project requirements"""
from inspect import ismethod


class BaseClassRequirements:
    def test_has_base_method(self, base):
        assert hasattr(base, "base_method")
        assert ismethod(base.base_method)

    def test_base_call(self, base):
        assert base() == "hello from BaseClass"

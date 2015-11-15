#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating custom exception classes"""


class BaseError(Exception):
    """BaseError Class"""
    pass


class StringError(BaseError, TypeError):
    """StringError Class"""
    pass


class NumberError(BaseError, TypeError):
    """NumberError Class"""
    pass


class NonZeroError(NumberError):
    """NonZeroError Class"""
    pass

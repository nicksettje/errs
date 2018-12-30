#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `errs` package."""

import pytest


from errs.errs import errs


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_no_error(response):
    @errs
    def no_raises():
        return 0
    out, err = no_raises()
    assert(err.check() == False)

def test_error(response):
    @errs
    def raises():
        raise Exception()
        return 0
    out, err = raises()
    assert(err.check() == True)

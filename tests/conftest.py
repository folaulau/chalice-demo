#######
# Copyright (C) 2019 Anvilogic Inc.
# Anvilogic CONFIDENTIAL - Use or disclosure of this material in whole or in part
# without a valid written license from Anvilogic Inc. is PROHIBITED
#######

# Python Imports
import pytest
import os
import app as chalice_app
from chalice import Chalice
from chalice.test import Client

@pytest.fixture
def app() -> Chalice:
    return chalice_app


@pytest.fixture
def test_client():
    with Client(chalice_app.app,stage_name='test') as client:
        yield client
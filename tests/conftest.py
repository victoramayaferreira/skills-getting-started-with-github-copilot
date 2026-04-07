import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

_INITIAL_ACTIVITIES_STATE = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    activities.clear()
    activities.update(copy.deepcopy(_INITIAL_ACTIVITIES_STATE))


@pytest.fixture
def client():
    return TestClient(app)

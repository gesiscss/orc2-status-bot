"""
Test Binder installation capability to launch repository
"""

import json
import datetime

import logging

import pytest  # pylint: disable=unused-import
import requests

REQUESTS_TIMEOUT = 30  # seconds
USER_TIMEOUT = 300  # seconds or 5min

LOGGER = logging.getLogger(__name__)


def test_launch_binder(binder_url):
    """
    We can launch an image that most likely already has been built.
    """
    repo = "binder-examples/requirements"
    ref = "50533eb470ee6c24e872043d30b2fee463d6943f"
    build_url = f"{binder_url}/build/gh/{repo}/{ref}"

    log = []

    begin_of_request = datetime.datetime.now()

    response = requests.get(build_url, stream=True, timeout=REQUESTS_TIMEOUT)
    response.raise_for_status()
    for line in response.iter_lines():
        now = datetime.datetime.now()
        request_duration = now - begin_of_request
        if request_duration.seconds > USER_TIMEOUT:
            response.close()
            break

        line = line.decode("utf8")
        if line.startswith("data:"):
            data = json.loads(line.split(":", 1)[1])

            log.append(data.get("message"))
            
            if data.get("phase") == "ready":
                notebook_url = data["url"]
                token = data["token"]
                break
    else:
        # This means we never got a 'Ready'!
        print(''.join(log))
        assert False

    headers = {"Authorization": f"token {token}"}
    response = requests.get(
        notebook_url + "/api", headers=headers, timeout=REQUESTS_TIMEOUT
    )
    assert response.status_code == 200
    assert "version" in response.json()

    response = requests.post(
        notebook_url + "/api/shutdown", headers=headers, timeout=REQUESTS_TIMEOUT
    )
    assert response.status_code == 200

import pytest

from engine.vlsm_engine import VLSMEngine


def test_vlsm_allocation():

    requests = {
        "CSE": 100,
        "IT": 50,
        "Admin": 25
    }

    result = VLSMEngine.allocate_vlsm(
        "192.168.0.0/24",
        requests
    )

    assert len(result) == 3


def test_address_space_exhaustion():

    requests = {
        "CSE": 500
    }

    with pytest.raises(ValueError):
        VLSMEngine.allocate_vlsm(
            "192.168.0.0/24",
            requests
        )


def test_invalid_host_count():

    with pytest.raises(ValueError):
        VLSMEngine.calculate_prefix(0)


def test_no_subnet_overlap():

    requests = {
        "CSE": 100,
        "IT": 50,
        "Admin": 25,
        "Library": 10
    }

    result = VLSMEngine.allocate_vlsm(
        "192.168.0.0/24",
        requests
    )

    networks = [
        subnet["network"] for subnet in result
    ]

    assert len(networks) == len(set(networks))
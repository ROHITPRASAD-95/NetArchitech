import pytest

from engine.routing_engine import RoutingEngine
from engine.explainability import ExplainabilityEngine

def test_single_site_ospf():

    result = RoutingEngine.recommend_routing(
        site_count=1,
        subnet_count=10
    )

    assert result["protocol"] == "OSPF Area 0"


def test_multiple_sites_routing():

    result = RoutingEngine.recommend_routing(
        site_count=3,
        subnet_count=20
    )

    assert result["protocol"] == "Multi-Area OSPF or eBGP"


def test_cloud_routing():

    result = RoutingEngine.recommend_routing(
        site_count=1,
        subnet_count=10,
        cloud_required=True
    )

    assert result["protocol"] == "Multi-Area OSPF or eBGP"


def test_invalid_site_count():

    with pytest.raises(ValueError):
        RoutingEngine.recommend_routing(
            site_count=0,
            subnet_count=10
        )

def test_explanation_generation():

    media = {
        "media": "Cat6a",
        "reason": "Suitable for distances up to 100 meters."
    }

    routing = {
        "protocol": "OSPF Area 0",
        "reason": "Single autonomous system."
    }

    result = ExplainabilityEngine.generate_explanation(
        media,
        routing
    )

    assert "Cat6a" in result
    assert "OSPF Area 0" in result
    assert "MEDIA SELECTION" in result
    assert "ROUTING SELECTION" in result
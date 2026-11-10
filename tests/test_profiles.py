from engine.profile_loader import ProfileLoader


def test_campus_profile():

    profile = ProfileLoader.load_profile("campus")

    assert profile["profile"] == "Campus LAN"
    assert profile["endpoints"] == 1600


def test_metro_profile():

    profile = ProfileLoader.load_profile("metro")

    assert profile["profile"] == "Metro MAN"
    assert profile["endpoints"] == 450


def test_wan_profile():

    profile = ProfileLoader.load_profile("wan")

    assert profile["profile"] == "Global WAN"
    assert profile["endpoints"] == 2000
    
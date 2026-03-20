from event.event import Event

def test_sign_up_adds_member():

    event = Event(None)

    event.sign_up("Anna")

    assert "Anna" in event.members

def test_sign_up_multiple_members():

    event = Event(None)

    event.sign_up("Anna")
    event.sign_up("Lena")

    assert len(event.members) == 2
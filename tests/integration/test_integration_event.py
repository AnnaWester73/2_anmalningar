from event.event import Event
from event.member_service import MemberService

def test_register_new_member_adds_to_both():

    service = MemberService()
    event = Event(service)

    event.register_new_member("Anna")

    assert "Anna" in service.members
    assert "Anna" in event.members

def test_register_new_member_calls_all_methods(mocker):

    service = MemberService()
    event = Event(service)

    spy_add = mocker.spy(service, "add_member")
    spy_signup = mocker.spy(event, "sign_up")

    event.register_new_member("Anna")

    spy_add.assert_called_once_with("Anna")
    spy_signup.assert_called_once_with("Anna")



from event.member_service import MemberService


def test_add_member():

    service = MemberService()
    service.add_member("Anna")

    assert "Anna" in service.members

#spytest
def test_add_member_called(mocker):

    service = MemberService()

    spy = mocker.spy(service, "add_member")

    service.add_member("Anna")

    spy.assert_called_once_with("Anna")
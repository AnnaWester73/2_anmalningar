
from event.member_service import MemberService

def test_add_member():

    service = MemberService()
    service.add_member("Anna")

    assert "Anna" in service.members
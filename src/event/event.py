
class Event:

    def __init__(self, member_service):
        self.member_service = member_service
        self.members = []

    def sign_up(self, member):
        self.members.append(member)

    def register_new_member(self, member):
        self.member_service.add_member(member)
        self.sign_up(member)
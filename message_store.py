class MessageStore:
    def __init__(self):
        self.messages = {}

    def save_message(self, to_user, message):
        if to_user not in self.messages:
            self.messages[to_user] = []
        self.messages[to_user].append(message)

    def get_messages(self, user):
        return self.messages.pop(user, [])

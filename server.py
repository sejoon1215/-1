from message_store import MessageStore

class KakaoServer:
    def __init__(self):
        self.store = MessageStore()

    def receive_message(self, from_user, to_user, message):
        print(f"[서버] {from_user} -> {to_user}: 메시지 수신")
        self.store.save_message(to_user, f"{from_user}: {message}")
        self.send_push_notification(to_user)

    def send_push_notification(self, user):
        print(f"[서버] {user} 에게 푸시 알림 전송")

    def fetch_messages(self, user):
        return self.store.get_messages(user)

from server import KakaoServer

class KakaoApp:
    def __init__(self, username, server):
        self.username = username
        self.server = server

    def send_message(self, to_user, message):
        print(f"[앱:{self.username}] 메시지 전송 요청 → 서버")
        self.server.receive_message(self.username, to_user, message)

    def receive_messages(self):
        print(f"[앱:{self.username}] 서버로부터 메시지 요청")
        messages = self.server.fetch_messages(self.username)
        for msg in messages:
            print(f"[앱:{self.username}] 수신된 메시지: {msg}")

from app import KakaoApp
from server import KakaoServer

# 1. 서버 시작
server = KakaoServer()

# 2. 사용자 A가 메시지 전송
user1 = KakaoApp("user1", server)
user1.send_message("user2", "안녕, 저녁 뭐 먹을 거야?")

print("\n--- 사용자 B 메시지 수신 ---\n")

# 3. 사용자 B가 메시지 확인
user2 = KakaoApp("user2", server)
user2.receive_messages()

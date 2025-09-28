from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# ① 생성한 OpenAI API Key 입력
api_key = os.getenv("OPENAI_API_KEY")

# ② OpenAI 클라이언트 생성
client = OpenAI(api_key=api_key)

# ③ 모델에 요청 전달
response = client.chat.completions.create(
  model="gpt-4o-mini", # ④ 사용할 모델 선택
  temperature=0.1,  # ⑤ 출력의 다양성을 조절하는 매개변수 (0에 가까울수록 안정적이고 일관된 답변 생성)
  messages=[
    {"role": "system", "content": "You are a helpful assistant."}, # ⑥ 시스템 메시지 (모델에 전달할 명령어 또는 정보)
    {"role": "user", "content": "2022년 월드컵 우승팀은 어디야?"}, # ⑦ 사용자 메시지 (모델에 전달할 질문 또는 요청)
  ]		# system, user, assistant 3가지 역할이 있으며 assistant는 모델이 제공하는 답변을 의미
)

print(response)

print('----')	# ⑤
print(response.choices[0].message.content) 
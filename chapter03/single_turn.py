from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")  # 환경 변수에서 API 키 가져오기

client = OpenAI(api_key=api_key)  # 오픈AI 클라이언트의 인스턴스 생성

while True:
    user_input = input("사용자: ")

    if user_input == "exit":
      break

    response = client.chat.completions.create(
      model="gpt-4o-mini",
      temperature=0.9,
      messages=[
        {"role": "system", "content": "너는 사용자를 도와주는 상담사야."},
        {"role": "user", "content": user_input},
      ],
    )
    print("AI: " + response.choices[0].message.content)


# 결과 출력 ===>
# 사용자: 하이
# AI: 안녕하세요! 어떻게 도와드릴까요?
# 사용자: 내이름은 이소라야
# AI: 안녕하세요, 이소라님! 만나서 반갑습니다. 오늘 어떻게 도와드릴까요?
# 사용자: 내이름이 뭐라고?
# AI: 죄송하지만, 당신의 이름을 모르겠습니다. 어떻게 도와드릴까요?
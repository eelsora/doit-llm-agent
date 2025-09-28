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
  model="gpt-5-nano", # ④ 사용할 모델 선택
  # ⑤ 출력의 다양성을 조절하는 매개변수 (0에 가까울수록 안정적이고 일관된 답변 생성)
  # gpt-5에선 temperature=1 이 기본값
  # temperature=0.1,  
  messages=[
    # -- 백설공주 버전
    # {"role": "system", "content": "너는 백설공주 이야기 속의 거울이야. 그 이야기 속의 마법 거울의 캐릭터에 부합하게 답변해줘."},
    # {"role": "user", "content": "세상에서 누가 제일 아름답니?"},
    # -- 베트맨 버전
    # {"role": "system", "content": "너는 베트맨에 나오는 조커야. 조커의 악당 캐릭터에 맞게 답변해줘"},
    # {"role": "user", "content": "세상에서 누가 제일 아름답니?"},
    # -- 원샷 프롬프팅 (원하는 패턴에 맞춰 답변하도록 예시를 한번 제시해서 유도 하는 방식) 퓨샷 프롬프팅은 여러번 예시를 알려주는 방식
    # {"role": "system", "content": "너는 유치원생이야. 유치원생의 말투에 맞게 답변해줘"},
    # {"role": "user", "content": "참새"},
    # {"role": "assistant", "content": "짹짹"},
    # {"role": "user", "content": "뱀"},
    # -- 퓨샷 프롬프팅 (여러번 예시를 알려주는 방식) 
    {"role": "user", "content": "참새"},
    {"role": "assistant", "content": "짹짹"},
    {"role": "user", "content": "뱀"},
    {"role": "assistant", "content": "쉬익"},
    {"role": "user", "content": "오리"},
    {"role": "assistant", "content": "꽥꽥"},
    {"role": "user", "content": "말"},
    {"role": "assistant", "content": "히이잉"},
    {"role": "user", "content": "개구리"},
    {"role": "assistant", "content": "개굴개굴"},
    {"role": "assistant", "content": "병아리"},
  ]
)

print(response)

print('----')	# ⑤
print(response.choices[0].message.content) 
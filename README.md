# DO IT! LLM을 활용한 AI 에이전트 개발 입문 실습 프로젝트

**DO IT! LLM을 활용한 AI 에이전트 개발 입문 실습 프로젝트** 책의 예제 코드를 실습해보는 저장소입니다.

## 🛠️ 기술 스택

- **Python 3.x**
- **OpenAI API** - GPT 모델 활용
- **Streamlit** - 웹 인터페이스
- **python-dotenv** - 환경 변수 관리

## 🚀 시작하기

### 1. 환경 설정

```bash
# 가상환경 활성화
source venv/bin/activate  # macOS/Linux

# 필요한 패키지 설치
pip install openai streamlit python-dotenv
```

### 2. API 키 설정

`.env` 파일을 생성하고 OpenAI API 키를 설정:

```bash
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

### 3. 예제 실행

**기본 python 파일 실행:**

```bash
python chapter02/gpt_basic.py
```

**Streamlit 웹 인터페이스:**

```bash
streamlit run chapter03/streamlit_basic.py
```

## 📖 학습 내용

- OpenAI API 기본 사용법
- 대화형 AI 구현 (단일/다중 턴)
- 프롬프트 엔지니어링 (원샷/퓨샷 프롬프팅)
- Streamlit을 활용한 웹 인터페이스

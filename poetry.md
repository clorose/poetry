다음은 **Poetry**를 사용하여 Python 프로젝트 환경을 설정하고, 필요한 라이브러리 설치 및 가상 환경 활성화 방법을 마크다운 형식으로 정리한 내용입니다.

---

## Poetry 설치 및 설정 방법

### 1. Poetry 설치

Poetry를 설치하려면, 아래 명령어를 실행합니다:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

설치가 완료되면, Poetry가 제대로 설치되었는지 확인하려면 아래 명령어를 실행합니다:

```bash
poetry --version
```

### 2. Poetry 프로젝트 초기화

새로운 프로젝트를 생성하려면 다음 명령어를 사용합니다:

```bash
poetry new 프로젝트이름
```

기존 프로젝트에 `pyproject.toml`을 생성하고 의존성을 관리하려면 아래 명령어를 사용합니다:

```bash
poetry init
```

### 3. Poetry로 의존성 추가

필요한 라이브러리를 추가하려면, 예를 들어 `requests` 라이브러리를 추가하고 싶다면 아래 명령어를 사용합니다:

```bash
poetry add requests
```

### 4. Poetry 가상 환경 활성화

Poetry가 관리하는 가상 환경을 활성화하려면 아래 명령어를 실행합니다:

```bash
poetry shell
```

### 5. Python 파일 실행

Poetry 가상 환경 내에서 Python 파일을 실행하려면 아래 명령어를 사용합니다:

```bash
poetry run python 파일명.py
```

### 6. 가상 환경 종료

Poetry 가상 환경을 종료하려면 아래 명령어를 사용합니다:

```bash
exit
```

가상 환경에서 나가면, 시스템 Python 환경으로 돌아가게 됩니다.

---

## Poetry와 `pyenv`를 사용할 때의 주의 사항

### 1. `pyenv`와 Poetry의 충돌 문제

- Poetry는 **자체적인 가상 환경**을 관리하므로, `pyenv`로 관리되는 Python 버전과 별개로 동작합니다.
- `pyenv`를 통해 프로젝트에 특정 버전을 설정하면, Poetry는 그 버전을 **자체적으로 관리**할 수 있습니다.

### 2. Poetry 가상 환경에서만 라이브러리 사용 가능

Poetry의 가상 환경에서 설치한 라이브러리는 **해당 가상 환경 내에서만** 사용할 수 있습니다. 예를 들어:

```bash
poetry add requests
```

이렇게 설치한 `requests`는 **Poetry 가상 환경** 내에서만 사용 가능하며, **Poetry 환경을 벗어나면** 라이브러리가 작동하지 않습니다.

### 3. `pyenv`를 끄고 Poetry만 사용

`pyenv`를 프로젝트에서 끄고 싶다면, 프로젝트 디렉토리 내에서 `pyenv local --unset` 명령어를 사용하여 `pyenv` 설정을 해제할 수 있습니다:

```bash
pyenv local --unset
```

이렇게 하면, `pyenv`는 해당 프로젝트에서 **더 이상 사용되지 않으며**, Poetry가 관리하는 가상 환경 내에서 Python 버전을 사용할 수 있게 됩니다.

### 4. 시스템 Python에서 Poetry 가상 환경 라이브러리 사용 불가

Poetry의 가상 환경에서 설치한 라이브러리는 **시스템 Python 환경에서 사용되지 않습니다**. 시스템 Python에서 라이브러리를 사용하려면, 시스템 환경에 직접 설치해야 합니다:

```bash
pip3 install requests
```

또는 Poetry 환경으로 돌아가서 실행하려면, `poetry shell` 명령어로 가상 환경을 활성화해야 합니다.

---

## 예시 코드

```python
# hello.py 파일

import requests

response = requests.get('https://www.example.com')
print(response.status_code)
```

이 코드는 **Poetry 가상 환경**에서만 실행됩니다. 시스템 Python 환경에서는 `requests` 라이브러리가 설치되지 않아 `ModuleNotFoundError`가 발생할 수 있습니다.

### 실행 방법:
1. Poetry 가상 환경을 활성화:

   ```bash
   poetry shell
   ```

2. Python 파일 실행:

   ```bash
   python hello.py
   ```

---

### 정리

- **Poetry**는 **자체 가상 환경을 관리**하고, 프로젝트별로 Python 버전과 의존성을 관리할 수 있게 돕습니다.
- Poetry 가상 환경을 벗어나면, **시스템 Python 환경에서 라이브러리**를 사용할 수 없습니다. 이럴 경우, **Poetry 가상 환경을 활성화**하거나 **시스템에 라이브러리를 재설치**해야 합니다.
- **`pyenv`와 함께 사용할 때**, `pyenv`로 Python 버전을 관리하고, Poetry가 그 버전의 가상 환경을 관리하도록 설정할 수 있습니다. `pyenv`를 끄고 Poetry만 사용할 수도 있습니다.

---

이 문서가 도움이 되셨길 바랍니다! 추가적인 질문이 있으시면 언제든지 알려주세요!
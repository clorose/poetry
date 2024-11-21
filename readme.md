# Poetry 사용법

- [설치법](./설치법.md) 은 페이지 참조 부탁드립니다.
- [사용법](./사용법.md) 은 페이지 참조 부탁드립니다.

## 주요 도구 소개

- python
- Poetry 
- Pyenv

## poetry 프로젝트 생성

**시작 전 선택사항**

```bash
poetry config virtualenvs.in-project true
```
로 프로젝트 폴더에 가상 환경을 생성하도록 설정합니다.
이 설정을 하지 않으면 프로젝트 폴더 외부에 가상 환경이 생성됩니다.
그러면 프로젝트 폴더를 삭제해도 가상 환경이 남아있습니다.

프로젝트 폴더에서 생성합니다.
```bash
poetry new <project-name>
```

만약 기존 프로젝트 폴더에서 생성하고 싶다면 아래와 같이 합니다.

```bash
poetry init
```


그러면 대화형으로 프로젝트 생성 가능합니다.
기본적으로는 전부 엔터로 넘어가면 됩니다.
추후에 pyproject.toml 파일을 수정해서 추가할 수 있습니다.

```toml
[tool.poetry]
name = "poetry"
version = "0.1.0"
description = "description your project"
authors = ["johndoe <johndoe@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "3.11.10" # 사용할 python 버전


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

## poetry 로 가상 환경 설정하기

### 1. Python 버전 설정

먼저 사용할 Python 버전을 설정합니다. 이 이유는 poetry 가 가상 환경을 만들 때, 이 버전을 사용하기 때문입니다.
만약 사용하지 않는다면 현재의 global 버전을 사용합니다.

```bash
pyenv global <version>
```

저는 3.11.10 버전을 사용했습니다.

```bash
pyenv global 3.11.10
```

### 2. Poetry 프로젝트 가상화

프로젝트 폴더에서 가상 환경을 만들어줍니다. 

```bash
poetry env use <version>
```

저는 3.11.10 버전을 사용했습니다.

```bash
poetry env use 3.11.10
```

### 3. pyproject.toml 파일 수정

pyproject.toml 파일에 사용할 python 버전을 설정합니다.

```toml
python = "3.11.10" # 방금 설정한 python 버전
```

### 4. Pyenv 버전 끊기

여기서 가상 환경을 끊는 이유는 zsh에서 poetry 가상 환경이 뜨지 않고, pyenv 의 버전만 뜨는 문제가 있어서
제가 원한건 poetry 의 가상 환경이 잘 실행중인지 zsh 에서 확인하고 싶어서 끊었습니다.

```bash
pyenv local --unset
```

### 5. 실행

```bash
poetry install
poetry shell
```


```bash
echo $POETRY_ACTIVE
```
를 통해 가상 환경이 잘 실행중인지 확인할 수 있습니다.

또는 

```bash
which python
```
를 통해 가상 환경의 python 경로를 확인할 수 있습니다.
실제 출력은 아래와 같습니다. (참고로 **poetry config virtualenvs.in-project true** 설정을 했기 때문에 프로젝트 폴더 내에 가상 환경이 생성됩니다.)

```bash
/Users/username/path/your/workspace/.venv/bin/python
```

## 참고

- 이 가이드라인은 Poetry와 Pyenv를 함께 사용할 때 발생하는 문제를 해결하기 위해 작성되었습니다.
- 주요 이슈: oh-my-zsh 환경에서 Poetry 가상환경 대신 Pyenv 버전이 표시되는 문제를 해결하는 방법을 다룹니다.
- 테스트 환경:
  - macOS: 테스트 완료
  - WSL: 테스트 진행 중
- 현재 제안된 해결방법(`pyenv local --unset`)의 장단점:
  - 장점: Poetry 가상환경이 정상적으로 표시됨
  - 주의사항: Pyenv 설정을 해제하는 것의 잠재적 영향은 추가 검증이 필요함
- 문제가 발생하거나 더 나은 해결방법이 있다면 이슈를 통해 공유해주세요.

### 이미지
- pyenv(before)
![pyenv](./image/pyenv.png)
- poetry(after)
![poetry](./image/poetry.png)


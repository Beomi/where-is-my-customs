# 내 통관은 어디쯤?

> 카카오톡 봇: [https://pf.kakao.com/_xdxnfMj](https://pf.kakao.com/_xdxnfMj)

우리가 직구를 하다보면 갑갑해지는 구간이 있습니다. (사실 한두곳이 아니기는 합니다)

Ultra Slow Postal Service를 지나, DE에서 NJ로 가는 여정을 지나, 
오프로드의 벽을 넘어서 한국에 들어와도 그 순간부터 배송 추적만으로는 진행상황을 알기 어려운 시점이 옵니다.

바로 세관 진행상황입니다. 

배송 추적 서비스에서는 세관에서 어떻게 진행되는지 잘 알려주지 않기 떄문이죠.
물론 일상적인 경우에는 하루만 기다리면 세관 통과가 진행되지만, 
하루라도 빨리 받아보고 싶은 직구러의 마음은 조금이나마 빨리 알고싶은 마음이니까요.

그래서 만들었습니다. `customs.go.kr` 에서 하루종일 새로고침하는 직구러들을 위한 봇!

아래와 같이 HLB(송장번호)등을 통한 조회가 가능합니다.

<img src='https://user-images.githubusercontent.com/11323660/46076623-0ddd6300-c1c9-11e8-8dbd-d87ea2c7fee6.jpg' style="max-wigth:350px" />

또한 7일 내 조회한 송장번호를 재입력없이 사용할 수 있습니다.

<img src='https://user-images.githubusercontent.com/11323660/46076624-0ddd6300-c1c9-11e8-82e0-e24fe3fcc2f1.jpg' style="max-wigth:350px" />

## 개발 가이드

이 프로젝트는 Python3.6을 사용합니다. 또한, `pip` 패키지 관리를 위해 `Pipenv`를 사용하고 있습니다.

> `pipenv`는 `pip install pipenv`로 설치할 수 있습니다.

### 패키지 설치 

전체 의존성 패키지들은 아래 명령어로 설치할 수 있습니다.

```bash
pipenv install 
```

> 혹시 `psycopg2-binary`로 인해 설치 오류가 난다면 로컬 개발시에는 이부분을 설치하지 않고 개발해도 됩니다. 해당 패키지는 Heroku 배포를 위해 들어가있습니다. 로컬 개발에서는 Sqlite3을 사용합니다.

### Django Setup

로컬에서 개발시에는 Sqlite3 DB를 생성해 사용합니다. 아래 명령어로 DB를 생성해주세요.

```bash
pipenv run python manage.py migrate
```

로컬 개발용 웹 서버는 아래와 같이 띄울 수 있습니다. 기본적으로 `http://localhost:8000`에 뜹니다.

```bash
pipenv run python manage.py runserver
```

## TODO

- [x] HBL(송장번호)로 통관 조회
- [ ] MBL로 통관 조회
- [ ] 화물관리번호로 통관 조회
- [ ] 오입력한 통관 번호 삭제 기능
- [ ] 숫자 아닌 경우 통관 조회
- [ ] 채팅방 나가는 경우 기록 삭제
- [ ] 텔레그램버전 추가
    - [ ] 주기적 체크
    - [ ] 변동시 알림

## Heroku에 한번에 배포하기

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

현재 Repo를 **Fork**한 뒤, 위 버튼을 누르면 `master`브랜치가 여러분의 Heroku 계정에 자동으로 배포됩니다.

# Tredecadia

[English](README.md) · **한국어** · [모든 언어](README.languages.md)

Tredecadia는 **28일짜리 13개월**로 이루어진 개방형 영구 달력 프로젝트입니다. 모든 달이 정확히 4주이므로 같은 날짜는 해마다 같은 요일에 놓입니다. 한 해의 길이를 맞추는 추가 날짜는 달과 7일 주기에서 따로 분리합니다.

> **현재 공개 버전은 `1.0.0-rc.1`입니다.** v1의 호환성 범위는 이미 고정되어 있지만, 최종 `v1.0.0`을 내기 전 실제 사용과 피드백을 확인하는 관찰 기간을 거칩니다.

## 기본 구조

- 13 × 28 = 달 안에 들어가는 일반 날짜 364일.
- 모든 달은 정확히 4주입니다.
- 매달 `01`은 항상 월요일, `28`은 항상 일요일입니다.
- `EQ` — 춘분 / 새해의 날 — 이 한 해를 시작하며 어느 달에도, 어느 요일에도 속하지 않습니다.
- 윤년에는 `13-28` 다음에 `ED` — 지구의 날 — 이 하나 더 들어가고, 그 뒤에 다음 해의 `EQ`가 옵니다.

평년:

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

윤년:

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Tredecadia Era

Tredecadia는 실제 **0년**을 포함하는 하나의 정수형 연도 축을 사용합니다. 달력 내부에서는 BCE/CE처럼 연대를 둘로 나눌 필요가 없습니다.

수학적 원점은 다음과 같습니다.

`TE 00000-EQ ↔ 그레고리력 천문학적 연도 -9999년 3월 20일`

통상적인 표현으로는 대략 **10000 BCE**에 해당합니다. 이 날짜를 인류나 문명의 시작으로 주장하는 것은 아닙니다. Tredecadia 연도 좌표를 정하기 위한 수학적 0점일 뿐입니다.

민간 변환 규칙은 간단합니다.

`TE 연도 = 그레고리력 천문학적 연도 + 9999`

따라서 2026년은 **TE 12025**입니다.

## 날짜 표기

기계 교환용 정규 형식은 엄격한 ASCII를 사용하며 연도는 최소 5자리입니다.

`12025-07-11` · `00000-EQ` · `-00001-01-01`

사용자 화면에서는 앞의 0을 생략하거나 조판용 마이너스 기호를 써도 됩니다. 이는 표시 방식일 뿐 다른 정규 식별자는 아닙니다.

## 월 이름

| # | 이름 | Short-6 | Short-4 |
|---:|---|---|---|
| 01 | Masanumika | Masanu | Masa |
| 02 | Tasuzunumu | Tasuzu | Tasu |
| 03 | Nazumasanu | Nazuma | Nazu |
| 04 | Mikasumani | Mikasu | Mika |
| 05 | Yanimuzunu | Yanimu | Yani |
| 06 | Zumitanasu | Zumita | Zumi |
| 07 | Muyasanumi | Muyasa | Muya |
| 08 | Sunizusaka | Sunizu | Suni |
| 09 | Numanamuta | Numana | Numa |
| 10 | Kazunusuya | Kazunu | Kazu |
| 11 | Yanazumasa | Yanazu | Yana |
| 12 | Sanumikazu | Sanumi | Sanu |
| 13 | Nimutazuna | Nimuta | Nimu |

대화에서는 월을 말하고 있다는 점이 분명할 때 4글자 Short-4를 우선 사용합니다. 기준 발음은 **첫 음절을 약하게 두드러지게** 하는 정도이며, 강세 자체는 이름의 식별 요소가 아닙니다.

## 사양과 코드

Python 기준 변환기는 [`reference/python/tredecadia.py`](reference/python/tredecadia.py)에 있습니다. 규범 문서는 [`specification/`](specification/), 기계 판독 레지스트리는 [`registry/`](registry/)에 있습니다.

이 한국어 README는 한국어 독자가 자연스럽게 읽을 수 있도록 별도로 작성한 소개문이며, 영어 문장을 그대로 옮긴 번역본이 아닙니다. 규범 판단은 정식 사양을 따릅니다.

## 라이선스

문서·사양·데이터는 **CC BY 4.0**, 코드와 스크립트는 별도 표기가 없으면 **MIT**입니다. 자세한 내용은 [`LICENSE.md`](LICENSE.md)를 참고하세요.

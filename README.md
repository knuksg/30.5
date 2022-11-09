# 30.5 🍔

> `30.5`는 망고플레이트를 기반으로 한 **맛집 정보 및 후기 공유 커뮤니티 서비스** 입니다.

<br/>

<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=ffffff"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=ffffff"/>　<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=ffffff"/>　<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=ffffff"/>　<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=ffffff"/>

<br/>

## **📅 일정**

- **2022.11.01 ~ 2022.11.07**

---

## **🧑‍💻 개발팀**

<a href="https://github.com/1c0332zz/Django_PJT_30.5/graphs/contributors">

| <img src="https://contrib.rocks/image?repo=1c0332zz/Django_PJT_30.5" />                         |     |
| ----------------------------------------------------------------------------------------------- | --- |
| 총괄 팀장: 송강섭<br />백엔드 및 발표: 주세환<br />백엔드 총괄 : 김선교<br />UI/UX 담당: 조병진 |     |

</a>

<br/>

---

## **🎮 주요 기능**

- **회원관리**
  - 회원가입
  - 로그인
  - 회원 프로필
    - 회원 프로필 관리 / 수정
    - **회원간 팔로우 / 팔로잉**
  - 로그아웃
  - 회원탈퇴

---

- **메인 페이지**
  - 헤더 - **검색 창: 태그 및 지역, 이름으로 검색**
  - 메인 - 믿고 보는 맛집 리스트 : 그리드 반응형
  - 메인 - 스토리 : 그리드 반응형
  - 메인 - 평점 높은 인기 식당 : 그리드 반응형
- **네브바**
  - 토글 버튼
  - 검색 기능
- **푸터**
  - 프로젝트 정보 및 팀 정보

---

- **맛집 리스트**
  - 메뉴별 리스트
    - 태그별 분류
  - 식당별 리스트
    - 식당 사진 / 이름 / 주소 / 평점 / 별점 주기 / 댓글 작성자 프로필 및 댓글 내용
- **식당 정보**
  - 사진
  - **조회 수, 리뷰 수, 별점 수**
  - **별점 주기 / 리뷰 쓰기**
  - 식당 정보
  - 리뷰 목록

---

- **리뷰 목록**
  - 리뷰 작성 시간 / 리뷰 내용 / 리뷰 평점 / 작성자 프로필 / 작성자 리뷰 개수
- **리뷰 작성**
  - 리뷰 내용
  - **평점**
  - **사진 추가**
- **리뷰 정보**
  - 리뷰 작성 시간 / 리뷰 내용 / 리뷰 평점 / 작성자 프로필 / 작성자 리뷰 개수
- **리뷰 수정**
- **리뷰 삭제**

---

## **🧩 DB 설계**

![](./img/DB.png)

---

## **🍔 서비스 소개**

<br/>

<details>
<summary>접기/펼치기</summary>

### **1. 메인화면**

![](./img/main-01.png)
![](./img/main-02.png)
![](./img/main-03.png)

- 메인화면에서는 식당을 찾아볼 수 있도록 `검색창과 베스트 맛집 리스트, 최근 맛집 스토리, 평점이 높은 식당`으로 구성되었습니다.

---

### **2. 맛집 리스트**

#### 2-1. 메뉴별 리스트

![](./img/top_list.png)

- 메뉴별 리스트에서는 베스트 맛집 `카테고리별로 확인`할 수 있습니다.

<br />

#### 2-2. 식당별 리스트

![](./img/list.png)

- 식당별 리스트에서는 조회수, 식당 정보, 최근 리뷰 내용과 날짜를 `간략하게 확인`할 수 있습니다.
- `별점(가고싶다) 등록이 가능`합니다.

---

### **3. 식당 정보**

![](./img/restaurant_detail-01.png)
![](./img/restaurant_detail-02.png)

- 식당 위치와 정보, 조회수, 리뷰수, 별점수를 `자세히 확인`할 수 있습니다.
- `리뷰 등록`과 `별점(가고싶다) 등록`이 가능합니다.
- `리뷰 목록`을 확인할 수 있습니다.

---

### **4. 리뷰**

#### 4-1. 리뷰 작성

![](./img/review_create.png)

- 리뷰에는 `리뷰 내용과 평점, 사진을 작성`할 수 있습니다.
- `평점은 1~5점까지` 줄 수 있으며, 리뷰 목록에서는 `3점을 기준으로 맛있다, 괜찮다, 별로라는 이모지로 출력`됩니다.

<br />

#### 4-2. 리뷰 정보

![](./img/review_detail.png)

- `본인이 작성한 리뷰에서만 수정, 삭제가 가능`합니다.
- 본인이 작성하지 않았다면 `프로필 사진을 눌러 다른 유저의 프로필로 이동`합니다.

---

### **4. 스토리**

#### 4-1. 스토리 리스트

![](./img/story_list-01.png)
![](./img/story_list-02.png)

- 스토리는 `권한받은 유저만 사용이 가능`합니다.

<br />

#### 4-2. 스토리 정보

![](./img/story_detail-01.png)
![](./img/story_detail-02.png)
![](./img/story_detail-03.png)

- `summernote 사용`해 스토리 작성시 사진과 텍스트 입력이 가능하도록 하였습니다.
- 긴 글을 보고 난 이후에는 `다른 스토리를 손쉽게 찾아 볼 수 있도록 현재 스토리를 제외한 나머지 최근 스토리`를 볼 수 있게 하였습니다.

---

### **4. 회원**

#### 5-1. 회원 정보

![](./img/profile-01.png)
![](./img/profile-02.png)

- 회원 정보에서는 `회원이 작성한 리뷰`와 `회원간 팔로우 수를 확인`할 수 있습니다.
- `별점(가고싶다)을 준 식당의 목록을 확인`할 수 있습니다.
- 식당 사진에 마우스를 올리면 `식당에 별점을 준 회원 수와 식당의 리뷰 수를 확인`할 수 있습니다.
- `회원 정보 수정 및 삭제가 가능`합니다.

<br />

#### 5-2. 회원 간 팔로우

![](./img/profile_follow.png)

- `회원간 팔로우가 가능`합니다.

---

</details>

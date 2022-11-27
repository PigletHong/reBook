# reBook
![thumbnail](https://user-images.githubusercontent.com/57736547/204151531-a0ce8006-ffeb-4b29-b9d2-6084229f8e25.jpg)

덮은 책도 다시 보자 rebook


[▶ 시연영상 보러가기](https://www.youtube.com/watch?v=Jv_2PIKvnio)
## 🙇🏻‍♀️프로젝트 소개

책을 읽고 독후감을 쓰지 않는 현대인을 위한 독후감 서비스 프로젝트입니다.
책을 좋아하는 사용자들을 위해서 책 관련 정보들을 확인할 수 있으며 서로의 리뷰를 공유할 수 있습니다.

## 📆제작 기간
2022.11.14 ~ 2022.11.16

## 🖼와이어 프레임
![images](https://user-images.githubusercontent.com/57736547/204151482-5b606666-be18-4891-a34d-2fd922a7e7b0.png)

## 🔨개발 스택
- Frontend : HTML5, CSS3, JavaScript, Jquery, Ajax
- Backend : Python, Flask , JWT, BS4, Datetime, hashlib
- DB : MongoDB Atlas
- Infrastructure : AWS EC2

## ⚙핵심 기능
(1) 로그인/회원가입

- jwt를 이용한 로그인/로그아웃

(2) 웹 크롤링

- selenium을 이용한 동적 웹 크롤링
- 신상품, 베스트 셀러 정보 크롤링
- 작성자가 입력한 책 url을 크롤링하여 리뷰 작성에 도움

## 🚀이슈

<details>
<summary>aws ec2 우분투 환경에서 셀레니움이 작동하지 않는 오류</summary>
<!--  -->

[해결 방법 보러 가기](https://synuns.tistory.com/13)

</details>

<details>
<summary>화면 렌더링 오류</summary>
<!--  -->

크롤링이 완료된 이후에 렌더링이 일어나게 되는데 크롤링이 너무 오래걸려서 일어나는 오류

해결방법 : 크롤링은 서버에서 주기적인 시간마다 실행되며 db에 저장되는 식으로 수정해야 할 것으로 보임

*시간 부족으로 해결하지 못했음*

</details>

<details>
<summary> 크롤링 시 이미지를 크롤링하지 못하는 오류 </summary>
<!--  -->

동적 페이지의 이미지가 lazy loading 옵션을 가지고 있어서 로딩되는 시간보다 페이지를 크롤링한 속도가 빨라서 발생한 오류

해결방법 : 크롤링 스크립트의 속도를 조절해야함

*시간 부족으로 해결하지 못했음*

</details>

## 팀원

| <img src="https://github.com/synuns.png" width=200px alt="_"/> | <img src="https://github.com/PigletHong.png" width=200px alt="_"/> | <img src="https://github.com/dbfl720.png" width=200px alt="_"/> | <img src="https://github.com/Jeongubeom.png" width=200px alt="_"/> |
| :------------------------------------------------------------: | :----------------------------------------------------------------: | :-------------------------------------------------------------: | :----------------------------------------------------------------: |
|              [장신원](https://github.com/synuns)               |              [홍윤재](https://github.com/PigletHong)               |              [홍유리](https://github.com/dbfl720)               |              [정우범](https://github.com/Jeongubeom)               |
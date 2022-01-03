# Portfolio - PLATE STUDIO

<details open="open">
  <summary>Contents</summary>
  <ol>
    <li>
      <a href="#개요">개요</a>
    </li>
    <li>
      <a href="#내용">내용</a>
    </li>
    <li><a href="#구현-페이지">구현 페이지</a>
      <ul>
        <li><a href="#main">메인 페이지</a></li>
        <li><a href="#item">제품 페이지</a></li>
        <li><a href="#search">검색창</a></li>
        <li><a href="#cart">장바구니</a></li>
        <li><a href="#order">주문 · 결제</a></li>
        <li><a href="#sign">로그인, 회원가입</a></li>
        <li><a href="#faq">FAQ 페이지</a></li>
      </ul>
    </li>
  </ol>
</details>

---

# 개요
⭐ 프로젝트 명 : PLATE-STUDIO<br><br>
🚩 프로젝트 기간 : 2021년 11월 22일 ~ 12월 17일 (총 4주)<br><br>
💡 개발 목적 : 대학교 수업에서 배운 Django를 활용하여 아기자기한 식기를 판매하는 온라인 쇼핑몰 웹사이트 제작<br><br>
⌨️ 사용된 기술 스택<br><br>
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white">
<img src="https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html&logoColor=white">
<img src="https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css&logoColor=white">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">

---

# 내용
**기능**
* 고객 : 회원가입, 게시판 조회, 상품 조회, 상품목록 조회<br>

* 회원 : 상품 주문, 결제, 장바구니 담기, 장바구니 상품 삭제<br>

* 관리자 : 게시판 관리, 카테고리 관리, 회원 관리, 상품 관리<br>

<br>

**Usecase Diagram**
![UsecaseDiagram](https://user-images.githubusercontent.com/90684987/147316228-5226ec19-c8dc-4fdd-a324-078b71379c4c.png)

**ERD Diagram**
![ErdDiagram](https://user-images.githubusercontent.com/90684987/147316171-b88db8e9-017f-4fde-8135-3a1a144b310c.png)

---

# 구현 페이지

<h3 id = "main">메인 페이지</h3>

https://user-images.githubusercontent.com/90684987/147317659-5dad73ad-9de4-4a22-9c89-e91a4e598335.mp4

» 구현 기능<br>

    * 전체 제품 리스트 화면에 render
    
    * 페이징을 통해 제품 목록 넘기기
    
    * 웹사이트 로고 클릭을 통해 메인 페이지로 이동
    
    * Navbar를 사용한 메뉴바

<h3 id = "item">제품 페이지</h3>

https://user-images.githubusercontent.com/90684987/147429079-40440b7a-9b15-4305-a859-4a3c9098f73a.mp4

» 구현 기능<br>

    * 카테고리별 제품 리스트 화면에 render
    
    * 페이징을 통해 제품 목록 넘기기
    
    * 클릭 시, 제품 상세 페이지로 이동
    
    * 제품 상세 정보를 화면에 render
    
<h3 id = "search">검색창</h3>

https://user-images.githubusercontent.com/90684987/147429323-c2bc2629-be4c-4cc6-b5cc-f447ce3c099b.mp4

» 구현 기능<br>

    * navbar의 검색창을 통해 검색하고자 하는 단어 입력
    
    * DB에 등록된 상품명 중 단어가 포함되는 제품 리스트 render
    
    * 검색된 결과가 없을 시 메시지 render
    
    * 클릭 시, 제품 상세 페이지로 이동
    
<h3 id = "cart">장바구니</h3>

https://user-images.githubusercontent.com/90684987/147429453-2890c6b4-2c4b-4264-ba51-45b2874bcd96.mp4

» 구현 기능<br>

    * 제품 상세 페이지에서 add to cart 버튼 클릭시 장바구니 화면 render
    
    * 사용자가 담은 장바구니 제품 리스트를 화면에 render
    
    * +,-,휴지통 버튼 클릭 시 제품 수량 변경 및 삭제
    
    * 장바구니에 제품이 없을 시 navbar에 장바구니 버튼 숨김, 주소를 통해 접근할 경우 장바구니 상품이 없음에 대한 메시지 render
    
    * 장바구니에 제품이 있을 시 navbar에 장바구니 버튼과 제품 수량 render
    
<h3 id = "order">주문 결제</h3>

https://user-images.githubusercontent.com/90684987/147434386-e9c7a665-c020-463d-a863-4450004c5db0.mp4

» 구현 기능<br>

    * Stripe 플랫폼를 이용한 제품 결제 템플릿 사용
    
    * 장바구니 페이지에서 pay now! 버튼 클릭시 결제 화면 render
    
    * 개인 정보 입력 후 결제 버튼 누르면 주문 완료됨
    
    * 주문 완료되면 장바구니의 상품이 사라지고 메인 페이지로 이동
    
<h3 id = "sign">로그인, 회원가입</h3>

로그인 페이지

https://user-images.githubusercontent.com/90684987/147433599-426f605c-922a-4453-b5ee-7350492d6ff0.mp4

회원가입 페이지

https://user-images.githubusercontent.com/90684987/147434477-92902a61-9ae2-4b10-9334-d214b441b1fc.mp4

» 구현 기능<br>

    * sign up 메뉴를 통해 회원가입 페이지로 login 메뉴를 통해 로그인 페이지로 이동
    
    * 회원가입 페이지에서 username, password, email, address, phone number 등의 정보 입력
    
    * 로그인 페이지에서 회원가입 시 입력한 username, password 입력
    
    * 회원가입 페이지에서 비밀번호 확인 칸과 비밀번호가 일치하지 않거나, 로그인 페이지에서 비밀번호가 틀리거나,
      두 페이지에서 모든 칸에 정보를 입력하지 않을 경우 오류 메시지 출력
    
    * 회원가입 페이지에서 sign up 버튼 로그인 페이지에서 login 버튼 클릭시 메인 화면 페이지로 이동

<h3 id = "faq">FAQ 페이지</h3>

https://user-images.githubusercontent.com/90684987/147434664-f93d6485-1276-497d-99bb-3fa0177932d4.mp4

» 구현 기능<br>

    * admin 페이지를 통해 글쓰기 가능
    
    * FAQ 메뉴를 통해 FAQ 패이지로 이동
    
    * 홈페이지 내에서 게시글 수정, 삭제, 게시 제한
    
    * 보고자 하는 게시글 클릭시 상세 글 조회

---

<p align = "center">
지금까지 읽어주셔서 감사합니다!🙇‍♀️
</p>

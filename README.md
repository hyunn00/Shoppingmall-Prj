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
⭐ 프로젝트 명 : PLATE-STUDIO<br>
🚩 프로젝트 기간 : 2021년 11월 22일 ~ 12월 17일 (총 4주)<br>
💡 개발 목적 : 대학교 수업에서 배운 Django를 활용하여 아기자기한 식기를 판매하는 온라인 쇼핑몰 웹사이트 제작<br>
⌨️ 사용된 기술 스택 : Django, Javascripts, HTML, CSS, Python

---

# 내용
**기능**
* 고객 : 회원가입, 게시판 조회, 상품 조회, 상품목록 조회
* 회원 : 상품 주문, 결제, 장바구니 담기, 장바구니 상품 삭제
* 관리자 : 게시판 관리, 카테고리 관리, 회원 관리, 상품 관리

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

» 구현 기능<br>

    * 카테고리별 제품 리스트 화면에 render
    * 페이징을 통해 제품 목록 넘기기
    * 클릭 시, 제품 상세 페이지로 이동
    * 제품 상세 정보를 화면에 render
    
<h3 id = "search">검색창</h3>

» 구현 기능<br>

    * navbar의 검색창을 통해 검색하고자 하는 단어 입력
    * DB에 등록된 상품명 중 단어가 포함되는 제품 리스트 render
    * 검색된 결과가 없을 시 메시지 render
    * 클릭 시, 제품 상세 페이지로 이동
    
<h3 id = "cart">장바구니</h3>

» 구현 기능<br>

    * 제품 상세 페이지에서 add to cart 버튼 클릭시 장바구니 화면 render
    * 사용자가 담은 장바구니 제품 리스트를 화면에 render
    * +,-,휴지통 버튼 클릭 시 제품 수량 변경 및 삭제
    * 장바구니에 제품이 없을 시 navbar에 장바구니 버튼 숨김
    * 장바구니에 제품이 있을 시 navbar에 장바구니 버튼과 제품 수량 render
    
<h3 id = "order">주문 결제</h3>

» 구현 기능<br>

    * 
    
<h3 id = "sign">로그인, 회원가입</h3>

» 구현 기능<br>

    * 

<h3 id = "faq">FAQ 페이지</h3>

» 구현 기능<br>

    * 

---

<p align = "center">
지금까지 읽어주셔서 감사합니다!🙇‍♀️
</p>

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
        <li><a href="#item">제품 리스트 페이지</a></li>
        <li><a href="#detail">제품 상세 페이지</a></li>
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

    * 전체 제품 목록 조회
    * 페이징을 통해 제품 목록 넘기기
    * 웹사이트 로고 클릭을 통해 메인 페이지로 이동
    * Navbar를 사용한 메뉴바

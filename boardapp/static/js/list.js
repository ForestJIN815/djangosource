const actionForm = document.querySelector("#actionForm");

// .page-link 클릭 시 a 태그 기능 중지
// page 번호 가져온 후 actionForm 안의 페이지 값 변경
// actionForm 보내기
document.querySelector(".pagination").addEventListener("click", (e) => {
  e.preventDefault();
  actionForm.page.value = e.target.getAttibute("href");
  actionForm.action = "/board";
  actionForm.submit();
});

// 제목 클릭 시 a 태그 중지 / href 값 가져오기
// actionForm action 수정 후 actionForm 보내기
document.querySelector("tbody").addEventListener("click", (e) => {
  e.preventDefault();
  actionForm.action = e.target.getAttibute("href");
  actionForm.submit();
});

// 정렬 기준 change 일어나면
document.querySelector(".so").addEventListener("change", (e) => {
  // 사용자가 선택한 value 가져온 후 actionForm so 필드 값 변경
  actionForm.so.value = e.target.value;
  actionForm.action = "/board";
  // actionForm 보내기
  actionForm.submit();
});

// 찾기 버튼 클릭 시(검색)
document
  .querySelector(".btn-outline-secondary")
  .addEventListener("click", () => {
    // actionForm 보내기
    // 사용자가 입력한 keyword를 actionForm 의 keyword 값으로 변경
    // page = 1 변경
    actionForm.keyword.value = document.querySelector("[name='keyword']").value;
    actionForm.page.value = 1;
    actionForm.action = "/board";
    actionForm.submit();
  });

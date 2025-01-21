const actionForm = document.querySelector("#actionForm");

// 정렬 기준 change 일어나면
document.querySelector(".so").addEventListener("change", (e) => {
  // 사용자가 선택한 value 가져온 후 actionForm so 필드 값 변경
  actionForm.so.value = e.target.value;
  // actionForm 보내기
  actionForm.submit();
});

// 찾기 버튼 클릭 시(검색)
document.querySelector(".btn-outline-secondary").addEventListener("click", () => {
  // actionForm 보내기
  // 사용자가 입력한 keyword를 actionForm 의 keyword 값으로 변경
  // page = 1 변경
  actionForm.keyword.value = document.querySelector("[name='keyword']").value;
  actionForm.page.value = 1;
  actionForm.submit();
});

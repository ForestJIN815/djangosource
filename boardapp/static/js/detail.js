// 목록으로 클릭 시 actionForm 보내기
const actionForm = document.querySelector("#actionForm");
document.querySelector(".btn-success").addEventListener("click", () => {
  actionForm.submit();
});

const elements = document.querySelectorAll(".delete");

elements.forEach((element) => {
  element.addEventListener("click", (e) => {
    if (confirm("정말로 삭제하시겠습니까?")) {
      location.href = e.target.dataset.uri;
    }
  });
});

const elements = document.querySelectorAll(".delete");

elements.forEach((element) => {
  element.addEventListener("click", (e) => {
    if (confirm("정말로 삭제하시겠습니까?")) {
      location.href = e.target.dataset.uri;
    }
  });
});

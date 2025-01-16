// navbar-nav li:last-child 클릭 시 logoutForm 보내기
document.querySelector(".navbar-nav li:last-child").addEventListener("click", () => {
  document.querySelector("#logoutForm").submit();
});

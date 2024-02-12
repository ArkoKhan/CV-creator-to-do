let taskDoneBtn = document.querySelectorAll(".done");
let task = document.querySelectorAll(".task");

for (let i = 0; i < task.length; i++) {
  taskDoneBtn[i].addEventListener("click", function () {
    task[i].classList.toggle("done_task");
  });
}

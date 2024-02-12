const InputBox = document.getElementById('input-box');
const ListContainer = document.getElementById('list-container');

document.getElementById("input-box").addEventListener("keyup", function(event) {
    if (event.keyCode === 13) { 
      document.getElementById("add-button").click(); 
    }
  });

function AddTask(){
    if (InputBox.value === ''){
        alert('Please enter a task');
    }
    else{
        let li = document.createElement('li');
        li.innerHTML = InputBox.value;
        ListContainer.appendChild(li);
        let span = document.createElement('span');
        span.innerHTML = '🗑';
        li.appendChild(span);
    }
    InputBox.value = '';
    saveTasks();
}

ListContainer.addEventListener('click', function(e){
    if (e.target.tagName === 'LI'){
        e.target.classList.toggle('checked');
        saveTasks();
    }
    else if (e.target.tagName === 'SPAN'){
        e.target.parentElement.remove();
        saveTasks();
    }
}, false);

function saveTasks(){
    localStorage.setItem('tasks', ListContainer.innerHTML);
}

function showTasks(){
    ListContainer.innerHTML = localStorage.getItem('tasks');
}
showTasks();
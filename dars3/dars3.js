// // let text = document.getElementById
// // ('text').innerHTML += "<mark>Salom</mark>"


// let text = document.getElementById('text');
// text.innerHTML += "<mark>Salom</mark>";
// text.style.backgroundColor = "red";


const box = document.getElementById('box');

document.getElementById('add').addEventListener('click', function(){
    box.classList.add('active');
});

document.getElementById('remove').addEventListener('click',function(){
    box.classList.remove('active1');
});

document.getElementById('toggle').addEventListener('click',function(){
    box.classList.toggle('active2');
});

document.getElementById('check').addEventListener('click',function(){
    console.log(box.classList.contains('active3'));
});

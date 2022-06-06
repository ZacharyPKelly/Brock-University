'use strict';
const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const btnCloseModal = document.querySelector('.exit_modal');
const btnShowModal = document.querySelectorAll('.information')
 
 
const openModal = function(){
    modal.classList.remove('hidden')
    overlay.classList.remove('hidden')
}
 
for(let i=0;i<btnShowModal.length;i++){
   btnShowModal[i].addEventListener('click',openModal );
}
 
const closeModal = function(){
    modal.classList.add('hidden')
    overlay.classList.add('hidden')
}
btnCloseModal.addEventListener('click', closeModal)
overlay.addEventListener('click', closeModal)
 
document.addEventListener('keydown', function(e){
    if (e.key === 'Escape'){
        if(!modal.classList.contains('hidden'))
            {
                closeModal();
            }
    }
})
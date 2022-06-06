function modal(id)
{
    let el = document.getElementById(id);  // can also use a query selector
    let body = document.querySelector("body");
    let bg = document.createElement("div");
    bg.className = "modal-js-overlay";
    
    body.appendChild(bg);

    let close = document.createElement("span");
    close.className = "modal-js-close";
    close.innerHTML = "x";
    close.addEventListener('click', function () {
        let overlay = body.querySelector(".modal-js-overlay");
        let closebtn = parent.querySelector(".modal-js-close");

        body.removeChild(overlay);

        el.classList.remove('on');
        el.removeChild(closebtn);
    });
}
function modaloff(id) {
    let body = document.querySelector("body");
    let el = document.querySelector(id);
    let overlay = body.querySelector(".modal-js-overlay");

    el.classList.remove('on');
    body.removeChild(overlay);
}

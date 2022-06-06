function modal(id)
{
    let el = document.getElementById(id);  // can also use a query selector
    let body = document.querySelector("body");
    let bg = document.createElement("div");
    bg.className = "modal_js_overlay";
    
    body.appendChild(bg);

    let close = document.createElement("span");
    close.className = "exit_modal";
    close.innerHTML = "CLOSE";
    close.addEventListener('click', function () {
        let overlay = body.querySelector(".modal_js_overlay");
        let closebtn = parent.querySelector(".exit_modal");

        body.removeChild(overlay);

        el.classList.remove('on');
        el.removeChild(closebtn);
    });
}

function modaloff(id) {
    let body = document.querySelector("body");
    let el = document.querySelector(id);
    let overlay = body.querySelector(".modal_js_overlay");

    el.classList.remove('on');
    body.removeChild(overlay);
}

const burger = document.querySelector("#btnHamburger");
const body = document.querySelector('body')
const header = document.querySelector(".header")
const overlay = document.querySelector(".overlay_set")
const fadeElems = document.querySelectorAll(".has-fade")
const textbookPage = document.querySelectorAll(".subject_card")

burger.addEventListener("click", function () {
    body.classList.remove('noscroll')
    if (header.classList.contains("open")) {
        header.classList.remove("open")
        fadeElems.forEach(function (element) {
            element.classList.remove("fade-in")
            element.classList.add("fade-out")
        })



    } else {
        body.classList.add('noscroll')
        header.classList.add("open")
        fadeElems.forEach(function (element) {
            element.classList.add("fade-in")
            element.classList.remove("fade-out")
        })

    }
})


textbookPage.forEach(function (subject) {
    subject.addEventListener("click", function () {
        let subjectText = subject.id
        let link = "subject/" + subjectText
        window.open(link, "_self")
    })

})
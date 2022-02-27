function search() {
    let input, filter, bookCards, header, txtValue;
    input = document.getElementById("search-box")
    filter = input.value.toUpperCase();
    bookCards = document.querySelectorAll(".book_card");
    for (let i = 0; i < bookCards.length; i++) {
        header = bookCards[i].getElementsByTagName("h1")[0];
        txtValue = header.textContent || header.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1){
            bookCards[i].style.display = "";
        }else {
            bookCards[i].style.display = "none";
        }
        if (txtValue === ""){
            bookCards[i].style.display = "";
        }
    }
}
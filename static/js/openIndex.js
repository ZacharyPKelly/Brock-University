let url = "index.html"
let request = new XMLHttpRequest()
request.open('GET', url, true)
request.onload = function () {
    if (request.status >= 200 && request.status < 400){
        window.location = url
    }
}
request.send()
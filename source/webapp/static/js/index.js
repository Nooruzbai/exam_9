async function make_request(url, method = 'GET') {
    let response = await fetch(url, {method})
    if (response.ok) {
        console.log('OK')
        return await response.json();
    } else {
        console.log('Not Successful')
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }

}

let Favourite = async function (event) {

    let url = event.target.dataset.articlesUrl;

    let data = await make_request(url)
     console.log()
    let counter = document.getElementById(`${event.target.dataset.id}`);
    counter.innerText = `${data.like_quantity}`
    let like_button = document.getElementById('favourite')
    let button = event.target

    if (button.innerText == "favourite") {
        button.innerText = "favourite"

    } else {
        button.innerText = "notfavourite"
    }

}


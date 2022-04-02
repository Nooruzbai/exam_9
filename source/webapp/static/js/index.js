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
    console.log(event.target)

    let url = event.target.dataset.imageUrl;
    console.log(url)

    let data = await make_request(url)
    //  console.log()
    let button = event.target

    if (button.innerText == "favourite") {
        button.innerText = "notfavourite"

    } else {
        button.innerText = "favourite"
    }

}


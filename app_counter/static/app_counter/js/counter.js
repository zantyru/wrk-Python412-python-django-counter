function getCookie(name)
{
    let matches = document.cookie.match(
        new RegExp(
            "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
        )
    );

    return matches ? decodeURIComponent(matches[1]) : undefined;
}

function fetchCounterAPI(apiURL, token, payload=null, method="post")
{
    return fetch(
        apiURL,
        {
            method: method,
            headers: {
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json, text/plain',
                'Authorization': `Token ${token}`
            },
            body: payload ? JSON.stringify(payload) : ""
        }
    ).then(
        response => response.json()
    )
}

function updateCounterValue(apiURL)
{
    let token = getCookie("access_token");

    fetchCounterAPI(apiURL, token).then(
        data => {
            // alert(JSON.stringify(data));
            let counterId = data["counter"]["id"];
            let counterValue = data["counter"]["value"];
            let outputElement = document.querySelector(`#counter${counterId}`);
            outputElement.innerText = counterValue;
        }
    ).catch(
        error => console.log('increaseCounter [Error]:', error)
    );
}

//document.addEventListener("DOMContentLoaded", () => {
//    // Код-заглушка +++
//    fetch(
//        'http://127.0.0.1:8000/api/counters/1/increase/',
//        {
//            method: 'post',
//            headers: {
//                'Accept': 'application/json, text/plain, */*',
//                'Content-Type': 'application/json, text/plain',
//                'Authorization': 'Token ...'
//            },
//            body: ""
//        }
//    ).then(
//        res => res.json()
//    ).then(
//        res => alert(JSON.stringify(res))
//    )
//    // Код-заглушка ---
//});
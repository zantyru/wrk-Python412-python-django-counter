function getToken()
{
    // Версия "Заглушка"

    let urlApiTokenAuth = "http://127.0.0.1:8000/api/token-auth/";
    let usernameInput = document.querySelector("#id_username");
    let passwordInput = document.querySelector("#id_password");
    let usernameEncoded = encodeURIComponent(usernameInput.value.trim());
    let passwordEncoded = encodeURIComponent(passwordInput.value);
    let payload = `username=${usernameEncoded}&password=${passwordEncoded}`;

    fetch(
        urlApiTokenAuth,
        {
            method: "post",
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            },
            body: payload
        }
    ).then(
        response => response.json()
    ).then(
        data => {
            let token = data["token"];

            if (!token) return;

            document.cookie = `access_token=${token}`;
        }
    )
}

document.addEventListener("DOMContentLoaded", () => {
    document.forms[0].addEventListener("submit", getToken);
});
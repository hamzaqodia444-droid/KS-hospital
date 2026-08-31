const API_URL = "http://127.0.0.1:8000";


const loginForm = document.getElementById("loginForm");


if (loginForm) {

    loginForm.addEventListener("submit", async function(e) {

        e.preventDefault();


        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;


        const message = document.getElementById("message");


        try {

            const response = await fetch(
                `${API_URL}/auth/login`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        username: username,
                        password: password
                    })
                }
            );


            const data = await response.json();


            if (response.ok) {

                localStorage.setItem(
                    "access_token",
                    data.access_token
                );


                localStorage.setItem(
                    "role",
                    data.role
                );


                localStorage.setItem(
                    "username",
                    data.username
                );


                message.innerHTML =
                "Login successful";

                setTimeout(() => {
                    window.location.href = "/dashboard";
                }, 1000);


                console.log(data);


            } else {

                message.innerHTML =
                data.detail || "Login failed";

            }


        } catch(error) {

            message.innerHTML =
            "Server connection error";

            console.error(error);

        }


    });

}

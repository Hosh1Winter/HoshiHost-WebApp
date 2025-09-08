document.getElementById('login-form').addEventListener("submit", function(e) {
                e.preventDefault();

                const username = document.getElementById("username").value;
                const password = document.getElementById("password").value;

                fetch("/login_try",{
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({username: username, password: password})
                })
                .then(response => response.json())
                .then(data => {
                    document.getElementById("login-state").textContent = data.message;
                })
                .catch(error => {
                    console.error("Error", error);
                    document.getElementById("login-state").textContent = "Login failed";
                });
            });
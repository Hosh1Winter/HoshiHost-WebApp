function start_server() {
                 fetch('/start_server', { method: 'POST' })
                .then(response => response.json())
                .then(data => alert(data.message));
            }
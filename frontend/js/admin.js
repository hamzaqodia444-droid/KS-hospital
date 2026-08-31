const token = localStorage.getItem("access_token");

if (!token) {
    window.location.href = "../login.html";
}


fetch("http://127.0.0.1:8000/admin/statistics", {

    method: "GET",

    headers: {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json"
    }

})

.then(response => response.json())

.then(data => {

    console.log('ADMIN API RESPONSE:', data);

    if(data.statistics){

        document.getElementById("users").innerHTML =
        data.statistics.users;

        document.getElementById("patients").innerHTML =
        data.statistics.patients;

        document.getElementById("doctors").innerHTML =
        data.statistics.doctors;

        document.getElementById("nurses").innerHTML =
        data.statistics.nurses;

    }

})

.catch(error => {

    console.log(error);

});

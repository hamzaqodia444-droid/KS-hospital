const role = localStorage.getItem("role");

if (!role) {
    window.location.href = "/login";
}

switch(role) {

    case "PATIENT":
        window.location.href = "/static/pages/patient-dashboard.html";
        break;

    case "DOCTOR":
        window.location.href = "/static/pages/doctor-dashboard.html";
        break;

    case "NURSE":
        window.location.href = "/static/pages/nurse-dashboard.html";
        break;

    case "ADMIN":
        window.location.href = "/static/pages/admin-dashboard.html";
        break;

    default:
        window.location.href = "/login";
}

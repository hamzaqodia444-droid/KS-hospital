import requests

BASE = "http://127.0.0.1:8000"


def login(username, password):
    r = requests.post(
        BASE + "/auth/login",
        json={
            "username": username,
            "password": password
        }
    )

    if r.status_code == 200:
        return r.json()["access_token"]

    print("Login failed:", r.text)
    return None


def check_access(role_name, token, paths):

    print("\n====== TESTING", role_name, "======")

    headers = {
        "Authorization": "Bearer " + token
    }

    for path in paths:

        r = requests.get(
            BASE + path,
            headers=headers
        )

        if r.status_code == 200:
            print(
                "[WARNING] ACCESS GRANTED",
                path,
                r.status_code
            )

        elif r.status_code in [401,403]:
            print(
                "[OK BLOCKED]",
                path,
                r.status_code
            )

        else:
            print(
                "[INFO]",
                path,
                r.status_code
            )


# Nurse account
nurse_token = login(
    "Nurse1",
    "StrongPass123"
)


# Endpoints nurse should NOT access

protected_doctor_admin = [

    "/admin/dashboard",

    "/admin/statistics",

    "/doctor/patients",

    "/doctor/patient/1/full-profile"

]


if nurse_token:

    check_access(
        "NURSE trying ADMIN/DOCTOR",
        nurse_token,
        protected_doctor_admin
    )


print("\n====== FINISHED ======")

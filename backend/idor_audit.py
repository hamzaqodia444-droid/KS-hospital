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

    r.raise_for_status()

    return r.json()["access_token"]


def test_patient_access(token, patient_ids):

    headers = {
        "Authorization": "Bearer " + token
    }

    print("\n====== IDOR AUTHORIZATION TEST ======\n")

    for pid in patient_ids:

        r = requests.get(
            f"{BASE}/doctor/patient/{pid}/full-profile",
            headers=headers
        )

        if r.status_code == 200:
            print(
                "[WARNING] ACCESS POSSIBLE:",
                "patient",
                pid
            )

        elif r.status_code in [403,404]:
            print(
                "[OK BLOCKED]:",
                "patient",
                pid,
                r.status_code
            )

        else:
            print(
                "[INFO]:",
                "patient",
                pid,
                r.status_code
            )


doctor_token = login(
    "Doctor1",
    "StrongPass123"
)


# جرّب أرقام مرضى مختلفة
test_patient_access(
    doctor_token,
    [
        1,
        2,
        3,
        999
    ]
)


print("\n====== FINISHED ======")

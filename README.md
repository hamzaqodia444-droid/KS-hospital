# KS-Hospital Management System

> **Full-Stack Role-Based Hospital Management Platform & Web Authorization Security Lab (`FastAPI` + `RBAC` / `IDOR` Auditing)**  
> **مشروع متكامل لمحاكاة نظام إدارة المستشفيات بلغة Python (FastAPI) مع اختبارات أمنية لصلاحيات الوصول (RBAC & IDOR)**

**KS-Hospital** is a full-stack web application simulating real-world clinical, administrative, and financial workflows inside a hospital. Built on a layered **FastAPI** backend (`routes` → `services` → `models` → `schemas`) with **JWT + Bcrypt** authentication and **4 dedicated frontend dashboards**, the project also serves as a practical **Application Security (AppSec)** lab equipped with automated scripts to audit **Role-Based Access Control (`RBAC`)** and **Insecure Direct Object Reference (`IDOR`)** protections across sensitive medical endpoints.

---

## Core Capabilities & Role Dashboards

The platform enforces strict role separation across four primary user portals:

| Role | Frontend Portal | Core Workflows & Permissions |
| :--- | :--- | :--- |
| **Admin** | `admin-dashboard.html` | View hospital-wide operational statistics (`/admin/statistics`), register medical staff (`/admin/create-staff`), manage hospital departments, and assign doctors to patients (`/admin/assign-doctor/{doctor_id}/{patient_id}`). |
| **Doctor** | `doctor-dashboard.html` | View assigned patients, inspect authorized full clinical profiles (`/doctor/patient/{patient_id}/full-profile`), update medical records, issue prescriptions, and request laboratory or radiology exams. |
| **Nurse** | `nurse-dashboard.html` | Track patient care workflows, record clinical observations, and manage nursing notes (`/nurse/notes`). |
| **Patient** | `patient-dashboard.html` | Book and track appointments, view personal prescriptions, lab & radiology results, hospital admissions, and billing statements. |

---

## Backend Modules (14 Operational Domains)

The backend (`backend/app/`) follows a clean modular architecture with separated SQLAlchemy ORM models, Pydantic validation schemas, business-logic services, and REST routers across **14 hospital domains**:

1. **Authentication (`auth`)** — User registration (`/auth/register`), login (`/auth/login`), `bcrypt` password hashing, and `JWT` bearer token issuance.
2. **Administration (`admin`)** — Staff provisioning, doctor-patient linking, and system analytics.
3. **Departments (`department`)** — Hospital clinical unit creation and listing.
4. **Doctors (`doctor`)** — Doctor profiles, assigned patient queues, and full patient medical dossiers.
5. **Nurses (`nurse`)** — Nurse portal operations and clinical nursing notes.
6. **Patients (`patient`)** — Patient profiles and personal health summaries.
7. **Appointments (`appointment`)** — Scheduling and tracking doctor consultations.
8. **Admissions (`admission`)** — Inpatient ward admissions and status updates.
9. **Medical Records (`medical_record`)** — Diagnoses, clinical histories, and treatment updates.
10. **Medicines (`medicine`)** — Pharmacy inventory catalog.
11. **Prescriptions (`prescription`)** — Digital medication orders linked to patients and doctors.
12. **Laboratory Tests (`lab_test`)** — Diagnostic lab orders and test results.
13. **Radiology (`radiology`)** — Medical imaging requests and radiology reports.
14. **Billing (`billing`)** — Patient invoices and payment status management.

---

## Application Security & Authorization Auditing (`AppSec`)

Because healthcare systems process sensitive patient records, **KS-Hospital** includes dedicated security verification scripts under `backend/` to validate access controls against common **OWASP Top 10 (Broken Access Control)** vulnerabilities:

- **`backend/rbac_audit.py` — Role-Based Access Control Auditor:**  
  Authenticates across lower-privileged roles (such as `Nurse`) and probes restricted administrative and cross-role endpoints, verifying that unauthorized requests are rejected with `HTTP 401/403` rather than `HTTP 200`.
- **`backend/idor_audit.py` — IDOR Authorization Tester:**  
  Tests horizontal and vertical privilege boundaries on sensitive medical endpoints (such as `/doctor/patient/{patient_id}/full-profile`) across sequential `patient_id` values to verify that doctors cannot access unassigned patient records.
- **`tests/test_auth.py` — Authentication Test Suite:**  
  Validates authentication and token verification workflows.

---

## Tech Stack

- **Backend:** Python, FastAPI, Uvicorn, SQLAlchemy ORM, Pydantic, SQLite (`hospital.db`)
- **Security & Auth:** JWT (`python-jose`), Password Hashing (`passlib` / `bcrypt`), CORS Middleware, Custom `RBAC` & `IDOR` Audit Scripts
- **Frontend:** HTML5, Responsive CSS3, Vanilla JavaScript (`Fetch API` modular client)

---

## Project Structure

```text
KS-hospital/
├── backend/
│   ├── app/
│   │   ├── main.py                # FastAPI entrypoint, CORS config & router registration
│   │   ├── core/                  # Security (JWT/Bcrypt), dependencies & configuration
│   │   ├── database/              # SQLAlchemy engine & session management
│   │   ├── models/                # 14 SQLAlchemy ORM database models
│   │   ├── schemas/               # Pydantic request/response schemas
│   │   ├── services/              # Business logic layer across all hospital modules
│   │   └── routes/                # REST API endpoints for Auth, Roles & Clinical services
│   ├── rbac_audit.py              # Automated Role-Based Access Control security audit script
│   ├── idor_audit.py              # Automated IDOR patient-profile authorization tester
│   └── requirements.txt           # Backend Python dependencies
├── frontend/
│   ├── index.html                 # Landing page
│   ├── login.html / register.html # Authentication portals
│   ├── pages/                     # Role dashboards (Admin, Doctor, Nurse, Patient)
│   ├── css/style.css              # Responsive stylesheet
│   └── js/                        # API client, authentication state & dashboard controllers
├── database/                      # Local SQLite database storage
└── tests/
    └── test_auth.py               # Authentication unit tests
```

---

## Running Locally

### 1. Install Dependencies

```bash
git clone https://github.com/hamzaqodia444-droid/KS-hospital.git
cd KS-hospital/backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Start the FastAPI Server

> **Tip:** Before running on a new machine, make sure static/template paths in `backend/app/main.py` point to your local `../frontend` directory.

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

- **Interactive Swagger API Docs:** `http://127.0.0.1:8000/docs`
- **ReDoc API Reference:** `http://127.0.0.1:8000/redoc`

### 3. Run Security Audits (with the server running)

```bash
python3 rbac_audit.py
python3 idor_audit.py
```

---

## نبذة بالعربية

**KS-Hospital** هو مشروع ويب متكامل يحاكي نظام إدارة المستشفيات الحديث، تم تطويره باستخدام إطار **FastAPI** وقواعد بيانات **SQLAlchemy** مع نظام مصادقة محمي عبر **JWT** وتشفير **Bcrypt**. يدعم النظام **4 لوحات تحكم مستقلة** (المدير، الطبيب، الممرض، المريض) عبر **14 وحدة برمجية** تشمل المواعيد، التنويم، السجلات الطبية، الوصفات، الصيدلية، المختبر، الأشعة، والفوترة، كما يتضمن سكربتات فحص أمني آلي (`rbac_audit.py` و `idor_audit.py`) لاختبار حماية بيانات المرضى ضد ثغرات تجاوز الصلاحيات.

---

## Author

**Hamza Qodia (BMB)** — [@hamzaqodia444-droid](https://github.com/hamzaqodia444-droid)

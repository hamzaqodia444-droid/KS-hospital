from sqlalchemy.orm import Session

from app.models.department import Department
from app.models.doctor import Doctor

from app.schemas.doctor import DoctorCreate





def create_doctor(
    db: Session,
    user_id: int,
    doctor_data: DoctorCreate
):

    department = (
        db.query(Department)
        .filter(
            Department.id == doctor_data.department_id
        )
        .first()
    )


    if not department:

        return None, "Department not found"



    existing_doctor = (
        db.query(Doctor)
        .filter(
            Doctor.user_id == user_id
        )
        .first()
    )


    if existing_doctor:

        return None, "Doctor profile already exists"



    existing_license = (
        db.query(Doctor)
        .filter(
            Doctor.license_number == doctor_data.license_number
        )
        .first()
    )


    if existing_license:

        return None, "License number already exists"



    doctor = Doctor(

        user_id=user_id,

        department_id=doctor_data.department_id,

        full_name=doctor_data.full_name,

        specialization=doctor_data.specialization,

        license_number=doctor_data.license_number,

        phone=doctor_data.phone

    )


    db.add(doctor)

    db.commit()

    db.refresh(doctor)


    return doctor, None





def get_doctor_by_user(
    db: Session,
    user_id: int
):

    return (
        db.query(Doctor)
        .filter(
            Doctor.user_id == user_id
        )
        .first()
    )


from app.models.patient import Patient
from app.models.medical_record import MedicalRecord


def get_doctor_patients(
    db: Session,
    doctor_id: int
):

    patients = (
        db.query(Patient)
        .join(
            MedicalRecord,
            MedicalRecord.patient_id == Patient.id
        )
        .filter(
            MedicalRecord.doctor_id == doctor_id
        )
        .distinct()
        .all()
    )


    return patients


from app.models.prescription import Prescription
from app.models.appointment import Appointment
from app.models.lab_test import LabTest
from app.models.radiology import Radiology
from app.models.admission import Admission
from app.models.billing import Billing


def get_full_patient_profile(
    db: Session,
    patient_id: int,
    doctor_id: int
):

    patient = (
        db.query(Patient)
        .filter(
            Patient.id == patient_id
        )
        .first()
    )


    if not patient:
        return None


    records = (
        db.query(MedicalRecord)
        .filter(
            MedicalRecord.patient_id == patient_id,
            MedicalRecord.doctor_id == doctor_id
        )
        .all()
    )


    prescriptions = (
        db.query(Prescription)
        .filter(
            Prescription.patient_id == patient_id,
            Prescription.doctor_id == doctor_id
        )
        .all()
    )


    appointments = (
        db.query(Appointment)
        .filter(
            Appointment.patient_id == patient_id,
            Appointment.doctor_id == doctor_id
        )
        .all()
    )


    lab_tests = (
        db.query(LabTest)
        .filter(
            LabTest.patient_id == patient_id,
            LabTest.doctor_id == doctor_id
        )
        .all()
    )


    radiology_tests = (
        db.query(Radiology)
        .filter(
            Radiology.patient_id == patient_id,
            Radiology.doctor_id == doctor_id
        )
        .all()
    )


    admissions = (
        db.query(Admission)
        .filter(
            Admission.patient_id == patient_id,
            Admission.doctor_id == doctor_id
        )
        .all()
    )


    bills = (
        db.query(Billing)
        .filter(
            Billing.patient_id == patient_id
        )
        .all()
    )


    return {

        "patient": {
            "id": patient.id,
            "full_name": patient.full_name,
            "birth_date": str(patient.birth_date),
            "gender": patient.gender,
            "blood_type": patient.blood_type
        },

        "medical_records": [
            {
                "id": r.id,
                "disease_name": r.disease_name,
                "description": r.description,
                "severity": r.severity
            }
            for r in records
        ],

        "prescriptions": [
            {
                "id": p.id,
                "medicine_id": p.medicine_id,
                "instructions": p.instructions
            }
            for p in prescriptions
        ],

        "appointments": [
            {
                "id": a.id
            }
            for a in appointments
        ],

        "lab_tests": [
            {
                "id": l.id,
                "status": l.status
            }
            for l in lab_tests
        ],

        "radiology_tests": [
            {
                "id": r.id,
                "test_type": r.test_type,
                "status": r.status
            }
            for r in radiology_tests
        ],

        "admissions": [
            {
                "id": a.id,
                "status": a.status
            }
            for a in admissions
        ],

        "billings": [
            {
                "id": b.id
            }
            for b in bills
        ]

    }

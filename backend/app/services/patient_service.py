from sqlalchemy.orm import Session

from app.models.patient import Patient
from app.schemas.patient import PatientCreate



def create_patient(
    db: Session,
    user_id: int,
    patient_data: PatientCreate
):

    existing_patient = (
        db.query(Patient)
        .filter(Patient.user_id == user_id)
        .first()
    )


    if existing_patient:

        return None, "Patient profile already exists"



    patient = Patient(

        user_id=user_id,

        full_name=patient_data.full_name,

        birth_date=patient_data.birth_date,

        birth_place=patient_data.birth_place,

        gender=patient_data.gender,

        age=patient_data.age,

        height=patient_data.height,

        weight=patient_data.weight,

        blood_type=patient_data.blood_type

    )


    db.add(patient)

    db.commit()

    db.refresh(patient)


    return patient, None





def get_patient_by_user(
    db: Session,
    user_id: int
):

    patient = (
        db.query(Patient)
        .filter(Patient.user_id == user_id)
        .first()
    )


    if not patient:

        return None


    return patient

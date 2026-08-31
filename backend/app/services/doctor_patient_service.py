from sqlalchemy.orm import Session

from app.models.doctor_patient import DoctorPatient


def assign_patient(
    db: Session,
    doctor_id: int,
    patient_id: int
):

    exists = (
        db.query(DoctorPatient)
        .filter(
            DoctorPatient.doctor_id == doctor_id,
            DoctorPatient.patient_id == patient_id
        )
        .first()
    )

    if exists:
        return None, "Already assigned"


    relation = DoctorPatient(
        doctor_id=doctor_id,
        patient_id=patient_id
    )

    db.add(relation)
    db.commit()
    db.refresh(relation)

    return relation, None



def get_doctor_patients(
    db: Session,
    doctor_id: int
):

    return (
        db.query(DoctorPatient)
        .filter(
            DoctorPatient.doctor_id == doctor_id
        )
        .all()
    )

from sqlalchemy.orm import Session
from datetime import datetime

from app.models.admission import Admission

from app.schemas.admission import (
    AdmissionCreate,
    DischargeUpdate
)





def create_admission(
    db: Session,
    admission_data: AdmissionCreate
):

    admission = Admission(

        patient_id=admission_data.patient_id,

        doctor_id=admission_data.doctor_id,

        room_number=admission_data.room_number,

        admission_reason=admission_data.admission_reason

    )


    db.add(admission)

    db.commit()

    db.refresh(admission)


    return admission





def discharge_patient(
    db: Session,
    admission_id: int,
    discharge_data: DischargeUpdate
):

    admission = (
        db.query(Admission)
        .filter(
            Admission.id == admission_id
        )
        .first()
    )


    if not admission:

        return None


    admission.status = "DISCHARGED"

    admission.discharge_notes = (
        discharge_data.discharge_notes
    )

    admission.discharged_at = datetime.utcnow()


    db.commit()

    db.refresh(admission)


    return admission





def get_patient_admissions(
    db: Session,
    patient_id: int
):

    return (
        db.query(Admission)
        .filter(
            Admission.patient_id == patient_id
        )
        .all()
    )





def get_doctor_admissions(
    db: Session,
    doctor_id: int
):

    return (
        db.query(Admission)
        .filter(
            Admission.doctor_id == doctor_id
        )
        .all()
    )

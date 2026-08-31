from sqlalchemy.orm import Session

from app.models.prescription import Prescription

from app.schemas.prescription import PrescriptionCreate





def create_prescription(
    db: Session,
    doctor_id: int,
    prescription_data: PrescriptionCreate
):

    prescription = Prescription(

        patient_id=prescription_data.patient_id,

        doctor_id=doctor_id,

        medicine_id=prescription_data.medicine_id,

        instructions=prescription_data.instructions

    )


    db.add(prescription)

    db.commit()

    db.refresh(prescription)


    return prescription





def get_patient_prescriptions(
    db: Session,
    patient_id: int
):

    return (
        db.query(Prescription)
        .filter(
            Prescription.patient_id == patient_id
        )
        .all()
    )





def get_doctor_prescriptions(
    db: Session,
    doctor_id: int
):

    return (
        db.query(Prescription)
        .filter(
            Prescription.doctor_id == doctor_id
        )
        .all()
    )

from sqlalchemy.orm import Session

from app.models.medical_record import MedicalRecord
from app.schemas.medical_record import MedicalRecordCreate



def create_medical_record(
    db: Session,
    doctor_id: int,
    record_data: MedicalRecordCreate
):

    record = MedicalRecord(

        patient_id=record_data.patient_id,

        doctor_id=doctor_id,

        disease_name=record_data.disease_name,

        description=record_data.description,

        causes=record_data.causes,

        severity=record_data.severity

    )


    db.add(record)

    db.commit()

    db.refresh(record)


    return record





def get_patient_records(
    db: Session,
    patient_id: int
):

    records = (
        db.query(MedicalRecord)
        .filter(
            MedicalRecord.patient_id == patient_id
        )
        .all()
    )


    return records





def get_doctor_records(
    db: Session,
    doctor_id: int
):

    records = (
        db.query(MedicalRecord)
        .filter(
            MedicalRecord.doctor_id == doctor_id
        )
        .all()
    )


    return records


from app.schemas.medical_record import MedicalRecordUpdate



def update_medical_record(
    db: Session,
    record_id: int,
    doctor_id: int,
    update_data: MedicalRecordUpdate
):

    record = (
        db.query(MedicalRecord)
        .filter(
            MedicalRecord.id == record_id,
            MedicalRecord.doctor_id == doctor_id
        )
        .first()
    )


    if not record:
        return None, "Medical record not found or access denied"


    if update_data.disease_name is not None:
        record.disease_name = update_data.disease_name


    if update_data.description is not None:
        record.description = update_data.description


    if update_data.causes is not None:
        record.causes = update_data.causes


    if update_data.severity is not None:
        record.severity = update_data.severity


    db.commit()

    db.refresh(record)


    return record, None

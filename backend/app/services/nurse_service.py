from sqlalchemy.orm import Session

from app.models.department import Department
from app.models.nurse import Nurse

from app.schemas.nurse import NurseCreate





def create_nurse(
    db: Session,
    user_id: int,
    nurse_data: NurseCreate
):

    department = (
        db.query(Department)
        .filter(
            Department.id == nurse_data.department_id
        )
        .first()
    )


    if not department:

        return None, "Department not found"



    existing_nurse = (
        db.query(Nurse)
        .filter(
            Nurse.user_id == user_id
        )
        .first()
    )


    if existing_nurse:

        return None, "Nurse profile already exists"



    if nurse_data.license_number:

        existing_license = (
            db.query(Nurse)
            .filter(
                Nurse.license_number == nurse_data.license_number
            )
            .first()
        )


        if existing_license:

            return None, "License number already exists"



    nurse = Nurse(

        user_id=user_id,

        department_id=nurse_data.department_id,

        full_name=nurse_data.full_name,

        license_number=nurse_data.license_number,

        phone=nurse_data.phone

    )


    db.add(nurse)

    db.commit()

    db.refresh(nurse)


    return nurse, None





def get_nurse_by_user(
    db: Session,
    user_id: int
):

    return (
        db.query(Nurse)
        .filter(
            Nurse.user_id == user_id
        )
        .first()
    )


from datetime import datetime

from app.models.nursing_note import NursingNote
from app.schemas.nurse import NursingNoteCreate



def create_nursing_note(
    db: Session,
    nurse_id: int,
    note_data: NursingNoteCreate
):

    note = NursingNote(

        patient_id=note_data.patient_id,

        nurse_id=nurse_id,

        note=note_data.note,

        patient_status=note_data.patient_status,

        created_at=datetime.utcnow()

    )


    db.add(note)

    db.commit()

    db.refresh(note)


    return note





def get_nurse_notes(
    db: Session,
    nurse_id: int
):

    return (
        db.query(NursingNote)
        .filter(
            NursingNote.nurse_id == nurse_id
        )
        .all()
    )

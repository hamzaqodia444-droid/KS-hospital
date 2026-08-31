from sqlalchemy.orm import Session

from app.models.radiology import Radiology

from app.schemas.radiology import (
    RadiologyCreate,
    RadiologyUpdate
)





def create_radiology_test(
    db: Session,
    radiology_data: RadiologyCreate
):

    radiology = Radiology(

        patient_id=radiology_data.patient_id,

        doctor_id=radiology_data.doctor_id,

        test_type=radiology_data.test_type

    )


    db.add(radiology)

    db.commit()

    db.refresh(radiology)


    return radiology





def update_radiology_result(
    db: Session,
    radiology_id: int,
    radiology_data: RadiologyUpdate
):

    radiology = (
        db.query(Radiology)
        .filter(
            Radiology.id == radiology_id
        )
        .first()
    )


    if not radiology:

        return None


    radiology.result = radiology_data.result

    radiology.status = "COMPLETED"


    db.commit()

    db.refresh(radiology)


    return radiology





def get_patient_radiology_tests(
    db: Session,
    patient_id: int
):

    return (
        db.query(Radiology)
        .filter(
            Radiology.patient_id == patient_id
        )
        .all()
    )





def get_doctor_radiology_tests(
    db: Session,
    doctor_id: int
):

    return (
        db.query(Radiology)
        .filter(
            Radiology.doctor_id == doctor_id
        )
        .all()
    )

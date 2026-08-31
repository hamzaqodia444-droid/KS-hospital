from sqlalchemy.orm import Session

from app.models.lab_test import LabTest

from app.schemas.lab_test import (
    LabTestCreate,
    LabTestUpdate
)





def create_lab_test(
    db: Session,
    lab_data: LabTestCreate
):

    lab_test = LabTest(

        patient_id=lab_data.patient_id,

        doctor_id=lab_data.doctor_id,

        test_name=lab_data.test_name,

        result=lab_data.result

    )


    db.add(lab_test)

    db.commit()

    db.refresh(lab_test)


    return lab_test





def update_lab_result(
    db: Session,
    lab_id: int,
    lab_data: LabTestUpdate
):

    lab_test = (
        db.query(LabTest)
        .filter(
            LabTest.id == lab_id
        )
        .first()
    )


    if not lab_test:

        return None


    lab_test.result = lab_data.result

    lab_test.status = "COMPLETED"


    db.commit()

    db.refresh(lab_test)


    return lab_test





def get_patient_lab_tests(
    db: Session,
    patient_id: int
):

    return (
        db.query(LabTest)
        .filter(
            LabTest.patient_id == patient_id
        )
        .all()
    )





def get_doctor_lab_tests(
    db: Session,
    doctor_id: int
):

    return (
        db.query(LabTest)
        .filter(
            LabTest.doctor_id == doctor_id
        )
        .all()
    )

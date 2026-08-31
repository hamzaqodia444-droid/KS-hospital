from sqlalchemy.orm import Session

from app.models.appointment import Appointment

from app.schemas.appointment import AppointmentCreate





def create_appointment(
    db: Session,
    appointment_data: AppointmentCreate
):

    appointment = Appointment(

        patient_id=appointment_data.patient_id,

        doctor_id=appointment_data.doctor_id,

        appointment_date=appointment_data.appointment_date,

        appointment_time=appointment_data.appointment_time,

        notes=appointment_data.notes

    )


    db.add(appointment)

    db.commit()

    db.refresh(appointment)


    return appointment





def get_patient_appointments(
    db: Session,
    patient_id: int
):

    return (
        db.query(Appointment)
        .filter(
            Appointment.patient_id == patient_id
        )
        .all()
    )





def get_doctor_appointments(
    db: Session,
    doctor_id: int
):

    return (
        db.query(Appointment)
        .filter(
            Appointment.doctor_id == doctor_id
        )
        .all()
    )

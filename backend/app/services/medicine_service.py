from sqlalchemy.orm import Session

from app.models.medicine import Medicine

from app.schemas.medicine import MedicineCreate





def create_medicine(
    db: Session,
    medicine_data: MedicineCreate
):

    existing_medicine = (
        db.query(Medicine)
        .filter(
            Medicine.name == medicine_data.name
        )
        .first()
    )


    if existing_medicine:

        return None, "Medicine already exists"



    medicine = Medicine(

        name=medicine_data.name,

        description=medicine_data.description,

        usage=medicine_data.usage,

        side_effects=medicine_data.side_effects,

        warnings=medicine_data.warnings

    )


    db.add(medicine)

    db.commit()

    db.refresh(medicine)


    return medicine, None





def get_all_medicines(
    db: Session
):

    return (
        db.query(Medicine)
        .all()
    )

from sqlalchemy.orm import Session

from app.models.department import Department

from app.schemas.department import DepartmentCreate





def create_department(
    db: Session,
    department_data: DepartmentCreate
):

    existing_department = (
        db.query(Department)
        .filter(
            Department.name == department_data.name
        )
        .first()
    )


    if existing_department:

        return None, "Department already exists"



    department = Department(

        name=department_data.name,

        description=department_data.description

    )


    db.add(department)

    db.commit()

    db.refresh(department)


    return department, None





def get_all_departments(
    db: Session
):

    return (
        db.query(Department)
        .order_by(Department.name)
        .all()
    )

from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/customers/')
async def get_customers(db: Session = Depends(get_db)):
    try:
        return await service.get_customers(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/customers/customer_id')
async def get_customers_customer_id(customer_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_customers_customer_id(db, customer_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/customers/customer_id/')
async def put_customers_customer_id(customer_id: int, name: Annotated[str, Query(max_length=100)], contact_details: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_customers_customer_id(db, customer_id, name, contact_details)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/customers/customer_id')
async def delete_customers_customer_id(customer_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_customers_customer_id(db, customer_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/service_providers/')
async def get_service_providers(db: Session = Depends(get_db)):
    try:
        return await service.get_service_providers(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/service_providers/provider_id')
async def get_service_providers_provider_id(provider_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_service_providers_provider_id(db, provider_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/service_providers/')
async def post_service_providers(provider_id: int, name: Annotated[str, Query(max_length=100)], details: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.post_service_providers(db, provider_id, name, details)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/service_providers/provider_id/')
async def put_service_providers_provider_id(provider_id: int, name: Annotated[str, Query(max_length=100)], details: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_service_providers_provider_id(db, provider_id, name, details)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/service_providers/provider_id')
async def delete_service_providers_provider_id(provider_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_service_providers_provider_id(db, provider_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/services/')
async def get_services(db: Session = Depends(get_db)):
    try:
        return await service.get_services(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/services/service_id')
async def get_services_service_id(service_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_services_service_id(db, service_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/services/')
async def post_services(service_id: int, name: Annotated[str, Query(max_length=100)], duration_minutes: int, db: Session = Depends(get_db)):
    try:
        return await service.post_services(db, service_id, name, duration_minutes)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/services/service_id/')
async def put_services_service_id(service_id: int, name: Annotated[str, Query(max_length=100)], duration_minutes: int, db: Session = Depends(get_db)):
    try:
        return await service.put_services_service_id(db, service_id, name, duration_minutes)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/services/service_id')
async def delete_services_service_id(service_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_services_service_id(db, service_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/appointments/')
async def get_appointments(db: Session = Depends(get_db)):
    try:
        return await service.get_appointments(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/appointments/appointment_id')
async def get_appointments_appointment_id(appointment_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_appointments_appointment_id(db, appointment_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/appointments/')
async def post_appointments(appointment_id: int, customer_id: int, provider_id: int, service_id: int, appointment_datetime: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.post_appointments(db, appointment_id, customer_id, provider_id, service_id, appointment_datetime)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/appointments/appointment_id/')
async def put_appointments_appointment_id(appointment_id: int, customer_id: int, provider_id: int, service_id: int, appointment_datetime: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_appointments_appointment_id(db, appointment_id, customer_id, provider_id, service_id, appointment_datetime)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/appointments/appointment_id')
async def delete_appointments_appointment_id(appointment_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_appointments_appointment_id(db, appointment_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/schedules/')
async def get_schedules(db: Session = Depends(get_db)):
    try:
        return await service.get_schedules(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/schedules/schedule_id')
async def get_schedules_schedule_id(schedule_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_schedules_schedule_id(db, schedule_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/schedules/')
async def post_schedules(schedule_id: int, provider_id: int, start_time: Annotated[str, Query(max_length=100)], end_time: Annotated[str, Query(max_length=100)], is_booked: int, db: Session = Depends(get_db)):
    try:
        return await service.post_schedules(db, schedule_id, provider_id, start_time, end_time, is_booked)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/schedules/schedule_id/')
async def put_schedules_schedule_id(schedule_id: int, provider_id: int, start_time: Annotated[str, Query(max_length=100)], end_time: Annotated[str, Query(max_length=100)], is_booked: int, db: Session = Depends(get_db)):
    try:
        return await service.put_schedules_schedule_id(db, schedule_id, provider_id, start_time, end_time, is_booked)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/schedules/schedule_id')
async def delete_schedules_schedule_id(schedule_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_schedules_schedule_id(db, schedule_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/login')
async def post_login(email: Annotated[str, Query(max_length=100, pattern='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$')], password: Annotated[str, Query(max_length=100, pattern='^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[!@#$%^&*()_+\\-=\\[\\]{};\':"\\\\|,.<>\\/?~]).{8,}$')], db: Session = Depends(get_db)):
    try:
        return await service.post_login(db, email, password)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/customers/')
async def post_customers(customer_id: int, name: Annotated[str, Query(max_length=100)], contact_details: Annotated[str, Query(max_length=100)], email: Annotated[str, Query(max_length=100)], password: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.post_customers(db, customer_id, name, contact_details, email, password)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))


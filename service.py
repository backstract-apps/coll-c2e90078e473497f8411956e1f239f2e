from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
from pathlib import Path


async def get_customers(db: Session):

    query = db.query(models.Customers)

    customers_all = query.all()
    customers_all = (
        [new_data.to_dict() for new_data in customers_all]
        if customers_all
        else customers_all
    )
    res = {
        "customers_all": customers_all,
    }
    return res


async def get_customers_customer_id(db: Session, customer_id: int):

    query = db.query(models.Customers)
    query = query.filter(and_(models.Customers.customer_id == customer_id))

    customers_one = query.first()

    customers_one = (
        (
            customers_one.to_dict()
            if hasattr(customers_one, "to_dict")
            else vars(customers_one)
        )
        if customers_one
        else customers_one
    )

    res = {
        "customers_one": customers_one,
    }
    return res


async def put_customers_customer_id(
    db: Session, customer_id: int, name: str, contact_details: str
):

    query = db.query(models.Customers)
    query = query.filter(and_(models.Customers.customer_id == customer_id))
    customers_edited_record = query.first()

    if customers_edited_record:
        for key, value in {
            "name": name,
            "customer_id": customer_id,
            "contact_details": contact_details,
        }.items():
            setattr(customers_edited_record, key, value)

        db.commit()
        db.refresh(customers_edited_record)

        customers_edited_record = (
            customers_edited_record.to_dict()
            if hasattr(customers_edited_record, "to_dict")
            else vars(customers_edited_record)
        )
    res = {
        "customers_edited_record": customers_edited_record,
    }
    return res


async def delete_customers_customer_id(db: Session, customer_id: int):

    query = db.query(models.Customers)
    query = query.filter(and_(models.Customers.customer_id == customer_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        customers_deleted = record_to_delete.to_dict()
    else:
        customers_deleted = record_to_delete
    res = {
        "customers_deleted": customers_deleted,
    }
    return res


async def get_service_providers(db: Session):

    query = db.query(models.ServiceProviders)

    service_providers_all = query.all()
    service_providers_all = (
        [new_data.to_dict() for new_data in service_providers_all]
        if service_providers_all
        else service_providers_all
    )
    res = {
        "service_providers_all": service_providers_all,
    }
    return res


async def get_service_providers_provider_id(db: Session, provider_id: int):

    query = db.query(models.ServiceProviders)
    query = query.filter(and_(models.ServiceProviders.provider_id == provider_id))

    service_providers_one = query.first()

    service_providers_one = (
        (
            service_providers_one.to_dict()
            if hasattr(service_providers_one, "to_dict")
            else vars(service_providers_one)
        )
        if service_providers_one
        else service_providers_one
    )

    res = {
        "service_providers_one": service_providers_one,
    }
    return res


async def post_service_providers(
    db: Session, provider_id: int, name: str, details: str
):

    record_to_be_added = {"name": name, "details": details, "provider_id": provider_id}
    new_service_providers = models.ServiceProviders(**record_to_be_added)
    db.add(new_service_providers)
    db.commit()
    db.refresh(new_service_providers)
    service_providers_inserted_record = new_service_providers.to_dict()

    res = {
        "service_providers_inserted_record": service_providers_inserted_record,
    }
    return res


async def put_service_providers_provider_id(
    db: Session, provider_id: int, name: str, details: str
):

    query = db.query(models.ServiceProviders)
    query = query.filter(and_(models.ServiceProviders.provider_id == provider_id))
    service_providers_edited_record = query.first()

    if service_providers_edited_record:
        for key, value in {
            "name": name,
            "details": details,
            "provider_id": provider_id,
        }.items():
            setattr(service_providers_edited_record, key, value)

        db.commit()
        db.refresh(service_providers_edited_record)

        service_providers_edited_record = (
            service_providers_edited_record.to_dict()
            if hasattr(service_providers_edited_record, "to_dict")
            else vars(service_providers_edited_record)
        )
    res = {
        "service_providers_edited_record": service_providers_edited_record,
    }
    return res


async def delete_service_providers_provider_id(db: Session, provider_id: int):

    query = db.query(models.ServiceProviders)
    query = query.filter(and_(models.ServiceProviders.provider_id == provider_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        service_providers_deleted = record_to_delete.to_dict()
    else:
        service_providers_deleted = record_to_delete
    res = {
        "service_providers_deleted": service_providers_deleted,
    }
    return res


async def get_services(db: Session):

    query = db.query(models.Services)

    services_all = query.all()
    services_all = (
        [new_data.to_dict() for new_data in services_all]
        if services_all
        else services_all
    )
    res = {
        "services_all": services_all,
    }
    return res


async def get_services_service_id(db: Session, service_id: int):

    query = db.query(models.Services)
    query = query.filter(and_(models.Services.service_id == service_id))

    services_one = query.first()

    services_one = (
        (
            services_one.to_dict()
            if hasattr(services_one, "to_dict")
            else vars(services_one)
        )
        if services_one
        else services_one
    )

    res = {
        "services_one": services_one,
    }
    return res


async def post_services(db: Session, service_id: int, name: str, duration_minutes: int):

    record_to_be_added = {
        "name": name,
        "service_id": service_id,
        "duration_minutes": duration_minutes,
    }
    new_services = models.Services(**record_to_be_added)
    db.add(new_services)
    db.commit()
    db.refresh(new_services)
    services_inserted_record = new_services.to_dict()

    res = {
        "services_inserted_record": services_inserted_record,
    }
    return res


async def put_services_service_id(
    db: Session, service_id: int, name: str, duration_minutes: int
):

    query = db.query(models.Services)
    query = query.filter(and_(models.Services.service_id == service_id))
    services_edited_record = query.first()

    if services_edited_record:
        for key, value in {
            "name": name,
            "service_id": service_id,
            "duration_minutes": duration_minutes,
        }.items():
            setattr(services_edited_record, key, value)

        db.commit()
        db.refresh(services_edited_record)

        services_edited_record = (
            services_edited_record.to_dict()
            if hasattr(services_edited_record, "to_dict")
            else vars(services_edited_record)
        )
    res = {
        "services_edited_record": services_edited_record,
    }
    return res


async def delete_services_service_id(db: Session, service_id: int):

    query = db.query(models.Services)
    query = query.filter(and_(models.Services.service_id == service_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        services_deleted = record_to_delete.to_dict()
    else:
        services_deleted = record_to_delete
    res = {
        "services_deleted": services_deleted,
    }
    return res


async def get_appointments(db: Session):

    query = db.query(models.Appointments)

    appointments_all = query.all()
    appointments_all = (
        [new_data.to_dict() for new_data in appointments_all]
        if appointments_all
        else appointments_all
    )
    res = {
        "appointments_all": appointments_all,
    }
    return res


async def get_appointments_appointment_id(db: Session, appointment_id: int):

    query = db.query(models.Appointments)
    query = query.filter(and_(models.Appointments.appointment_id == appointment_id))

    appointments_one = query.first()

    appointments_one = (
        (
            appointments_one.to_dict()
            if hasattr(appointments_one, "to_dict")
            else vars(appointments_one)
        )
        if appointments_one
        else appointments_one
    )

    res = {
        "appointments_one": appointments_one,
    }
    return res


async def post_appointments(
    db: Session,
    appointment_id: int,
    customer_id: int,
    provider_id: int,
    service_id: int,
    appointment_datetime: str,
):

    record_to_be_added = {
        "service_id": service_id,
        "customer_id": customer_id,
        "provider_id": provider_id,
        "appointment_id": appointment_id,
        "appointment_datetime": appointment_datetime,
    }
    new_appointments = models.Appointments(**record_to_be_added)
    db.add(new_appointments)
    db.commit()
    db.refresh(new_appointments)
    appointments_inserted_record = new_appointments.to_dict()

    res = {
        "appointments_inserted_record": appointments_inserted_record,
    }
    return res


async def put_appointments_appointment_id(
    db: Session,
    appointment_id: int,
    customer_id: int,
    provider_id: int,
    service_id: int,
    appointment_datetime: str,
):

    query = db.query(models.Appointments)
    query = query.filter(and_(models.Appointments.appointment_id == appointment_id))
    appointments_edited_record = query.first()

    if appointments_edited_record:
        for key, value in {
            "service_id": service_id,
            "customer_id": customer_id,
            "provider_id": provider_id,
            "appointment_id": appointment_id,
            "appointment_datetime": appointment_datetime,
        }.items():
            setattr(appointments_edited_record, key, value)

        db.commit()
        db.refresh(appointments_edited_record)

        appointments_edited_record = (
            appointments_edited_record.to_dict()
            if hasattr(appointments_edited_record, "to_dict")
            else vars(appointments_edited_record)
        )
    res = {
        "appointments_edited_record": appointments_edited_record,
    }
    return res


async def delete_appointments_appointment_id(db: Session, appointment_id: int):

    query = db.query(models.Appointments)
    query = query.filter(and_(models.Appointments.appointment_id == appointment_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        appointments_deleted = record_to_delete.to_dict()
    else:
        appointments_deleted = record_to_delete
    res = {
        "appointments_deleted": appointments_deleted,
    }
    return res


async def get_schedules(db: Session):

    query = db.query(models.Schedules)

    schedules_all = query.all()
    schedules_all = (
        [new_data.to_dict() for new_data in schedules_all]
        if schedules_all
        else schedules_all
    )
    res = {
        "schedules_all": schedules_all,
    }
    return res


async def get_schedules_schedule_id(db: Session, schedule_id: int):

    query = db.query(models.Schedules)
    query = query.filter(and_(models.Schedules.schedule_id == schedule_id))

    schedules_one = query.first()

    schedules_one = (
        (
            schedules_one.to_dict()
            if hasattr(schedules_one, "to_dict")
            else vars(schedules_one)
        )
        if schedules_one
        else schedules_one
    )

    res = {
        "schedules_one": schedules_one,
    }
    return res


async def post_schedules(
    db: Session,
    schedule_id: int,
    provider_id: int,
    start_time: str,
    end_time: str,
    is_booked: int,
):

    record_to_be_added = {
        "end_time": end_time,
        "is_booked": is_booked,
        "start_time": start_time,
        "provider_id": provider_id,
        "schedule_id": schedule_id,
    }
    new_schedules = models.Schedules(**record_to_be_added)
    db.add(new_schedules)
    db.commit()
    db.refresh(new_schedules)
    schedules_inserted_record = new_schedules.to_dict()

    res = {
        "schedules_inserted_record": schedules_inserted_record,
    }
    return res


async def put_schedules_schedule_id(
    db: Session,
    schedule_id: int,
    provider_id: int,
    start_time: str,
    end_time: str,
    is_booked: int,
):

    query = db.query(models.Schedules)
    query = query.filter(and_(models.Schedules.schedule_id == schedule_id))
    schedules_edited_record = query.first()

    if schedules_edited_record:
        for key, value in {
            "end_time": end_time,
            "is_booked": is_booked,
            "start_time": start_time,
            "provider_id": provider_id,
            "schedule_id": schedule_id,
        }.items():
            setattr(schedules_edited_record, key, value)

        db.commit()
        db.refresh(schedules_edited_record)

        schedules_edited_record = (
            schedules_edited_record.to_dict()
            if hasattr(schedules_edited_record, "to_dict")
            else vars(schedules_edited_record)
        )
    res = {
        "schedules_edited_record": schedules_edited_record,
    }
    return res


async def delete_schedules_schedule_id(db: Session, schedule_id: int):

    query = db.query(models.Schedules)
    query = query.filter(and_(models.Schedules.schedule_id == schedule_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        schedules_deleted = record_to_delete.to_dict()
    else:
        schedules_deleted = record_to_delete
    res = {
        "schedules_deleted": schedules_deleted,
    }
    return res


async def post_login(db: Session, email: str, password: str):

    query = db.query(models.Customers)
    query = query.filter(
        and_(models.Customers.email == email, models.Customers.password == password)
    )

    customer_login = query.first()

    customer_login = (
        (
            customer_login.to_dict()
            if hasattr(customer_login, "to_dict")
            else vars(customer_login)
        )
        if customer_login
        else customer_login
    )

    res = {
        "customer": customer_login,
    }
    return res


async def post_customers(
    db: Session,
    customer_id: int,
    name: str,
    contact_details: str,
    email: str,
    password: str,
):

    record_to_be_added = {
        "name": name,
        "email": email,
        "password": password,
        "customer_id": customer_id,
        "contact_details": contact_details,
    }
    new_customers = models.Customers(**record_to_be_added)
    db.add(new_customers)
    db.commit()
    db.refresh(new_customers)
    customers_inserted_record = new_customers.to_dict()

    res = {
        "customers_inserted_record": customers_inserted_record,
    }
    return res

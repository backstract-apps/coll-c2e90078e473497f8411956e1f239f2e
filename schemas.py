from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Customers(BaseModel):
    customer_id: Any
    name: str
    contact_details: str
    email: str
    password: str


class ReadCustomers(BaseModel):
    customer_id: Any
    name: str
    contact_details: str
    email: str
    password: str
    class Config:
        from_attributes = True


class ServiceProviders(BaseModel):
    provider_id: Any
    name: str
    details: str


class ReadServiceProviders(BaseModel):
    provider_id: Any
    name: str
    details: str
    class Config:
        from_attributes = True


class Services(BaseModel):
    service_id: Any
    name: str
    duration_minutes: int


class ReadServices(BaseModel):
    service_id: Any
    name: str
    duration_minutes: int
    class Config:
        from_attributes = True


class Appointments(BaseModel):
    appointment_id: Any
    customer_id: int
    provider_id: int
    service_id: int
    appointment_datetime: Any


class ReadAppointments(BaseModel):
    appointment_id: Any
    customer_id: int
    provider_id: int
    service_id: int
    appointment_datetime: Any
    class Config:
        from_attributes = True


class Schedules(BaseModel):
    schedule_id: Any
    provider_id: int
    start_time: Any
    end_time: Any
    is_booked: int


class ReadSchedules(BaseModel):
    schedule_id: Any
    provider_id: int
    start_time: Any
    end_time: Any
    is_booked: int
    class Config:
        from_attributes = True



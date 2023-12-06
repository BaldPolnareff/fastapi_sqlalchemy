from pytest import fixture
import pytest 

from sql_app.crud import (
    get_user, 
    get_user_by_email, 
    get_users, 
    create_users, 
    get_items, 
    create_user_item
)

from sql_app import models, schemas 

from sql_app.database import engine, SessionLocal
from sqlalchemy.orm import Session



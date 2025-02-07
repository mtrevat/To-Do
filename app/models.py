import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.orm import Mapped, mapped_column
from wtforms import TextAreaField
from wtforms.validators import Length
from app import db

class Task(db.Model):
    pass
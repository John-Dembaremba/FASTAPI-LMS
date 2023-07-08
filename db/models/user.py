import enum
from sqlalchemy import Text, Integer, Column, VARCHAR, Boolean, ForeignKey
from sqlalchemy_utils import EmailType, ChoiceType
from sqlalchemy.orm import relationship
from ..db_setup import Base
from .mixins import TimeStamp
 
class Role(enum.Enum):
    teacher = 1
    student = 2
    
class User(TimeStamp, Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(EmailType)
    roles = Column(ChoiceType(Role))
    is_active = Column(Boolean, default=False)
    profile = relationship("Profile", back_populates="owner", uselist=False)

class Profile(TimeStamp, Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(VARCHAR(100), nullable=False)
    last_name = Column(VARCHAR(100), nullable=False)
    bio = Column(Text, nullable=True, default=None)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    owner = relationship("User", back_populates="profile") 
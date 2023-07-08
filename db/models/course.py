import enum
from sqlalchemy import Text, Integer, Column, VARCHAR, Boolean, ForeignKey
from sqlalchemy_utils import ChoiceType, URLType
from sqlalchemy.orm import relationship

from ..db_setup import Base
from .mixins import TimeStamp
from .user import User


class ContentType(enum.Enum):
    lesson = 1
    quiz = 2
    assignment = 3
    
class Course(TimeStamp, Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(100), nullable=False)
    description = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    created_by = relationship(User)
    sections = relationship("Section", back_populates="course", uselist=False)
    student_course = relationship("StudentCourse", back_populates="course")

class Section(TimeStamp, Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(200), nullable=False)
    description = Column(Text, nullable=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)

    course = relationship("Course", back_populates="sections")
    content_blocks = relationship("ContentBlock", back_populates="section")


class ContentBlock(TimeStamp, Base):
    __tablename__ = "content_blocks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(200), nullable=False)
    description = Column(Text, nullable=True)
    type = Column(ChoiceType(ContentType))
    url = Column(URLType, nullable=True)
    content = Column(Text, nullable=True)
    section_id = Column(Integer, ForeignKey("sections.id"), nullable=False)

    section = relationship("Section", back_populates="content_blocks")
    completed_content_blocks = relationship("CompletedContentBlock", back_populates="content_block")


class StudentCourse(TimeStamp, Base):
    """
    Students can be assigned to courses.
    """
    __tablename__ = "student_courses"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    completed = Column(Boolean, default=False)

    student = relationship(User, back_populates="student_courses")
    course = relationship("Course", back_populates="student_courses")


class CompletedContentBlock(TimeStamp, Base):
    """
    This shows when a student has completed a content block.
    """
    __tablename__ = "completed_content_blocks"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    content_block_id = Column(Integer, ForeignKey("content_blocks.id"), nullable=False)
    url = Column(URLType, nullable=True)
    feedback = Column(Text, nullable=True)
    grade = Column(Integer, default=0)

    student = relationship(User, back_populates="student_content_blocks")
    content_block = relationship(ContentBlock, back_populates="completed_content_blocks")
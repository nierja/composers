from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# ABC for entities
Base = declarative_base()

### My DB entities: ###
class Composer(Base):
    __tablename__ = 'composers'

    id_composer = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    nationality = Column(String, nullable=False)
    style = Column(String)

    works = relationship("Work", back_populates="composer")

class Work(Base):
    __tablename__ = 'works'

    id_work = Column(Integer, primary_key=True)
    id_composer = Column(Integer, ForeignKey('composers.id_composer'), nullable=False)
    title = Column(String, nullable=False)
    publication_year = Column(String)
    feature = Column(String)

    composer = relationship("Composer", back_populates="works")
    editions = relationship("WorksEditions", back_populates="work")

class Publisher(Base):
    __tablename__ = 'publishers'

    id_publisher = Column(Integer, primary_key=True)
    publishing_house = Column(String, nullable=False)
    annual_revenue = Column(String)

    editions = relationship("Edition", back_populates="publisher")

class Edition(Base):
    __tablename__ = 'editions'

    id_edition = Column(Integer, primary_key=True)
    id_publisher = Column(Integer, ForeignKey('publishers.id_publisher'), nullable=False)
    name = Column(String, nullable=False)
    chief_editor = Column(String, nullable=False)

    publisher = relationship("Publisher", back_populates="editions")
    works = relationship("WorksEditions", back_populates="edition")

class WorksEditions(Base):
    __tablename__ = 'works_editions'

    id_work = Column(Integer, ForeignKey('works.id_work'), primary_key=True)
    id_edition = Column(Integer, ForeignKey('editions.id_edition'), primary_key=True)

    work = relationship("Work", back_populates="editions")
    edition = relationship("Edition", back_populates="works")

print("Database defined!")

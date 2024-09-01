from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Base for models
Base = declarative_base()

# Define the models

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

# Create the SQLite engine
engine = create_engine('sqlite:///classical_music.db')

# Create all tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Example data population
def populate_db():
    composer_1 = Composer(name="Beethoven", nationality="German", style="Classical")
    composer_2 = Composer(name="Bach", nationality="German", style="Baroque")

    work_1 = Work(title="Symphony No. 9", publication_year="1824", composer=composer_1)
    work_2 = Work(title="Mass in B minor", publication_year="1749", composer=composer_2)

    publisher_1 = Publisher(publishing_house="Schott", annual_revenue="500000")
    publisher_2 = Publisher(publishing_house="Breitkopf & Härtel", annual_revenue="700000")

    edition_1 = Edition(name="First Edition", chief_editor="Editor 1", publisher=publisher_1)
    edition_2 = Edition(name="Second Edition", chief_editor="Editor 2", publisher=publisher_2)

    works_editions_1 = WorksEditions(work=work_1, edition=edition_1)
    works_editions_2 = WorksEditions(work=work_2, edition=edition_2)

    session.add_all([composer_1, composer_2, work_1, work_2, publisher_1, publisher_2, edition_1, edition_2, works_editions_1, works_editions_2])
    session.commit()

# Populate the database
populate_db()

print("Database created and populated with example data.")

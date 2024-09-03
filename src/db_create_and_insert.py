import os
from db_entities import Base, Composer, Work, Publisher, Edition, WorksEditions
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///classical_music.db') # global SQLite engine
Session = sessionmaker(bind=engine)                    # global DB session
Base.metadata.create_all(engine)
print("Database created!")

def populate_db_from_files():
    session = Session()

    # handle data paths
    data_dir = 'data'
    composers_file = os.path.join(data_dir, 'composers.data')
    editions_file = os.path.join(data_dir, 'editions.data')
    publishers_file = os.path.join(data_dir, 'publishers.data')
    works_file = os.path.join(data_dir, 'works.data')
    works_editions_file = os.path.join(data_dir, 'worksEditions.data')

    # composers
    with open(composers_file, 'r') as file:
        for line in file:
            parts = line.strip().split(';')
            if len(parts) >= 4:
                name = parts[1].strip().strip("'")
                nationality = parts[2].strip().strip("'")
                style = parts[3].strip().strip("'")
                composer = Composer(name=name, nationality=nationality, style=style)
                session.add(composer)

    # publishers
    with open(publishers_file, 'r') as file:
        for line in file:
            parts = line.strip().split(';')
            if len(parts) >= 3:
                publishing_house = parts[1].strip().strip("'")
                annual_revenue = parts[2].strip().strip("'")
                publisher = Publisher(publishing_house=publishing_house, annual_revenue=annual_revenue)
                session.add(publisher)

    # editions
    with open(editions_file, 'r') as file:
        for line in file:
            parts = line.strip().split(';')
            if len(parts) >= 4:
                id_publisher = int(parts[1].strip())
                name = parts[2].strip().strip("'")
                chief_editor = parts[3].strip().strip("'")
                edition = Edition(id_publisher=id_publisher, name=name, chief_editor=chief_editor)
                session.add(edition)

    # works
    with open(works_file, 'r') as file:
        composer_map = {composer.name: composer.id_composer for composer in session.query(Composer).all()}
        for line in file:
            parts = line.strip().split(';')
            if len(parts) >= 3:
                composer_name = parts[1].strip()
                title = parts[2].strip().strip("'")
                publication_year = parts[3].strip().strip("'") if len(parts) > 3 else None
                id_composer = composer_map.get(composer_name)
                if id_composer:
                    work = Work(id_composer=id_composer, title=title, publication_year=publication_year)
                    session.add(work)

    # works_editions
    with open(works_editions_file, 'r') as file:
        for line in file:
            parts = line.strip().split(';')
            if len(parts) >= 2:
                id_work = int(parts[0].strip())
                id_edition = int(parts[1].strip())
                works_editions = WorksEditions(id_work=id_work, id_edition=id_edition)
                session.add(works_editions)

    session.commit()
    print("Database inserted into!")

def main():
    populate_db_from_files()

if __name__ == '__main__':
    main()
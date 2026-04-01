import pandas as pd
from app.core.database import SessionLocal, init_db
from app.modules.catalog.repositories.models import StudioModel, ProducerModel, MovieModel, AwardModel


init_db()

def load_csv(file_path:str) -> pd.DataFrame:
    return pd.read_csv(file_path, sep=";")

def validate_row(row) -> bool:
    if pd.isna(row['year']) or pd.isna(row['title']):
        return False
    return True

def normalize_list(value: str) -> list:
    if not value:
        return []
    value = value.replace(' and', ',')
    return [v.strip() for v in value.split(',') if v.strip()]

def main():
    session = SessionLocal()

    try:
        df = load_csv("../../../dump-database.csv")

        studios_cache = {}
        studios_to_insert = []
        producers_cache = {}
        producers_to_insert = []
        movies_to_insert = []
        awards_to_insert = []

        existing_studio = {s.name: s for s in session.query(StudioModel).all()}
        existing_producer = {p.name: p for p in session.query(ProducerModel).all()}

        for _, row in df.iterrows():
            if not validate_row(row):
                continue

            year = row['year']
            title = row['title']
            winner = bool(row['winner'])

            # ---- studios ----
            studio_names = normalize_list(row['studios'])
            studio_objs = []

            for name in studio_names:
                if name not in studios_cache:
                    if name not in existing_studio:
                        studio = StudioModel(name=name)
                        studios_cache[name] = studio
                        studios_to_insert.append(studio)
                    else:
                        studios_cache[name] = existing_studio[name]
                studio_objs.append(studios_cache[name])

            # ----  producers ----
            producers_names = normalize_list(row['producers'])
            producer_objs = []

            for name in producers_names:
                if name not in producers_cache:
                    if name not in existing_producer:
                        producer = ProducerModel(name=name)
                        producers_cache[name] = producer
                        producers_to_insert.append(producer)
                    else:
                        producers_cache[name] = existing_producer[name]
                producer_objs.append(producers_cache[name])

            # ---- movie ----
            if studio_objs and producer_objs:
                movie = MovieModel(
                    title=title,
                    release_year=year,
                    studios=studio_objs,
                    producers=producer_objs
                )

                movies_to_insert.append(movie)

                # award
                if winner:
                    award = AwardModel(
                        movie=movie,
                        year=year,
                        winner=winner # True
                    )
                    awards_to_insert.append(award)

        session.bulk_save_objects(producers_to_insert)
        session.bulk_save_objects(studios_to_insert)

        session.add_all(movies_to_insert)
        session.add_all(awards_to_insert)

        session.flush()
        session.commit()

        print("Importation completed!")

    except Exception as e:
        session.rollback()
        print("Exception occurred: ", e)
    finally:
        session.close()


if __name__ == '__main__':
    main()
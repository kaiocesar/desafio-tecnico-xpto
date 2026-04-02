from pprint import pprint

from sqlalchemy import func, select, desc, asc

from app.modules.catalog.repositories.interfaces.award_interface import IAwardInterface
from app.modules.catalog.repositories.models import AwardModel, ProducerModel, MovieModel, MovieProducerModel


class AwardService:
    def __init__(self, repository: IAwardInterface):
        self.repository = repository

    def get_award_list(self):
        return self.repository.find_all()

    def get_award_intervals(self):
        previous_year = func.lag(AwardModel.year).over(
            partition_by=ProducerModel.name,
            order_by=AwardModel.year
        )
        intervals_select = (
            select(
                ProducerModel.name.label("name"),
                MovieModel.title.label("title"),
                AwardModel.year.label("year"),
                previous_year.label("previous_win_year"),
                (AwardModel.year - previous_year).label("years_between_wins"),
            )
            .select_from(AwardModel)
            .join(MovieProducerModel, AwardModel.movie_id == MovieProducerModel.movie_id, isouter=True)
            .join(ProducerModel, MovieProducerModel.producer_id == ProducerModel.id, isouter=True)
            .join(MovieModel, MovieModel.id == AwardModel.movie_id, isouter=True)
            .where(AwardModel.winner.is_(True))
            .cte("intervals")
        )

        ranked_cte = (
            select(
                intervals_select,
                func.rank().over(
                    order_by=desc(intervals_select.c.years_between_wins),
                ).label("r_max"),
                func.rank().over(
                    order_by=asc(intervals_select.c.years_between_wins)
                ).label("r_min"),
            )
            .where(intervals_select.c.years_between_wins.isnot(None))
            .cte("ranked")
        )

        query_max = select(ranked_cte).where(
            (ranked_cte.c.r_max <= 2)
        )
        query_min = select(ranked_cte).where(
            (ranked_cte.c.r_min <= 2)
        )

        return {
            "max": self.repository.db.execute(query_max).mappings().all(),
            "min": self.repository.db.execute(query_min).mappings().all(),
        }
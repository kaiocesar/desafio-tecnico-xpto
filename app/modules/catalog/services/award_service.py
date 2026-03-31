from app.modules.catalog.repositories.interfaces.award_interface import IAwardInterface


class AwardService:
    def __init__(self, repository: IAwardInterface):
        self.repository = repository

    def get_award_list(self):
        return self.repository.find_all()

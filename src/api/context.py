from src.api.app.app_factory import ApplicationFactory
from src.api.service.recommendation_service import RecommendationService
from src.repository import DatabaseClient
from src.util.config import Config

cfg = Config(f'./config.yaml')

app = ApplicationFactory.create(cfg['api.uri'])

client = DatabaseClient(
    cfg['database.url'],
    cfg['database.username'],
    cfg['database.password']
)

recommendation_service = RecommendationService(client, cfg)

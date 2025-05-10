from app.api.types import Town
from app.models import Town as TownModel


def build_town(town: TownModel) -> Town:
    """Convert town from model to type."""
    return Town(id=town.id, name=town.name)

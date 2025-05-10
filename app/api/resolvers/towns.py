from app.api.builders import build_town
from app.api.types import Town
from app.validators import validate_args
from app.controllers import get_town, get_towns


async def get_town_resolver(town_id: str) -> Town | None:
    if errors := validate_args({"town_id": town_id}):
        raise Exception(errors)
    if town := await get_town(town_id):
        return build_town(town)


async def get_towns_resolver() -> list[Town]:
    towns = []
    for town in await get_towns():
        towns.append(build_town(town))
    return towns

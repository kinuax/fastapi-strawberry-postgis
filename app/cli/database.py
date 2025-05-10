from asyncio import run
from datetime import datetime
from uuid import uuid4

import typer

from app.controllers import create_tables, load_tables, truncate_tables, drop_tables
from app.models import Town, Venue, Event
from app.utils import get_point_from_lat_lon


app = typer.Typer(context_settings={"help_option_names": ["-h", "--help"]})
tables = ["events", "venues", "towns"]


@app.command()
def create() -> None:
    run(create_tables())
    print("database created")


@app.command()
def load() -> None:
    objs = []
    barcelona = Town(name="Barcelona")
    barcelona.id = uuid4()
    objs.append(barcelona)
    espigo = Venue(
        town_id=barcelona.id,
        name="Espigó del Bogatell",
        point=get_point_from_lat_lon(41.390609378811966, 2.2057509477779105),
        address="Espigó del Bogatell - 08005"
    )
    espigo.id = uuid4()
    big = Venue(
        town_id=barcelona.id,
        name="BIG: Barcelona Improv Group",
        point=get_point_from_lat_lon(41.38162832110099, 2.1564985250274495),
        address="Carrer del Comte Borrell, 143 - 08015"
    )
    big.id = uuid4()
    eca = Venue(
        town_id=barcelona.id,
        name="Sala ECA",
        point=get_point_from_lat_lon(41.3969821983816, 2.182881893629522),
        address="Carrer d'Ausiàs March, 143 - 08013"
    )
    eca.id = uuid4()
    objs.extend([espigo, big, eca])
    espigo_event = Event(
        venue_id=espigo.id,
        name="BEACH Flow Yoga",
        start=datetime(2025, 7, 12, 10, 0),
        end=datetime(2025, 7, 12, 11, 15),
        desc="Flow Yoga Class ON THE BEACH.",
    )
    espigo_event.id = uuid4()
    big_event = Event(
        venue_id=big.id,
        name="Spill the Tea: Improv Comedy Show",
        start=datetime(2025, 7, 12, 20, 0),
        end=datetime(2025, 7, 12, 21, 30),
        desc="Welcome to the long form improv comedy show where YOU Spill the Tea and WE mop it all up to create "
             "improvised comedy and theatre!",
    )
    big_event.id = uuid4()
    eca_event = Event(
        venue_id=eca.id,
        name="Comedy Selection",
        start=datetime(2025, 7, 12, 22, 0),
        end=datetime(2025, 7, 12, 23, 15),
        desc="The best selection of Barcelona Comedy Club.",
    )
    eca_event.id = uuid4()
    objs.extend([espigo_event, big_event, eca_event])
    seoul = Town(name="Seoul")
    seoul.id = uuid4()
    objs.append(seoul)
    gate = Venue(
        town_id=seoul.id,
        name="Gwanghwamun Gate",
        point=get_point_from_lat_lon(37.5758882709091, 126.97682213941088),
        address="12 Hyoja-ro - Jongno-gu"
    )
    gate.id = uuid4()
    yna = Venue(
        town_id=seoul.id,
        name="YNA Lounge",
        point=get_point_from_lat_lon(37.55044612784208, 126.92284959577398),
        address="65 Wausan-ro - Mapo-gu"
    )
    yna.id = uuid4()
    objs.extend([gate, yna])
    gate_event = Event(
        venue_id=gate.id,
        name="Founders Running Club",
        start=datetime(2025, 7, 12, 8, 0),
        end=datetime(2025, 7, 12, 10, 0),
        desc="FRC brings founders, investors, tech, creative people and startup enthusiasts together "
             "for weekly easy runs and networking.",
    )
    gate_event.id = uuid4()
    yna_event = Event(
        venue_id=yna.id,
        name="Internationl Language Exchange Party",
        start=datetime(2025, 7, 12, 19, 0),
        end=datetime(2025, 7, 12, 21, 0),
        desc="Our YNA Language Exchange group is a conversational platform where people from around the world "
             "can exchange languages and cultures.",
    )
    yna_event.id = uuid4()
    objs.extend([gate_event, yna_event])
    run(load_tables(objs))
    print("database loaded")


@app.command()
def truncate() -> None:
    run(truncate_tables(tables))
    print("database truncated")


@app.command()
def drop() -> None:
    run(drop_tables(tables))
    print("database dropped")


if __name__ == "__main__":
    app()

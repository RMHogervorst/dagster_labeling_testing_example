from warnings import filterwarnings

from dagster import Definitions, load_assets_from_modules, ExperimentalWarning

# stop warnings for  `Parameter `owners` of function `asset` is experimental.`
filterwarnings(
    "ignore",
    category=ExperimentalWarning,
    message="""Parameter `owners` of function `asset` is experimental.""",
)

from project import assets  # noqa: TID252,E402
from project import ds_team  # noqa E402

all_assets = load_assets_from_modules([assets, ds_team])

sensors = [ds_team.hot_new_model_prod_sensor]

external_assets = [ds_team.hot_new_item_model_prod]

defs = Definitions(
    assets=[*all_assets, *external_assets],
    sensors=sensors,
)

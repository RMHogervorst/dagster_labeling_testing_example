from dagster import asset, Out

@asset(
    metadata={
        "dataset":"clicks",
        "dagster/uri":"s3://my_bucket/my_object",
        "dagster/table_name":"src.clicks_hourly"
        },
    tags={"domain": "marketing", "pii": "true"}, 
    owners=["team:Data-Engineering"], 
    kinds={"python","s3", "iceberg"}
    )
def read_clicks_data():
    """This asset has metadata.

    A rich description.
    Owners, tags, kinds-tags, and metadata (normal and special dagster metadata)
    """
    n=0
    # some code that creates a dataset.
    dataset = {}
    # some code that counts the number of rows.
    return Out(dataset,metadata={"dagster/row_count":n})



# an asset with group
@asset(
    metadata={
        "dataset":"clicks",
        "dagster/table_name":"src.clicks_hourly_region"
        },
    tags={"domain": "marketing", "pii": "false"}, 
    owners=["team:Data-Engineering"], 
    kinds={"sql","iceberg", "bronze"},
    deps=["read_clicks_data"]
)
def split_clicks_data():
    """Split data into regions."""
    # something
    return

@asset(
    metadata={
        "dataset":"clicks",
        "priority":"medium"
        },
    tags={"domain": "marketing", "pii": "false"}, 
    owners=["team:Marketing"], 
    kinds={"dashboard", "gold"},
    deps=["split_clicks_data"],
    group_name="Marketing"
)
def dashboard_clicks_north():
    """Marketing dashboard for region North."""
    # all the code to create the dashboard
    pass

@asset(
    metadata={
        "dataset":"clicks",
        "priority":"medium"
        },
    tags={"domain": "marketing", "pii": "false"}, 
    owners=["team:Marketing"], 
    kinds={"dashboard", "gold"},
    deps=["split_clicks_data"],
    group_name="Marketing"
)
def dashboard_clicks_south():
    """Marketing dashboard for region South."""
    # all the code to create the dashboard
    pass


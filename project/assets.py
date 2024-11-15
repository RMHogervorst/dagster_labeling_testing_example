from dagster import asset, Out


@asset(
    metadata={
        "dataset": "clicks",
        "dagster/uri": "s3://my_bucket/my_object",
        "dagster/table_name": "src.clicks_hourly",
    },
    tags={"domain": "marketing", "pii": "true"},
    owners=["team:Data-Engineering"],
    kinds={"python", "s3", "iceberg"},
)
def read_clicks_data():
    """This asset has metadata.

    A rich description.
    It has Owners, tags, kinds-tags, and metadata
    (normal and special dagster metadata)

    I imagine this asset reads from S3 and delivers a dataset into iceberg.
    This process is owned by the data engineering team.
    It also has dynamic metadata (the number of rows) but
    you would only see that on materialization.
    """
    n = 0
    # some code that creates a dataset.
    dataset = {}
    # some code that counts the number of rows.
    return Out(dataset, metadata={"dagster/row_count": n})


@asset(
    metadata={"dataset": "clicks", "dagster/table_name": "src.clicks_hourly_region"},
    tags={"domain": "marketing", "pii": "false"},
    owners=["team:Data-Engineering"],
    kinds={"sql", "iceberg", "bronze"},
    deps=["read_clicks_data"],
)
def split_clicks_data():
    """Split data into regions.

    This process is also owned by Data Engineering and we use
    a medallion architecture here, marking this dataset as 'bronze'.
    This process runs on sql."""
    # something
    return


# TODO add staging layer


@asset(
    metadata={"dataset": "clicks", "priority": "high"},
    tags={"domain": "marketing", "pii": "false"},
    owners=["team:Data-Engineering"],
    kinds={"iceberg", "silver"},
    deps=["split_clicks_data"],
)
def cleaned_clicks_data():
    pass


@asset(
    metadata={"dataset": "clicks", "priority": "medium"},
    tags={"domain": "marketing", "pii": "false"},
    owners=["team:Marketing"],
    kinds={"dashboard", "gold"},
    deps=["cleaned_clicks_data"],
    group_name="Marketing",
)
def dashboard_clicks_north():
    """Marketing dashboard for region North.

    There should be at least a staging (silver) layer
    in between the bronze and this 'gold' dataset, but
    I'm just creating this for demonstration purposes.
    """
    # all the code to create the dashboard
    pass


@asset(
    metadata={"dataset": "clicks", "priority": "low"},
    tags={"domain": "marketing", "pii": "false"},
    owners=["team:Marketing"],
    kinds={"dashboard", "gold"},
    deps=["cleaned_clicks_data"],
    group_name="Marketing",
)
def dashboard_clicks_south():
    """Marketing dashboard for region South.

    This is also a dashboard, identical to the
    North dashboard dataset, but it has
    priority:low. This metadata doesn't do
    anything in dagster, but it can help
    in prioritizing your work."""
    # all the code to create the dashboard
    pass

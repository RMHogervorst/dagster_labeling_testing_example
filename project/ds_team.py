from dagster import asset, AssetSpec, AssetKey, sensor, SensorResult, AssetObservation

GROUP = "datascience"


@asset(
    metadata={"priority": "low", "ds/type": "classification", "Status": "PoC"},
    tags={"domain": "marketing", "pii": "false"},
    owners=["team:Data-Science"],
    kinds={"s3", "python", "scikitlearn"},
    deps=["cleaned_clicks_data"],
    group_name=GROUP,
    op_tags={
        "dagster/max_retries": "1",
        "dagster-k8s/config": {
            "container_config": {
                "requests": {"cpu": "1000m", "memory": "12Gi"},
                "limits": {"cpu": "1200m", "memory": "12Gi"},
            }
        },
    },
)
def train_classifier_hot_new_item():
    """Train a classifier to detect hot new items and dump model in s3."""
    pass


hot_new_item_model_prod = AssetSpec(
    key=AssetKey("hot_new_item_model"),
    group_name=GROUP,
    tags={"domain": "marketing"},
    description="""Current hot new item model. 
    
    This is an external asset, we promote our models through MLFlow.
    But we could make the sensor not only emit asset observations
    but even asset materializations when the model version changes.
    This would allow us to trigger a pipeline downstream""",
    metadata={"ds/type": "classification", "Status": "PoC"},
    kinds={"scikitlearn", "mlflow"},
)


@sensor(minimum_interval_seconds=60)
def hot_new_model_prod_sensor():
    # observes the model and returns metrics
    # asset observations
    metadata = {"predictions/last_60s": 10, "model_version": "23dj84c"}
    return SensorResult(
        asset_events=[
            AssetObservation(asset_key="hot_new_item_model", metadata=metadata)
        ]
    )

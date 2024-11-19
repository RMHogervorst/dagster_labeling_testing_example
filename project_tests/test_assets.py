import pytest
from dagster import AssetSpec, AssetsDefinition

from project.definitions import all_assets


@pytest.mark.parametrize("asset", all_assets)
def test_assets_style(asset):
    if isinstance(asset, AssetSpec):
        spec = asset
    else:
        assert isinstance(asset, AssetsDefinition), "not an asset"
        spec = asset.get_asset_spec()
    # then we can test for all sorts of things
    assert spec.description is not None, f"{spec.key.to_string()} needs a description"

    if spec.metadata.get("Status"):
        assert spec.metadata.get("Status") in ["PoC", "Prototype", "Product"]
        # status one of group
        # you can set some rules
        if spec.metadata.get("Status") == "Product":
            asset_spec_tester_prototype(spec)
            asset_spec_tester_product(spec)
        if spec.metadata.get("Status") == "Prototype":
            asset_spec_tester_prototype(spec)
    ## dashboard datasets need a url.
    if "dashboard" in spec.kinds:
        assert (
            spec.metadata.get("dashboard_url") is not None
        ), f"{spec.key.to_string()} has kind dashboard, and therefore needs a dashboard_url."
    # spec.kinds
    # spec.metadata
    # spec.owners
    # spec.tags


def asset_spec_tester_product(spec):
    """test specific things for assets in product stage."""
    assert spec.metadata.get("docs"), f"{spec.key.to_string()} needs a docs link"


def asset_spec_tester_prototype(spec):
    """Tests for assets in prototype stage."""
    assert spec.owners is not None, f"{spec.key.to_string()} needs owners"

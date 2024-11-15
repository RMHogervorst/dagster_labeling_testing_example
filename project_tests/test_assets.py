import pytest
from dagster import AssetSpec, AssetsDefinition

from project.definitions import all_assets

@pytest.mark.parametrize("asset",all_assets)
def test_assets_style(asset):
    if isinstance(asset, AssetSpec):
        spec = asset
    else:
        assert isinstance(asset, AssetsDefinition), "not an asset"
        spec = asset.get_asset_spec()
    # then we can test for all sorts of things
    assert spec.description is not None, f"{spec.key.to_string()} needs a description"
    
    ## if spec.metadata.get("Status"):
        # status one of group
        # you can set some rules
    #spec.kinds
    # spec.metadata
    # spec.owners
    # spec.tags

def asset_spec_tester_product(spec):
    # test specific things for product stage 
    pass
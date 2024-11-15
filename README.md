# Labeling and testing assets with Dagster

In this project I create an example set of assets (with no real content).
All of the assets have rich metadata to showcase all of the ways in which you can differentiate your assets in dagster.

Finally I show some ways of testing for these style rules.

## installation
This project uses poetry.

`poetry install` to install the program (it will create a virtualenv)
use `poetry run dagster dev` to see the user interface.


## An example project with rich metadata.
This is the example project, inspirationately called 'project' with the exceptionally original name 'labeling example project'.

In this project a data engineering team pulls marketing data (clicks) from s3 and parks it into iceberg. From there, the data is transformed in several steps until it ends up in datasets
that are used for dashboards and for use in machine learning project.

```
read_clicks_data => split_clicks_data => cleaned_click_data

cleaned_clicks_data => [dashboard_clicks_north, dashboard_clicks_south]

cleaned_clicks_data => train_classifier_hot_new_item
```

Finally there is an external asset that represents the hot_new_item classifier that is currently in production.

### What is visible

Here are the currently visible ways to differentiate assets in this project:

- based on `asset groups`: bundeling assets that belong together
- based on `kind`, a special type of metadata that is represented with an icon: dashboard, silver, gold, sql, iceberg, scikitlearn, python
- based on asset `owners`
- based on `tag`

There is more metadata available:

- All assets have a `description`
- All assets have `metadata`

In the 'global asset lineage' overview you can see all assets and their lineage, and you can also filter on `kind`, `tag`, `owner`, `asset group`.

![global asset overview](img/Screenshot%20from%202024-11-14%2021-11-09.png)

When you click on an asset you can see a details pane with `description` and `metadata` (both static, and dynamic from last runs).


![global overview with detail view of upstream asset.](img/Screenshot%20from%202024-11-14%2021-20-15.png)


![Detail view of one asset downstream](img/Screenshot%20from%202024-11-14%2021-12-48.png)

![detail of one group](img/Screenshot%20from%202024-11-15%2019-24-05.png)

The asset listing has the same filter options ( `kind`, `tag`, `owner`, `asset group`.) but shows the description too.

![asset listing](img/Screenshot%20from%202024-11-15%2019-21-49.png)

![asset listing, filter options](img/Screenshot%20from%202024-11-15%2019-22-09.png)

The asset catalog shows all the details for one asset; `asset group`, `kind`,`tag`, `owner`, `description` and `metadata`.

![](img/Screenshot%20from%202024-11-15%2019-51-04.png)

### Labeling makes your life easier
The tags, metadata, kinds, description etc. make it easy to see what assets are available, who is responsible and what kind of asset something is.

You also know who to contact when something breaks.

### Further reading about tags, kinds and metadata

Some useful links:

- If you want to select a kind-tag that turns into an image here are [all current kind tags](https://sourcegraph.com/github.com/dagster-io/dagster/-/blob/js_modules/dagster-ui/packages/ui-core/src/graph/OpTags.tsx)
- more details about [asset-metadata](https://docs.dagster.io/concepts/metadata-tags/asset-metadata)
- all predefined dagster [standard metadata](https://docs.dagster.io/concepts/metadata-tags/asset-metadata#standard-asset-metadata-entries)


## Testing

In the project_test folder I defined a test that checks all assets for 
a few basics; does it have a description?

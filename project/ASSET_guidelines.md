# Guidelines for assets for org

_This could be your guide, I wrote something similar for my $work._

As our number of assets grow, finding a specific one becomes harder. With more assets, the probability that one fails is larger. But not all assets are important, or urgent. Using consistent tags, kind, and metadata makes the work easier. 

We can filter on `tags`, `kind`, `owner`, ( and `asset_group`, but there can only be one asset group).

Here are some guidelines (SHOULD) and rules (MUST) for assets.

## Metadata

You SHOULD:

- use the metadatavalue `dagster/table_name` when your asset creates a table
- use the metadatavalue `dagster/uri` for s3 bucket folders that you read from.
- use metadatavalue `Status` (PoC/Prototype/Product) to label the status of your asset
- add a `docs` metadatavalue
- use the metadatavalue `dagster/row_count` or `dagster/partition_row_count` to report the number or rows in a materialization.
- emit relevant metadata in the materialization. 

You MUST[^1]:

- have a metadata value `docs` for assets with Status=Product

## Tags

You SHOULD

- label your domain
- label when data contains Personally Identifiable Information (PII)

You MUST[^1]:

- add a specific op_tag to any asset that uses the resource OLTP_db. Use tag=db and value=prod (this allows us to limit the number of simultaneous processes)

## Kinds
You SHOULD

- label the storage layer (iceberg, S3, postgres, etc.)
- label the medallion stage the asset lives in (bronze, silver, gold)
- label dashboards datasets with the dashboard kind


You MUST[^1]:


## Owners
You SHOULD

- have owners on all assets
- have a `team:` as owner


You MUST[^1]:

- have owners on assets of Status: Prototype and higher.


[^1]: we run a testsuite on assets on every MR to comply with these rules. If your asset does not comply it will fail the tests

## asset groups

You SHOULD label your assets with the asset group they are part of. we label all
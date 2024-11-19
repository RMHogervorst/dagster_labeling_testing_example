from dagster import ConfigurableResource

class OLTP_db(ConfigurableResource):
    user: str
    passw: str
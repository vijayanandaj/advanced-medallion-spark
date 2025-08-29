# Secrets & Config (Workspace)

## Event Hubs / Kafka
- Create a secret scope (e.g., `eh-scope`).
- Store the connection string as `eh-conn`.
- Read it in notebooks with:
~~~python
conn = dbutils.secrets.get("eh-scope", "eh-conn")
~~~

## Widgets (catalog/schema/paths)
~~~python
try:
    dbutils.widgets.text("catalog","main")
    dbutils.widgets.text("schema","demo")
    dbutils.widgets.text("base_path","/tmp/adv_medallion")
    CATALOG = dbutils.widgets.get("catalog")
    SCHEMA  = dbutils.widgets.get("schema")
    BASE    = dbutils.widgets.get("base_path")
except Exception:
    CATALOG, SCHEMA, BASE = "main","demo","./_local"
~~~

def get_widgets():
    try:
        dbutils.widgets.text("catalog", "main")
        dbutils.widgets.text("schema", "demo")
        dbutils.widgets.text("base_path", "/tmp/adv_medallion")
        return (dbutils.widgets.get("catalog"),
                dbutils.widgets.get("schema"),
                dbutils.widgets.get("base_path"))
    except Exception:
        return "main", "demo", "./_local"

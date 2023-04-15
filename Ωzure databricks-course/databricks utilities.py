# Databricks notebook source
# MAGIC %fs
# MAGIC ls /databricks-datasets

# COMMAND ----------

dbutils.fs.ls('/databricks-datasets/COVID')

# COMMAND ----------

for files in dbutils.fs.ls('/databricks-datasets/COVID'):
    print(files.name)
#     if files.name.endswith('/'):
#         print(file.name)

# COMMAND ----------

dbutils.fs.help('ls')

# COMMAND ----------



# Databricks notebook source
# import sql 

# COMMAND ----------

for i in range(10):
    print("you got this")

# COMMAND ----------

display(dbutils.fs.ls("./"))

# COMMAND ----------

dbutils.fs.ls("./databricks-datasets")

# COMMAND ----------

display(dbutils.fs.ls("./"))

# COMMAND ----------



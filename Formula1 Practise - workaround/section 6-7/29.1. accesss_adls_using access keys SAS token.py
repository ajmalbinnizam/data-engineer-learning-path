# Databricks notebook source
# MAGIC %md
# MAGIC ### Access Azure data lake using access keys
# MAGIC 1. set the spark config fs.azure.account.key
# MAGIC 1. list files form demo container
# MAGIC 1. read data from circuits.csv file

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.formula369.dfs.core.windows.net",
    '6cS9vDjlv9zCC50VDuRlf9dRwhfFpFEZlKxidudet7Tzsbq6NeSvvADuT0chLj7zjuMOof4R2cco+AStxgO5O'
)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula369.dfs.core.windows.net"))

# COMMAND ----------

circuit = spark.read.csv("abfss://demo@formula369.dfs.core.windows.net/circuits (1).csv")
display(circuit)

# COMMAND ----------

# MAGIC %md
# MAGIC ### [Access Azure data lake using SAS Token 🔗](https://learn.microsoft.com/en-us/azure/databricks/storage/azure-storage#access-azure-data-lake-storage-gen2-or-blob-storage-using-a-sas-token)
# MAGIC 1. set the spark config for sas token
# MAGIC 1. list files form demo container
# MAGIC 1. read data from circuits.csv file
# MAGIC ##### [more about shared access token 🔗](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.formula369.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.formula369.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.formula369.dfs.core.windows.net", "sp=rl&st=2023-04-15T18:50:24Z&se=2023-04-17T02:50:24Z&spr=https&sv=2021-12-02&sr=c&sig=EX6goWm%2BSF9by04TdnEdGoDjNndJZvzIJYAv1NxJKU8%")

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula369.dfs.core.windows.net"))

# COMMAND ----------

circuit_demo = spark.read.csv("abfss://demo@formula369.dfs.core.windows.net/circuits (1).csv")
display(circuit_demo)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Access by adding IAM roles as Storage Blob Data Contributor
# MAGIC ![as](https://learn.microsoft.com/en-us/azure/databricks/_static/images/clusters/credential-passthrough-single.png)
# MAGIC #### Edit and restart the cluster
# MAGIC ###### now no need to adding credentials; users can have access to the storage account as per the role

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula369.dfs.core.windows.net"))

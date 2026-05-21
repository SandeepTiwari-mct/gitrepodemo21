# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "0d8f4857-6430-435f-ba63-de12095188f3",
# META       "default_lakehouse_name": "lkh1",
# META       "default_lakehouse_workspace_id": "36cabf81-75cd-4a07-a4ef-c02d311bf8fc",
# META       "known_lakehouses": [
# META         {
# META           "id": "0d8f4857-6430-435f-ba63-de12095188f3"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/products.csv")
# df now is a Spark DataFrame containing CSV data from "Files/products.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.createOrReplaceTempView('v1')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

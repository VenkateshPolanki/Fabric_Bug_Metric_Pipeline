#!/usr/bin/env python
# coding: utf-8

# ## bronze_ingestion
# 
# null

# **Reading Source File**

# In[1]:


df = spark.read.format("csv")\
     .option("header", "true")\
     .option("inferSchema", "true")\
     .option("delimiter", ";")\
     .load("Files/bronze/azdo/brnz_azdo_workitems_current_anonymized.csv.csv")


# **Adding Metadata Columns**

# In[2]:


from pyspark.sql.functions import *

df = df.withColumn("ingestion_timestamp", current_timestamp())
df = df.withColumn("source_file_name", lit("brnz_azdo_workitems_current_anonymized.csv"))


# **Validate Schema**

# In[3]:


df.printSchema()


# **Validate sample data**

# In[4]:


display(df.limit(5))


# **DF Row Count**

# In[5]:


source_count = df.count()
print("Source df Count: ", source_count)


# **Writing into delta table**

# In[6]:


df.write.mode("overwrite").saveAsTable("bronze.bronze_azdo_workitems")


# **Read Bronze table**

# In[7]:


bronze_df = spark.table("bronze.bronze_azdo_workitems")


# **Bronze table Count**

# In[8]:


target_count = bronze_df.count()
print("Bronze Table Count: ", target_count)


# **Compare Counts**

# In[9]:


if source_count == target_count:
    print("Validation passed - Row Counts match")
else:
    print("Validation failed - Row Counts mismatch")  


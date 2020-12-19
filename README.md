# sfo_crime_statics_with_spark
This is the project to provide statistical analysis of the data using Apache Spark Structured Streaming. The stream and the data is produced as Kafka topic and Kafka Spark will be used to consume and analyse the data.

# Project details from Udacity :
## How To Run :

Modify the zookeeper.properties and producer.properties given to suit your topic and port number of your choice. Start up these servers in the terminal using the commands:

Unzip police-department-calls-for-service.json.zip to the current folder.
  >/usr/bin/zookeeper-server-start zookeeper.propertie <br>
 /usr/bin/kafka-server-start server.properties

You’ll need to open up two terminal tabs to execute each command.

Install requirements using the provided ./start.sh script. This needs to be done every time you re-open the workspace, or anytime after you've refreshed, or woken up, or reset data, or used the "Get New Content" button in this workspace.

In the terminal, to install other packages that you think are necessary to complete the project, use conda install <package_name>. You may need to reinstall these packages every time you re-open the workspace, or anytime after you've refreshed, or woken up, or reset data, or used the "Get New Content" button in this workspace.

#### Consumer Output
![](https://github.com/vinayms/sfo_crime_statics_with_spark/blob/main/images/Sample_Kafka_Consumer_console_output.png)

#### Spark JOB Progress
![](https://github.com/vinayms/sfo_crime_statics_with_spark/blob/main/images/Progress_report_Spark_JOB.png)

#### Spark JOB UI
![](https://github.com/vinayms/sfo_crime_statics_with_spark/blob/main/images/Spark_Streaming_UI.png)
#### SF Crime data
![](https://github.com/vinayms/sfo_crime_statics_with_spark/blob/main/images/Console_output_window_crime_stats.png)

#### Udacity Question :

1.  How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
    + Observed varying batch size with changing config value of "maxOffsetsPerTrigger", the throughput increased and more records processed with the increase in the "maxOffsetsPerTrigger" values. (like 200, 300, 500)
2.  What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
    + Tuning "maxOffsetsPerTrigger" and "sf.window()" we can control how many records/batch could be processed. With a good (maximum required) number of records processed in batch will be efficient.

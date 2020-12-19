# sfo_crime_statics_with_spark
This is the project to provide statistical analysis of the data using Apache Spark Structured Streaming. The stream and the data is produced as Kafka topic and Kafka Spark will be used to consume and analyse the data.

# Project details from Udacity :
# How To Run :

Modify the zookeeper.properties and producer.properties given to suit your topic and port number of your choice. Start up these servers in the terminal using the commands:

  /usr/bin/zookeeper-server-start zookeeper.properties
  /usr/bin/kafka-server-start server.properties

You’ll need to open up two terminal tabs to execute each command.

Install requirements using the provided ./start.sh script. This needs to be done every time you re-open the workspace, or anytime after you've refreshed, or woken up, or reset data, or used the "Get New Content" button in this workspace.

In the terminal, to install other packages that you think are necessary to complete the project, use conda install <package_name>. You may need to reinstall these packages every time you re-open the workspace, or anytime after you've refreshed, or woken up, or reset data, or used the "Get New Content" button in this workspace.

# Consumer Output
![](https://github.com/vinayms/sfo_crime_statics_with_spark/blob/main/images/Sample_Kafka_Consumer_console_output.png)

# Spark JOB Progress
![](https://github.com/vinayms/sfo_crime_statics_with_spark/blob/main/iimages/Progress_report_Spark_JOB.png)

# Spark JOB UI
![](https://github.com/vinayms/sfo_crime_statics_with_spark/blob/main/images/Spark_Streaming_UI.png)
# SF Crime data
![](https://github.com/vinayms/sfo_crime_statics_with_spark/blob/main/images/Console_output_window_crime_stats.png)

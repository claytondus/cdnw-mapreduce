#!/bin/sh
#Generate stop word list and inverted index
#export HADOOP_DIR
export HADOOP_STREAMING=/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar
export HDFS_PATH=/user/$USER

hadoop fs -mkdir $HDFS_PATH/pa2
hadoop fs -mkdir $HDFS_PATH/pa2/shake
hadoop fs -rm $HDFS_PATH/pa2/shake/*
hadoop fs -put ../shake/pg100.txt $HDFS_PATH/pa2/shake/

hadoop fs -rm -R $HDFS_PATH/pa2/wc/
hadoop jar $HADOOP_STREAMING -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input $HDFS_PATH/pa2/shake/ -output $HDFS_PATH/pa2/wc

hadoop fs -rm -R /user/$USER/pa2/doc_counts/
hadoop jar $HADOOP_STREAMING -files mapper2.py,reducer.py -mapper mapper2.py -reducer reducer.py -input /user/$USER/pa2/wc/ -output /user/$USER/pa2/doc_counts

hadoop fs -rm -R /user/$USER/pa2/stop_words/
hadoop jar $HADOOP_STREAMING -files mapper3.py,reducer3.py -mapper mapper3.py -reducer reducer3.py -input /user/$USER/pa2/doc_counts/ -output /user/$USER/pa2/stop_words

rm ./stop-words.json
hadoop fs -get /user/$USER/pa2/stop_words/part-00000 ./stop-words.json

hadoop fs -rm -R /user/$USER/pa2/inverted_index/
hadoop jar $HADOOP_STREAMING -files mapper4.py,reducer4.py,stop-words.json -mapper mapper4.py -reducer reducer4.py -input /user/$USER/pa2/shake/ -output /user/$USER/pa2/inverted_index

rm ./inverted_index.json
hadoop fs -get /user/$USER/pa2/inverted_index/part-00000 ./inverted_index.json

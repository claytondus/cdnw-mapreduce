#!/bin/sh
#Generate stop word list and inverted index
#export HADOOP_DIR

hadoop fs -mkdir pa2
hadoop fs -mkdir pa2/shake
hadoop fs -rm pa2/shake/*
hadoop fs -put ../shake/pg100.txt pa2/shake/

hadoop fs -rm -R pa2/wc/
hadoop jar $HADOOP_DIR/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input pa2/shake/ -output pa2/wc

hadoop fs -rm -R pa2/doc_counts/
hadoop jar $HADOOP_DIR/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -files mapper2.py,reducer.py -mapper mapper2.py -reducer reducer.py -input pa2/wc/ -output pa2/doc_counts

hadoop fs -rm -R pa2/stop_words/
hadoop jar $HADOOP_DIR/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -files mapper3.py,reducer3.py -mapper mapper3.py -reducer reducer3.py -input pa2/doc_counts/ -output pa2/stop_words

rm ./stop-words.json
hadoop fs -get pa2/stop_words/part-00000 ./stop-words.json

hadoop fs -rm -R pa2/inverted_index/
hadoop jar $HADOOP_DIR/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -files mapper4.py,reducer4.py,stop-words.json -mapper mapper4.py -reducer reducer4.py -input pa2/shake/ -output pa2/inverted_index

rm ./inverted_index.json
hadoop fs -get pa2/inverted_index/part-00000 ./inverted_index.json

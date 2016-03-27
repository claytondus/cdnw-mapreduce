hadoop fs -mkdir pa2
hadoop fs -mkdir pa2/shake
hadoop fs -put /tmp/shake/*.txt pa2/shake/

hadoop jar /usr/prog/hadoop-2.7.2/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input pa2/shake/ -output pa2/wc

hadoop jar /usr/prog/hadoop-2.7.2/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -files mapper2.py,reducer.py -mapper mapper2.py -reducer reducer.py -input pa2/wc/ -output pa2/doc_counts

hadoop jar /usr/prog/hadoop-2.7.2/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -files mapper3.py,reducer3.py -mapper mapper3.py -reducer reducer3.py -input pa2/doc_counts/ -output pa2/stop_words

hadoop fs -get pa2/stop_words/part-00000 ./stop-words.txt

 

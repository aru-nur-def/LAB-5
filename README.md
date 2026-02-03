# Lab 5 – Mini-MapReduce on Amazon EMR

**Student:** Aruzhan Saparkhankyzy  
**Group:** IT-2306  
**Course:** Distributed Computing  

---

## Overview
This laboratory work demonstrates the use of the MapReduce programming model on a Hadoop cluster deployed with Amazon Elastic MapReduce (EMR).
A WordCount application was implemented using Python Hadoop Streaming, with input and output data stored in HDFS.
An experiment was conducted to analyze how execution time changes with different input sizes.

---

## Objectives
The main objective of this laboratory work is to study the MapReduce programming model and understand how it enables distributed processing of large datasets.
Additionally, the work focuses on deploying and configuring a Hadoop cluster using Amazon EMR, executing a WordCount MapReduce job using Python,
utilizing HDFS as a distributed storage system, and analyzing performance through experimentation.

---

## Technology Stack
- Amazon EMR (EMR 7.12.0)
- Hadoop 3.4.1
- Hadoop Distributed File System (HDFS)
- Python (Hadoop Streaming)
- SSH and AWS Management Console

---

## Dataset
The dataset used in this lab is a text corpus from Simple English Wikipedia.
It was downloaded on the EMR master node and uploaded to HDFS for distributed processing.

---

## Cluster Configuration
- Primary (Master) node: 1
- Core (Worker) node: 1
- Instance type: m4.large

The cluster was verified using YARN and HDFS administrative commands to ensure all services were running correctly.

---

## MapReduce Implementation (WordCount)
- Mapper: extracts lowercase alphabetic words and emits (word, 1) pairs.
- Reducer: aggregates values for each word and outputs (word, total_count).

The application was executed using Hadoop Streaming.

---

## Running the Job
```bash
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
  -input /user/hadoop/input/corpus.txt \
  -output /user/hadoop/output/wordcount \
  -mapper "python3 mapper.py" \
  -reducer "python3 reducer.py" \
  -file mapper.py \
  -file reducer.py
```

---

## Output Validation
The output directory contains the _SUCCESS file and the reducer output file part-00000.
The top-10 most frequent words were extracted using:

```bash
hdfs dfs -cat /user/hadoop/output/wordcount/part-00000 | sort -k2 -nr | head
```

Typical results include words such as the, of, in, a, and and.

---

## Experiment: Input Size Analysis
An input-size experiment was performed to analyze performance.

- Small input (~1 MB): 50.184 seconds
- Large input (~32 MB): 69.150 seconds

The results show that execution time increases with larger input sizes due to increased map output and shuffle/sort overhead.

---

## Conclusion
This laboratory work successfully demonstrated the deployment of a Hadoop cluster on Amazon EMR and the execution of a MapReduce WordCount job
using Python and Hadoop Streaming.
The experiment confirmed that MapReduce execution time grows with input size, highlighting the scalability characteristics of distributed data processing systems.

---

## Repository Structure
```
.
├── mapper.py
├── reducer.py
├── README.md
└── report.pdf
```

---

## Status
✔ Lab completed  
✔ Experiment performed  
✔ Ready for submission  

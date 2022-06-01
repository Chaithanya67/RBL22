#!/bin/bash

python3 main.py dataset study 1 &&
python3 evaluation_metrics.py --clustered prediction.csv --goldstandard dataset/study_ground_truth.csv

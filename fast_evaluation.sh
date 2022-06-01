chmod u+x /content/RBL22/main.py /content/RBL22/dataset /content/RBL22/dataset/study  &&
python3 /content/RBL22/evaluation_metrics.py --clustered prediction.csv --goldstandard dataset/study_ground_truth.csv


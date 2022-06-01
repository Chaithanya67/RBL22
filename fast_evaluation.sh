chmod u+x /content/Vertex-Clustering/main.py /content/Vertex-Clustering/datasets /content/Vertex-Clustering/datasets/study  &&
python3 /content/Vertex-Clustering/evaluation_metrics.py --clustered prediction.csv --goldstandard datasets/study_ground_truth.csv

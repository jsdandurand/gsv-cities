import kagglehub

# Download latest version
path = kagglehub.dataset_download("amaralibey/gsv-cities")

print("Path to dataset files:", path)
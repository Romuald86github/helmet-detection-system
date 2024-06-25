import os

# Define the directory structure
directories = [
    "data/raw",
    "data/processed",
    "models/yolo",
    "src",
    "iot",
    "app"
]

# Define the empty scripts to be created
scripts = {
    "src": ["data_preparation.py", "model_setup.py", "detection.py", "video_stream.py", "deployment.py"],
    "iot": ["iot_device.py", "lambda_function.py"],
    "app": ["interface.py"]
}

# Define the model files
model_files = {
    "models/yolo": ["yolov3.cfg", "yolov3.weights", "yolov3.names"]
}

# Function to create directories and .gitkeep files for empty directories
def create_directories(directories):
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        # Add a .gitkeep file to empty directories
        if not os.listdir(directory):
            with open(os.path.join(directory, ".gitkeep"), 'w') as f:
                f.write("")

# Function to create empty scripts
def create_scripts(scripts):
    for folder, files in scripts.items():
        for file in files:
            with open(os.path.join(folder, file), 'w') as f:
                f.write("# Script: {}\n".format(file))

# Function to create model files
def create_model_files(model_files):
    for folder, files in model_files.items():
        for file in files:
            with open(os.path.join(folder, file), 'w') as f:
                f.write("# Model file: {}\n".format(file))

# Create directories and scripts
create_directories(directories)
create_scripts(scripts)
create_model_files(model_files)

# Create requirements.txt
with open("requirements.txt", 'w') as f:
    f.write("# List of project dependencies\n")

print("Project structure created successfully.")

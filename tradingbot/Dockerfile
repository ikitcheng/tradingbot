# Use the official python image.
FROM python:3.9

# Allow statements and log messages to immediately appear in the native logs
ENV PYTHONUNBUFFERED 1

# sets the working directory to /app
WORKDIR /app

# install swig
RUN apt-get update && apt-get install -y swig

# installs the latest version of pip
RUN pip install --upgrade pip

# Copies the requirements.txt file to the working directory
COPY requirements.txt /app

# installs the dependencies from the requirements.txt file
RUN pip install -r requirements.txt

# Copies the rest of the files to the working directory
COPY . /app

# Expose Jupyter Notebook port
EXPOSE 8888

# Exposes the port 8888 for the jupyter notebook
CMD ["jupyter", "lab", "--notebook-dir", "/app/", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
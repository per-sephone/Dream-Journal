FROM google/cloud-sdk

LABEL maintainer="nob@pdx.edu"

COPY . /app

WORKDIR /app

RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && apt update --allow-releaseinfo-change -y && apt install -y python3-pip && pip3 install -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app

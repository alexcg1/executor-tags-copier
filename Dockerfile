FROM jinaai/jina:3.13.0-py39-perf

# copy the content of the repo to the container
COPY . /workspace
WORKDIR /workspace

# install the third-party requirements
RUN pip install -r requirements.txt

# start jina executor using the config file
ENTRYPOINT ["jina", "executor", "--uses", "config.yml"]
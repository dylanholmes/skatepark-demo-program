ARG RUNTIME_VERSION="3.11"

FROM python:${RUNTIME_VERSION}
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["/entry_file.sh"]
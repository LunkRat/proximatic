FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN pip install --upgrade pip && \
      pip install proximatic &&\
      apt-get remove -y curl && \
      rm -rf /var/lib/apt/lists/
COPY ./app /app

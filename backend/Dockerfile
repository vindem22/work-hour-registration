FROM python:3.8

WORKDIR /usr/app/src

COPY entrypoint.sh .

COPY requirements.txt .

RUN pip install -r requirements.txt --no-input

RUN chmod +x /usr/app/src/entrypoint.sh

ENTRYPOINT [ "/usr/app/src/entrypoint.sh" ]
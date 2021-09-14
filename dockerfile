FROM python:3.6

COPY . /src/

WORKDIR /src/

RUN pip3 install --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python3" , "app.py"]
FROM jcdemo/flaskapp

RUN pip install --no-cache-dir --r requirements.txt

COPY . /src/

EXPOSE 8080

CMD ["python", "/src/app.py"]
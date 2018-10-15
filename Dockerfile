FROM MohammadAli/flask-Todoapi-Postgres:1


ADD ./app /home/app/

WORKDIR /home/app/

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]

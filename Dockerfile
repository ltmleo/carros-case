FROM leonardomontero/py-mongo-flask:1.0.0

WORKDIR /app

COPY . .

ENTRYPOINT [ "python", "/app/Main.py" ]

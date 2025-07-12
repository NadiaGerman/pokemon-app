FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY api/ ./api
COPY db/ ./db
COPY utils.py ./
COPY main.py ./

EXPOSE 5000

CMD ["python", "main.py"]

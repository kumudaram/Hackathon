FROM python:3.8.10-slim

WORKDIR /app

COPY requirements.txt /app/


RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

#CMD ["uvicorn", "APIDevelopement.model_app:app", "--host", "0.0.0.0", "--port", "8000"]

#GCP
ENTRYPOINT ["uvicorn", "APIDevelopement.model_app:app", "--host", "0.0.0.0", "--port", "8000"]


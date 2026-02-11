FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
# Hugging Face için portu 7860 yapıyoruz
EXPOSE 7860
# Uvicorn'u 7860 portunda çalışacak şekilde güncelliyoruz
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]

FROM python:3.12-slim
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 
COPY form.py .
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "form.py"]
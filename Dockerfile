FROM  python:3.8-buster
ENV  PYTHONDONTWRITEBYETCODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app/
COPY requirements.txt /app/
RUN sed -i 's/http:\/\/[a-zA-Z0-9]*.[a-zA-Z0-9]*.*.com/http:\/\/ir.ubuntu.sindad.cloud/g' /etc/apt/sources.list
RUN pip3 install --upgrade pip -i https://mirror-pypi.runflare.com/simple 
RUN pip3 install -r requirements.txt -i https://mirror-pypi.runflare.com/simple 
COPY ./core /app/
EXPOSE 8000
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]

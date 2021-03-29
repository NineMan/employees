FROM python:3.8

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/


COPY . /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"

CMD ["python", "app/main.py"]
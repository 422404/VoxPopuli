FROM python:3

WORKDIR /usr/src/

COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

CMD [ "python", "./vox.py" ]
FROM python:3.10-alpine

WORKDIR /app
RUN apk add --no-cache \
    build-base cairo-dev cairo cairo-tools \
    # pillow dependencies
    jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev


COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8080

RUN chmod +x ./start.sh
ENV PYTHON_ENV=production
ENV FLASK_APP=app/main.py
RUN python pre_cache_images.py
# CMD [ "python3", "app/main.py"]
CMD ["sh", "/app/start.sh"]

FROM nginx:1.21-alpine

WORKDIR /app

ADD app/ /app

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx/nginx.conf /etc/nginx/conf.d

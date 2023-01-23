FROM nginx:1.21-alpine

ADD ../app/ /app

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

FROM nginx:1.22.0
LABEL MAINTAINER ="SHAHRAM | ZCFCO.IR"

COPY nginx.conf /etc/nginx/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
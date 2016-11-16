FROM rhel7.3

RUN yum update -y \
 && yum-config-manager --enable rhel-server-rhscl-7-rpms \
 && yum install -y scl-utils rh-nginx18 \
 && yum clean all \
#&& echo "daemon off;" >> /etc/opt/rh/rh-nginx18/nginx/nginx.conf

ADD nginx.conf /etc/opt/rh/rh-nginx18/nginx/nginx.conf
ADD conf.d/* /etc/opt/rh/rh-nginx18/nginx/conf.d/

#VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx", "/var/www/html"]
#WORKDIR /etc/nginx

CMD /opt/rh/rh-nginx18/root/sbin/nginx

EXPOSE 80
EXPOSE 443

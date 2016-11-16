FROM rhel7.3

RUN yum -y --setopt=tsflags=nodocs update \
 && yum-config-manager --enable rhel-server-rhscl-7-rpms \
 && yum -y --setopt=tsflags=nodocs install scl-utils httpd24-httpd rh-python35 rh-python35-mod_wsgi \
 && yum clean all \
 && mkdir -p /my/web/{wsgi,html} \
 && echo Welcome to $(hostname) docroot >/my/web/html/index.html

ADD start-httpd /usr/local/bin/start-httpd
ADD 00_myvhost.conf /opt/rh/httpd24/root/etc/httpd/conf.d/00_myvhost.conf
ADD test.wsgi /my/web/wsgi/test.wsgi

RUN chmod +x /usr/local/bin/start-httpd

CMD ["/usr/local/bin/start-httpd"]

EXPOSE 80
EXPOSE 443

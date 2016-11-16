FROM rhel7.3

RUN yum -y --setopt=tsflags=nodocs update \
 && yum-config-manager --enable rhel-server-rhscl-7-rpms \
 && yum -y --setopt=tsflags=nodocs install scl-utils rh-python35 rh-python35-python-devel rh-python35-python-pip \
 && yum clean all \
 && scl enable rh-python35 'pip install flower'

ADD start-celeryflower /usr/local/bin/start-celeryflower
RUN chmod +x /usr/local/bin/start-celeryflower

RUN mkdir -p /etc/flower /var/flower/db
COPY flowerconfig.py /etc/flower/flowerconfig.py

CMD ["/usr/local/bin/start-celeryflower"]

EXPOSE 5555

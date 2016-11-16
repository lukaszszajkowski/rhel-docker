FROM rhel7.3

RUN yum -y --setopt=tsflags=nodocs update \
 && yum-config-manager --enable rhel-server-rhscl-7-rpms \
 && yum -y --setopt=tsflags=nodocs install scl-utils rh-python35 rh-python35-python-devel rh-python35-python-pip \
 && yum clean all \
 && scl enable rh-python35 'pip install celery'

WORKDIR /root

RUN { \
	echo 'import os'; \
	echo "BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'amqp://')"; \
} > celeryconfig.py

# --link some-rabbit:rabbit "just works"
ENV CELERY_BROKER_URL amqp://guest:guest@127.0.0.1

ADD start-celery /usr/local/bin/start-celery
RUN chmod +x /usr/local/bin/start-celery

CMD ["/usr/local/bin/start-celery"]


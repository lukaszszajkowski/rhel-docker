FROM rhel7.3

RUN yum -y --setopt=tsflags=nodocs update \
 && yum install -y wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-8.noarch.rpm \
 && yum install -y rabbitmq-server pwgen \
 && yum clean all \
 && rabbitmq-plugins enable rabbitmq_management

ADD scripts /scripts
RUN chmod +x /scripts/*
RUN touch /.firstrun

ENTRYPOINT ["/scripts/start-rabbitmq"]
CMD [""]

EXPOSE 4369 5671 5672 15671 15672 25672

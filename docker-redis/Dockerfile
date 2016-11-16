FROM rhel7.3

RUN yum -y --setopt=tsflags=nodocs update \
 && yum-config-manager --enable rhel-server-rhscl-7-rpms \
 && yum -y --setopt=tsflags=nodocs install scl-utils gcc make \
 && yum clean all

ADD http://download.redis.io/releases/redis-3.2.5.tar.gz /tmp/redis.tar.gz
ADD start-redis /usr/local/bin

RUN cd /tmp \
 && tar zxvf redis.tar.gz \
 && cd redis-3.2.5/deps \
 && make hiredis lua jemalloc linenoise geohash-int \
 && cd .. \
 && make \
 && cd src \
 && cp redis-server redis-cli /usr/local/bin \
 && cp redis-sentinel redis-benchmark redis-check-aof redis-check-rdb /usr/local/bin \
 && mkdir -p /etc/redis \
 && rm -rf /tmp/redis-*

ADD redis.conf /etc/redis/redis.conf 

RUN chmod +x /usr/local/bin/start-redis

CMD ["/usr/local/bin/start-redis"]

EXPOSE 6379

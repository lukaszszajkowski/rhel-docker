FROM rhel7.3

RUN yum -y --setopt=tsflags=nodocs update \ 
 && yum-config-manager --enable rhel-server-rhscl-7-rpms \
 && yum -y --setopt=tsflags=nodocs install \
	scl-utils gcc gcc-c++ gd-devel GeoIP-devel libxslt-devel make perl \
	perl-ExtUtils-Embed readline-devel unzip zlib-devel pcre-devel \
	openssl-devel \
 && yum clean all

ADD https://openresty.org/download/openresty-1.11.2.1.tar.gz /tmp/openresty.tar.gz

RUN cd /tmp \
 && tar zxvf openresty.tar.gz \
 && cd openresty-1.11.2.1/ \
 && ./configure  \
 && gmake \
 && gmake install

ENTRYPOINT ["/usr/local/openresty/bin/openresty", "-g", "daemon off;"]

EXPOSE 80

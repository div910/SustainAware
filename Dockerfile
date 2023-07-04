FROM centos:7
LABEL maintainer="SustainAware"

RUN \
 yum install -y epel-release && \
 yum install -y wget \
                git \
                which \
                make \
                python-setuptools \
                python-pip \
                python-dev \
                zlib-devel \
                openssl-devel \
                mysql-devel \
                python-devel \
                gcc-c++ \
                snappy-devel \
                gcc \
                postgresql \
                postgresql-devel \
                sqlite-devel \
                expat-devel \
                bzip2-devel \
                libffi-devel \
                zlib-devel \
                libxslt-devel \
                libxml2-devel \
                python-argparse \
                xmlsec1-devel \
                xmlsec1-openssl-devel \
                libtool-ltdl-devel && \
 yum install -y nginx && \
 yum install -y screen && \
 pip install supervisor && \

 mkdir -p /var/log/supervisor /etc/supervisord.d /logs /opt/logs /etc/newrelic && \
 yum clean all

EXPOSE 80
EXPOSE 8000


RUN \
 cd /opt && \
 wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz  && \
 tar xvf Python-3.8.0.tgz && \
 cd /opt/Python-3.8.0 && \
 ./configure --enable-shared --with-system-ffi --with-system-expat --enable-unicode=ucs4 --prefix=/usr/local/python3.8 LDFLAGS="-L/usr/local/python3.8/lib -Wl,--rpath=/usr/local/python3.8/lib"  && \
 make && \
 make altinstall && \
 rm -f /etc/localtime && \
 ln -s /usr/share/zoneinfo/Asia/Kolkata /etc/localtime && \
 rm -Rf Python-3.8.0.tgz /opt/Python-3.8.0

WORKDIR /usr/local/sustainaware/

COPY ./requirements.txt /etc/pip/requirements.txt
RUN /usr/local/python3.8/bin/pip3.8 install -r /etc/pip/requirements.txt

COPY ./ /usr/local/sustainaware

#RUN /usr/local/python3.8/bin/python3.8  /usr/local/team/mysite/mysite/manage.py runserver

CMD ["/usr/local/python3.8/bin/python3.8", "/usr/local/sustainaware/sustainaware_backend//manage.py", "runserver"]
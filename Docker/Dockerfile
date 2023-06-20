FROM ubuntu:18.04
LABEL maintainer="vamshi"
RUN apt-get update && apt-get -y install
EXPOSE 80
ENTRYPOINT ["/usr/sbin/apachectl"]
CMD ["-D","FOREGROUND"]
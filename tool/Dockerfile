FROM alpine:3.11

RUN apk update && apk upgrade && apk add --no-cache \
    bash \
    procps \
    drill \
    git \
    coreutils \
    libidn \
    curl \
    nmap \
    nmap-scripts

WORKDIR /home/tool
RUN git clone --depth=1 https://github.com/drwetter/testssl.sh.git .
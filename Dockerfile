FROM python:3.8.5-slim-buster
LABEL version="2.0.1"
LABEL description="litncov - A ncov report library and tool for LIT(Luoyang Institute of Science and Technology)"
LABEL maintainer="icepie"
ENV LANG zh_CN.UTF-8
ENV LANGUAGE zh_CN.UTF-8
ENV LC_ALL zh_CN.UTF-8

USER root

RUN rm -rf /etc/localtime && \
  ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
  pip3 install --upgrade pip && \
  pip3 install --upgrade litncov && \
  groupadd -r nonroot && \
  useradd -m -r -g nonroot -d /home/nonroot -s /usr/sbin/nologin -c "Nonroot User" nonroot && \
  mkdir -p /home/nonroot/workdir && \
  chown -R nonroot:nonroot /home/nonroot 

USER nonroot
ENV HOME /home/nonroot
WORKDIR /home/nonroot/workdir
VOLUME ["/home/nonroot/workdir"]
ENV USER nonroot
ENTRYPOINT ["/usr/local/bin/litncov"]
CMD ["--help"]

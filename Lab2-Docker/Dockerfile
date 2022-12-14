FROM ubuntu:20.04

# set environment vars
ENV HADOOP_HOME /opt/hadoop
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# install packages
RUN \
  apt-get update && apt-get install -y \
  ssh \
  rsync \
  vim \
  openjdk-8-jdk \
  nano

# download and extract hadoop, set JAVA_HOME in hadoop-env.sh, update path
RUN \
  wget https://dlcdn.apache.org/hadoop/common/hadoop-3.2.4/hadoop-3.2.4.tar.gz && \
  tar -xzf hadoop-3.2.4.tar.gz && \
  mv hadoop-3.2.4 $HADOOP_HOME && \
  rm hadoop-3.2.4.tar.gz && \
  echo "export JAVA_HOME=$JAVA_HOME" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
  echo "export HDFS_NAMENODE_USER=root" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
  echo "export HDFS_DATANODE_USER=root" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
  echo "export HDFS_SECONDARYNAMENODE_USER=root" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
  echo "export YARN_RESOURCEMANAGER_USER=root" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
  echo "export YARN_NODEMANAGER_USER=root" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
  echo "PATH=$PATH:$HADOOP_HOME/bin" >> ~/.bashrc

RUN \
  apt-get install -y openssh-server

# create ssh keys
RUN \
  ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \
  cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
  chmod 0600 ~/.ssh/authorized_keys

# copy hadoop configs
ADD configs/*xml $HADOOP_HOME/etc/hadoop/

# copy ssh config
ADD configs/ssh_config /root/.ssh/config

# copy script to start hadoop
ADD start-hadoop.sh start-hadoop.sh

RUN \
   chown root:$USER ~/.ssh/config && \
   chmod 644 ~/.ssh/config

USER root 

# expose various ports
EXPOSE 8088 50070 50075 50030 50060 22 9870 9864 

# start hadoop
CMD bash start-hadoop.sh

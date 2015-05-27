from ubuntu:14.04


run apt-get update --fix-missing

run apt-get install -y python-software-properties \
                       build-essential \
                       software-properties-common

run add-apt-repository ppa:fkrull/deadsnakes

run apt-get update

run apt-get install -y python2.7 python-dev curl 

run curl https://bootstrap.pypa.io/get-pip.py | python

run pip install yhat==1.2.10
run pip install pandas==0.16.1

copy hello.py /root/hello.py
workdir /root
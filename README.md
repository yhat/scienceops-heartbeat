# ScienceOps Heartbeat
Automated CI style deployments for ScienceOps models.


## Jenkins
### With Docker
```bash
cd $WORKSPACE

set -ex

docker build -t yhat/heartbeat .
docker run -e 'USERNAME=YOUR_USERNAME' -e 'APIKEY=YOUR_APIKEY' -e 'OPS_ENDPOINT=http://scienceops-hostname/' yhat/heartbeat python hello.py
```
### With `virtualenv`
```bash
$ sudo apt-get -y update
$ sudo apt-get install -y python-software-properties python-pip
$ sudo pip install virtualenv
$ virtualenv env
$ source env/bin/activate
$ sudo pip install yhat
$ python hello.py
```

## Cron
Same as `virtualenv`

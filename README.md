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
# bootstrap your server
$ sudo apt-get -y update
$ sudo apt-get install -y python-software-properties python-pip
$ sudo pip install virtualenv

# as a part of your jenkins job
$ virtualenv env
$ source env/bin/activate
$ sudo pip install yhat
$ python hello.py
$ deactivate
$ rm -rf env
```

## Cron
Same as `virtualenv`

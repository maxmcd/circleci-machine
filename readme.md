$ ssh -p 64536 -L 8081:35.196.37.168:2376 34.224.66.252
root@6d447a644094:~# channel 3: open failed: administratively prohibited: port forwarding is disabled
channel 3: open failed: administratively prohibited: port forwarding is disabled

http://blog.wrouesnel.com/articles/SSH%20port%20forwarding%20when%20AllowTCPForwarding%20is%20disabled/

socat TCP-LISTEN:8082,reuseaddr,fork "EXEC:ssh -p 64536 34.224.66.252 nc 35.196.37.168 2376"

ssh -p 64536 34.224.66.252 cat /tmp/docker-certs952729926/key.pem > key.pem
ssh -p 64536 34.224.66.252 cat /tmp/docker-certs952729926/cert.pem > cert.pem
ssh -p 64536 34.224.66.252 cat /tmp/docker-certs952729926/ca.pem > ca.pem


socat TCP-LISTEN:8082,reuseaddr,fork "EXEC:ssh -p 64536 34.224.66.252 nc 35.196.37.168 2376"

maxm 👻 :~
$ DOCKER_HOST=tcp://127.0.0.1:8082 docker ps
Get http://127.0.0.1:8082/v1.39/containers/json: net/http: HTTP/1.x transport connection broken: malformed HTTP response "\x15\x03\x01\x00\x02\x02".
* Are you trying to connect to a TLS-enabled daemon without TLS?
maxm 👻 :~
$ DOCKER_TLS_VERIFY=1 DOCKER_CERT_PATH=/Users/maxm/Sites/golang/src/github.com/maxmcd/circleci-machine  DOCKER_HOST=tcp://127.0.0.1:8082 docker ps
error during connect: Get https://127.0.0.1:8082/v1.39/containers/json: x509: certificate is valid for 35.196.37.168, not 127.0.0.1
maxm 👻 :~
$ vim /etc/hosts
maxm 👻 :~
$ sudo vim /etc/hosts
Password:
maxm 👻 :~
$ DOCKER_TLS_VERIFY=1 DOCKER_CERT_PATH=/Users/maxm/Sites/golang/src/github.com/maxmcd/circleci-machine  DOCKER_HOST=tcp://35.196.37.168:8082 docker ps
Cannot connect to the Docker daemon at tcp://35.196.37.168:8082. Is the docker daemon running?
maxm 👻 :~
$ DOCKER_TLS_VERIFY=1 DOCKER_CERT_PATH=/Users/maxm/Sites/golang/src/github.com/maxmcd/circleci-machine  DOCKER_HOST=tcp://127.0.0.1:8082 docker ps
error during connect: Get https://127.0.0.1:8082/v1.39/containers/json: x509: certificate is valid for 35.196.37.168, not 127.0.0.1

docker run --rm -u root -p 8008:8008 \
-v jenkins-data:/var/jenkins_home \
-v $(which docker):/usr/bin/docker \
-v /var/run/docker.sock:/var/run/docker.sock \
-v "$HOME":/home \
--name jenkins_server jenkins/jenkins:lts

##264928f29f164af3a8b889925ff7571e
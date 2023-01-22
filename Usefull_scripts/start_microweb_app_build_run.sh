docker build -t microweb_app:latest .
docker run -t -d -p 80:5050 --name microflask microweb_app
# docker container inspect container id | grep IPAddress
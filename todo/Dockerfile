FROM phusion/passenger-full:0.9.11

# Set correct environment variables.
ENV HOME /root

# Use baseimage-docker's init process.
CMD ["/sbin/my_init"]

# ...put your own build instructions here...

# Install postgresql adapter and pip
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get install -y python-psycopg2 libpq-dev python3-pip python3-setuptools

# Setup postgres variables so they don't get removed by nginx
ADD postgresql/postgres-env.conf /etc/nginx/main.d/postgres-env.conf

#install bower
RUN npm install -g bower

#install app
ADD ./app /home/app
WORKDIR /home/app
RUN pip3 install -r requirements/development.txt

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

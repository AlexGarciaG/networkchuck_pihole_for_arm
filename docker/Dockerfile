FROM pihole/pihole:2023.03.1


#Install Python
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install python3-pip -y


# Copy Files and give permissions
WORKDIR /home
COPY network/ network/
WORKDIR /home/network
#Expose ports
    ## Pi Hole
EXPOSE 53/tcp 
EXPOSE 53/udp
EXPOSE 80
EXPOSE 443
    ## API for PiHole
EXPOSE 8080

#Install python requirements
RUN pip3 install -r requirements.txt
# Launch Python script to block website.
CMD [ "python3", "./network.py"]

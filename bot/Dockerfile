#FROM rasa/rasa-sdk:2.8.2
FROM rasa/rasa:2.8.33-full
#FROM rasa/rasa-sdk:2.30.0
# Use subdirectory as working directory
# Copy any additional custom requirements, if necessary (uncomment next line)
# COPY actions/requirements-actions.txt ./
# Change back to root user to install dependencies
#USER root
# Install extra requirements for actions code, if necessary (uncomment next line)
# RUN pip install -r requirements-actions.txt
# Copy actions folder to working directory
USER root
RUN /opt/venv/bin/python -m pip install --upgrade pip
COPY ./  /app
WORKDIR /app
RUN ls
ENV RASA_TELEMETRY_ENABLED=false
RUN  rasa train -c to_chat/config.yml -d to_chat/domain.yml --data to_chat/data --debug
CMD [ "run","-m","/app/models","--enable-api","--cors","*","--debug" ]
#EXPOSE 5005
#COPY ./  /app
#WORKDIR /app

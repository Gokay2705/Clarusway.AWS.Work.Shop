FROM ubuntu
RUN apt-get update -y && \
    apt-get install -y python3-pip python3

WORKDIR /app
COPY  . ./
ADD static static
ADD templates templates
RUN pip3 install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python3"]
CMD ["roman-numerals-converter-app.py"]
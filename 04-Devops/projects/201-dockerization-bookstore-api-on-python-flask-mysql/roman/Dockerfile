FROM ubuntu
RUN apt-get update -y && \
    apt-get install -y python3-pip python3 git
WORKDIR /app
RUN git clone https://github.com/JBCodeWorld/aws-workshop.git && \
    mv aws-workshop/001-roman-numerals-converter/* . && \
    rm -rf aws-workshop && \
    apt-get remove -y git
COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python3"]
CMD ["roman-numerals-converter-app.py"]

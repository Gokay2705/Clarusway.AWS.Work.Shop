# Dockerize Roman Numerals Converter Application (Python Flask)


# Directory Tree

- Can be download from https://github.com/JBCodeWorld/aws-workshop.git

```text
.
├── Dockerfile
├── requirements.txt
├── roman-numerals-converter-app.py
├── static
│   └── styles
│       ├── master1CSS.css
│       └── master2CSS.css
└── templates
    ├── index.html
    └── result.html

3 directories, 7 files
```

# requirements.txt file
```text
flask
```



# Dockerfile contents

- Both of the `Dockerfile` files are working.

- Compare them

```text
FROM python:alpine
WORKDIR /app
COPY  . ./
ADD static static
ADD templates templates
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python"]
CMD ["roman-numerals-converter-app.py"]
```


```text
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
```



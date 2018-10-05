FROM python:3

WORKDIR /code

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

#ENV PATH "/code"
#CMD ["python", "../usr/local/bin/dispynode.py" && "python", "../usr/local/bin/dispynode.py" && "python", "main.py"]
#CMD ["python", "test.py" && "python", "main.py"]
#CMD [ "/bin/bash", "start.sh" ]
CMD ["ls"]
#CMD ["python", "./test.py" && "python","./main.py"]
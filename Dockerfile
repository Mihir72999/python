FROM faucet/python3
WORKDIR /app
COPY ./requirements.txt ./
RUN  pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
ENV MONGO_URI="mongodb+srv://mihir72999:Mihir72999@api.tv0cw9w.mongodb.net/data?retryWrites=true&w=majority"

CMD [ "python3",  "main.py" ] 







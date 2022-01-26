FROM node:14

WORKDIR /app

COPY . .

RUN npm install

EXPOSE 80

VOLUME ["/app/feedback"]

CMD ["node","server.js"]



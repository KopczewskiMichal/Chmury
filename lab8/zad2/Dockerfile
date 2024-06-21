FROM node:14-alpine

WORKDIR /usr/src/app

COPY ./app/package*.json ./

RUN npm install

COPY ./app/ .

EXPOSE 3000

# Uruchom aplikację
CMD ["node", "index.js"]

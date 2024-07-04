FROM node:14
WORKDIR /usr/src/app
COPY ./app/package*.json ./
RUN npm install
COPY ./app .
CMD [ "node", "app.js" ]
HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD curl -f http://localhost:3000/health || exit 1

FROM node

ENV NODE_ENV=production

WORKDIR /usr/src/app

COPY ./simpleServer/package.json ./simpleServer/yarn.lock ./

RUN yarn install --frozen-lockfile --production --silent

COPY ./simpleServer ./

EXPOSE 3000

RUN chown -R node /usr/src/app

USER node

CMD ["node", "index.js"]

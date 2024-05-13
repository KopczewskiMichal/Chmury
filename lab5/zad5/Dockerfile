FROM alpine

# Instalacja node.js, npm oraz yarn
RUN apk update && \
    apk add --no-cache nodejs npm && \
    npm install --global yarn && \
    rm -rf /var/cache/apk/*

# Ustawienie katalogu roboczego
WORKDIR /usr/src/app

# Skopiowanie plików pakietów i instalacja zależności
COPY ./simpleServer/package.json ./simpleServer/yarn.lock ./
RUN yarn install --frozen-lockfile --production --silent

# Skopiowanie pozostałych plików aplikacji
COPY ./simpleServer ./

# Zmiana właściciela katalogu na użytkownika "node"
RUN chown -R nobody:nogroup /usr/src/app

# Ustawienie użytkownika "nobody" jako użytkownika domyślnego
USER nobody

# Otwarcie portu 3000 i uruchomienie aplikacji
EXPOSE 3000
CMD ["node", "index.js"]

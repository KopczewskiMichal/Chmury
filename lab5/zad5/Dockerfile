FROM alpine as builder

# Instalacja node.js, npm oraz yarn
RUN apk update && \
    apk add --no-cache nodejs npm && \
    npm install --global yarn && \
    rm -rf /var/cache/apk/*

# Ustawienie katalogu roboczego
WORKDIR /usr/src/app

# Skopiowanie plików pakietów i instalacja zależności
COPY ./my-app/package.json ./my-app/yarn.lock ./
RUN yarn install --frozen-lockfile --production --silent

# Skopiowanie pozostałych plików aplikacji
COPY ./my-app ./
RUN yarn build

# # Zmiana właściciela katalogu na użytkownika "node"
# RUN chown -R nobody:nogroup /usr/src/app

# # Ustawienie użytkownika "nobody" jako użytkownika domyślnego
# USER nobody

# # Otwarcie portu 3000 i uruchomienie aplikacji
# EXPOSE 3000
# CMD ["node", "index.js"]



# Etap 2: Konfiguracja serwera nginx
FROM nginx

# Skopiowanie wynikowych plików aplikacji z pierwszego etapu
COPY --from=builder /usr/src/app/build /usr/share/nginx/html

# Konfiguracja serwera nginx do obsługi aplikacji
COPY ./default.conf /etc/nginx/conf.d/default.conf

# Otwarcie portu 80 i uruchomienie serwera nginx
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
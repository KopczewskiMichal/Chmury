FROM node

# Ustawiamy zmienną środowiskową NODE_ENV na "production"
ENV NODE_ENV=production

# Ustawiamy katalog roboczy w kontenerze
WORKDIR /usr/src/app

# Kopiujemy pliki package.json i yarn.lock do katalogu roboczego
COPY ./simpleServer/package.json ./simpleServer/yarn.lock ./

# Instalujemy zależności za pomocą Yarna
RUN yarn install --frozen-lockfile --production --silent

# Kopiujemy resztę plików aplikacji do katalogu roboczego
COPY ./simpleServer ./

# Deklarujemy port, który aplikacja będzie nasłuchiwać
EXPOSE 3000

# Nadajemy odpowiednie uprawnienia do katalogu roboczego
RUN chown -R node /usr/src/app

# Ustawiamy użytkownika node jako użytkownika, który uruchamia aplikację
USER node

# Uruchamiamy aplikację
CMD ["node", "index.js"]

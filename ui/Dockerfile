FROM node:14 as builder
WORKDIR /src/app/
COPY package*.json /src/app/
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /src/app/build /var/www/html

FROM node:14

WORKDIR /app

COPY package*.json ./
RUN npm install -g yarn
RUN yarn install

COPY . .

EXPOSE 3000
CMD ["yarn", "start"]

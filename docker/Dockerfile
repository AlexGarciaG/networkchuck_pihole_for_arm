FROM node:18-alpine
ENV ARCH=amd64
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
EXPOSE 3000
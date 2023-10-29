FROM node:18-alpine As development

WORKDIR /usr/src/app
COPY --chown=node:node package*.json ./
COPY --chown=node:node .env ./
RUN npm ci
COPY --chown=node:node . .
USER node

# Production build
FROM node:18-alpine As build
WORKDIR /usr/src/app
COPY --chown=node:node package*.json ./
COPY --chown=node:node --from=development /usr/src/app/node_modules ./node_modules
COPY --chown=node:node . .
RUN npx prisma generate
RUN npm run build
ENV NODE_ENV production
RUN npm ci && npm cache clean --force
USER node


# Production image
FROM node:18-alpine As production
COPY --chown=node:node --from=build /usr/src/app/node_modules ./node_modules
COPY --chown=node:node --from=build /usr/src/app/dist ./dist
COPY --chown=node:node --from=build /usr/src/app/package*.json ./
COPY --chown=node:node --from=build /usr/src/app/.env .env
COPY --chown=node:node --from=build /usr/src/app/prisma ./prisma
RUN npm i -g ts-node
CMD [ "npm", "run", "start:prod:migrate" ]

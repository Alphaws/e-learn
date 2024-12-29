FROM node:20-alpine AS build
WORKDIR /app
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
RUN npm install -g @angular/cli
COPY frontend .
ARG FE_CONFIG=development
RUN echo "FE_CONFIG=${FE_CONFIG}"
RUN ng build --configuration ${FE_CONFIG}

FROM nginx:stable-alpine AS serve
COPY --from=build /app/nginx.conf /etc/nginx/nginx.conf
COPY --from=build /app/dist/frontend/browser /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

FROM node:13.12.0 AS frontendbuild

COPY frontend/ /app/

WORKDIR /app
RUN npm install && npm run build

FROM python:3

COPY ./ /app
COPY --from=frontendbuild /app/dist /app/frontend/dist

WORKDIR /app
RUN pip install --user pipenv && /root/.local/bin/pipenv install

ENTRYPOINT [ "/root/.local/bin/pipenv", "run", "python","manage.py","runserver","0:8000" ]

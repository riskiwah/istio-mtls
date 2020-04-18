FROM python:3.5 AS build
COPY requirements.txt .
RUN pip install -r ./requirements.txt

FROM gcr.io/distroless/python3
COPY --from=build /usr/local/lib/python3.5/site-packages/ \
 /usr/lib/python3.5/.

WORKDIR /usr/src/app
COPY app.py app.py
CMD ["-m", "flask", "run", "--host", "0.0.0.0"]
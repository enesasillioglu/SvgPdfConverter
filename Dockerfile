FROM python:3

WORKDIR /usr/src/app

RUN pip3 install cairosvg
RUN pip3 install falcon

RUN mkdir -p /usr/share/fonts/
COPY fonts/* /usr/share/fonts/
RUN fc-cache -fv

COPY . .

CMD [ "python", "./converter.py" ]
FROM python:3.5.1

RUN groupadd killerapp && useradd --create-home --home-dir /opt/killerapp -g killerapp killerapp
WORKDIR /opt/killerapp

ADD src/ src/
ADD setup.py setup.py

RUN pip3.5 install .
RUN chown -R killerapp:killerapp /opt/killerapp

USER killerapp

CMD ["killer_app"]

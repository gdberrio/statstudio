FROM python:3.9
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /statstudio
COPY pyproject.toml pyproject.toml
RUN apt-get update -y
# necessary for pymc3
RUN apt-get install -y libhdf5-dev
RUN apt-get install -y libnetcdf-dev
RUN apt-get clean
RUN pip3 install --upgrade pip
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
COPY . /statstudio
EXPOSE 8000

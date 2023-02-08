# Pull base image

FROM python:3.10

# Set environment variables

ENV PYTHONDONTWRITEBYCODE 1

ENV PYTHONUNBUFFERED 1

# Set work directory

WORKDIR /PythonProjects

# Install dependencies

COPY Pipfile Pipfile.lock /PythonProjects/

RUN pip install pipenv && pipenv install --system

# Copy project

COPY . /PythonProjects/
 
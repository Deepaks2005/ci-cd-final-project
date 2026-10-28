# DevOps Capstone

[![Build Status](https://github.com/Deepaks2005/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/Deepaks2005/devops-capstone-project/actions/workflows/ci-build.yaml)

## Project Name

DevOps Capstone

## Description

This project is part of the IBM DevOps and Software Engineering course. It demonstrates a customer-account REST microservice, automated testing, code quality checks, and CI/CD pipeline automation using GitHub Actions and Tekton.

## Build Status

The badge above shows the status of the GitHub Actions CI pipeline for the `main` branch.

## Project Layout

- `service/` - Flask REST microservice and database model
- `tests/` - automated unit tests
- `.github/workflows/ci-build.yaml` - GitHub Actions CI pipeline
- `.tekton/tasks.yml` - Tekton cleanup and test tasks
- `requirements.txt` - Python dependencies
- `setup.cfg` - test, coverage, lint, and tool configuration

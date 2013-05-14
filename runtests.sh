#!/bin/sh
coverage erase
tox
coverage report
coverage html

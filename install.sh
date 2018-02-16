#!/usr/bin/env bash

PY_VERSION=${1:-'3.5'}
APP_NAME='pixel-monitoring'
ENVS_DIR=${2:-"/home/`whoami`/.envs"}
APP_ENV="${ENVS_DIR}/${APP_NAME}"
VENV='virtualenv'

print () {
    echo; echo $1; echo
}

# Check if script is running from the correct place
if [ -z "$(ls . | grep 'install.sh')" -o -z "$(ls . | grep 'requirements.txt')" ]; then
    print 'Please launch deploy script right from application root directory'
    exit 1
fi

# Check if correct python version is installed
if [ -z "$(which python${PY_VERSION} 2>/dev/null | grep -E "(/\w+)+/python${PY_VERSION}")" ]; then
    print "Seems like python${PY_VERSION} is not installed. Please install python${PY_VERSION} first."
    exit 1
fi

print "Installing virtualenv..."
if python${PY_VERSION} -m pip install virtualenv; then
    # Create vitrualenv for the app
    mkdir -p ${ENVS_DIR}

    if [ -d "${APP_ENV}" ]; then
        print "Cleaning old virtualenv..."
        rm -rf ${APP_ENV}
    fi

    print "Success. Creating virtualenv for ${APP_NAME}..."
    if python${PY_VERSION} -m ${VENV} -p python${PY_VERSION} ${APP_ENV}; then  # Being super-explicit

        # Upgrade pip
        ${APP_ENV}/bin/pip install --upgrade pip &>/dev/null

        print "Success. Installing ${APP_NAME} requirements..."
        # Install application and its dependencies under virtualenv
        if ${APP_ENV}/bin/pip install -r requirements.txt >install.log; then
            print "Application requirements installed."
        else
            print "Failed to install application, aborting."
            exit 1
        fi
    else
        print "Failed to create virtualenv, aborting."
        exit 1
    fi
else
    print "Failed to install virtualenv, aborting."
    exit 1
fi

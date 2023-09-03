#!/bin/bash

set -euo pipefail

make collectstatic
make migrate
make initadmin
make loaddata
make runserver-prod


#if [[ "$DJANGO_ENV" = "PRODUCTION" ]]; then
#else
#  make runserver
#fi
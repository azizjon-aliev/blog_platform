#!/bin/bash

set -euo pipefail

make collectstatic
make migrate
make initadmin
make loaddata


if [[ "$DJANGO_ENV" = "PRODUCTION" ]]; then
  make runserver-prod
else
  make runserver
fi
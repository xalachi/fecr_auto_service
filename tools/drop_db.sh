#!/bin/bash
BASE=$1

INSTANCE='local'
USER='odoo'

docker exec $INSTANCE\_db psql -d template1 -U $USER -c "
    SELECT pg_terminate_backend(pg_stat_activity.pid)
    FROM pg_stat_activity
    WHERE pg_stat_activity.datname = '$BASE'
    AND pid <> pg_backend_pid();
"
docker exec local_db dropdb -U odoo $BASE

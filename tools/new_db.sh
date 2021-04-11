#!/bin/bash
BASE=$1
NEW=$2
LOGIN=$3

INSTANCE='local'
USER='odoo'

docker exec $INSTANCE\_db psql -d template1 -U $USER -c "
    SELECT pg_terminate_backend(pg_stat_activity.pid)
    FROM pg_stat_activity
    WHERE pg_stat_activity.datname = '$BASE'
    AND pid <> pg_backend_pid();
"
docker exec $INSTANCE cp -r /var/lib/odoo/filestore/$BASE /var/lib/odoo/filestore/$NEW
docker exec $INSTANCE\_db createdb -U $USER -T $BASE $NEW
docker exec $INSTANCE\_db psql -d $NEW -U $USER -c "
UPDATE res_partner SET email = '$LOGIN' WHERE id = (SELECT partner_id FROM res_users WHERE login = 'user');
UPDATE res_users SET login = '$LOGIN' WHERE login = 'user';
"

import subprocess

# echo '*:*:*:odoo:odoo' > /var/lib/odoo/.pgpass
# chmod 600 /var/lib/odoo/.pgpass

PSQL_EXEC = "psql -h db -d template1 -tA -c"
ODOO_CONNECTION = "--db_host db --db_port 5432 --db_user odoo --db_password odoo --stop-after-init"
SELECT_DB = "SELECT datname FROM pg_database;"
EXCLUDED_BDS = {
    "postgres",
    "template0",
    "template1",
}
MODULES_TO_UPDATE = [
    "fecr",
    "fecr_auto_service",
]


def get_dbs():
    return (
        subprocess.run([*PSQL_EXEC.split(), SELECT_DB], stdout=subprocess.PIPE)
        .stdout.decode("utf-8")
        .splitlines()
    )


def process_db(db):
    return subprocess.run(
        [
            "odoo",
            *ODOO_CONNECTION.split(),
            "-d",
            db,
            "-u",
            ",".join(MODULES_TO_UPDATE),
            "--stop-after-init",
        ],
    )


def update_dbs():
    dbs = get_dbs()

    for db in dbs:
        if db in EXCLUDED_BDS:
            continue
        process_db(db)


if __name__ == "__main__":
    update_dbs()

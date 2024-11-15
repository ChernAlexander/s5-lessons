import logging

import pendulum
from airflow.decorators import dag, task

log = logging.getLogger('load_posgre_dag')


def say_hello(log: logging.Logger) -> None:
    log.info("Hello Worlds!!")


@dag(
    schedule_interval='0/15 * * * *',
    start_date=pendulum.datetime(2022, 5, 5, tz="UTC"),
    catchup=False,
    tags=['sprint5', 'example', 'hello_world'],
    is_paused_upon_creation=False
)
def load_postgre_dag():

    @task()
    def hello_task():
        say_hello(log)

    hello = hello_task()
    hello  # type: ignore
asdasda

hello_dag = load_postgre_dag()

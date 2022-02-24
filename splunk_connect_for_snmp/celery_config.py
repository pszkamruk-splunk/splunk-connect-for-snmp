#
# Copyright 2021 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Support use of .env file for developers
from contextlib import suppress

from kombu import Queue, Exchange

with suppress(ImportError):
    from dotenv import load_dotenv

    load_dotenv()


import os

MONGO_DB = os.getenv("MONGO_DB", "sc4snmp")
MONGO_DB_SCHEDULES = os.getenv("MONGO_DB_SCHEDULES", "schedules")

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_CELERY_DATABASE = os.getenv("MONGO_DB_CELERY_DATABASE", MONGO_DB)

# broker
broker_url = os.getenv("CELERY_BROKER_URL")
# results config
result_backend = MONGO_URI
result_extended = True
mongodb_backend_settings = {"database": MONGO_DB_CELERY_DATABASE}

beat_scheduler = "celerybeatmongo.schedulers.MongoScheduler"
mongodb_scheduler_url = MONGO_URI
mongodb_scheduler_db = MONGO_DB_CELERY_DATABASE

# Optimization for long running tasks
# https://docs.celeryproject.org/en/stable/userguide/optimizing.html#reserve-one-task-at-a-time
task_acks_late = True
worker_prefetch_multiplier = 1
task_acks_on_failure_or_timeout = True
task_reject_on_worker_lost = True
task_time_limit = 2400
task_create_missing_queues = False
task_ignore_result = True
result_persistent = False
result_expires = 60
default_exchange = Exchange('default', delivery_mode=1, type='x-consistent-hash')
task_queues = (
    Queue('traps', default_exchange, routing_key='1', durable=False),
    Queue('traps1', default_exchange, routing_key='1', durable=False),
)
task_default_exchange = 'default'
task_default_queue = 'traps1'
task_routes = {
    'splunk_connect_for_snmp.snmp.tasks.trap': {
        'exchange': 'default',
        'routing_key': '1'
    },
    'splunk_connect_for_snmp.splunk.tasks.send': {
        'exchange': 'default',
        'routing_key': '2',
    },
    'splunk_connect_for_snmp.splunk.tasks.prepare': {
        'exchange': 'default',
        'routing_key': '3'
    },
    'splunk_connect_for_snmp.enrich.tasks.enrich': {
        'exchange': 'default',
        'routing_key': '4',
    },
    'splunk_connect_for_snmp.inventory.tasks.inventory_setup_poller': {
        'exchange': 'default',
        'routing_key': '5'
    },
    'splunk_connect_for_snmp.snmp.tasks.poll': {
        'exchange': 'default',
        'routing_key': '6'
    }
}
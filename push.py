# from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
#
# registry = CollectorRegistry()
# g = Gauge('job_last_success_unixtime', 'Last time a batch job successfully finished', registry=registry)
# g.set_to_current_time()
# push_to_gateway('http://localhost:9091', job='batchA', registry=registry)

from prometheus_client import CollectorRegistry, Gauge, push_to_gateway, Histogram,  Info
from prometheus_client.exposition import basic_auth_handler


def my_auth_handler(url, method, timeout, headers, data):
    username = 'admin'
    password = 'admin'
    return basic_auth_handler(url, method, timeout, headers, data, username, password)


registry = CollectorRegistry()
g = Gauge('job_last_success_unixtime', 'Last time a batch job successfully finished', registry=registry)
g.set_to_current_time()

h = Histogram('request_latency_seconds', 'Description of histogram', registry=registry)
h.observe(4.7)    # Observe 4.7 (seconds in this case)

i = Info('my_build_version', 'Description of info', registry=registry)
i.info({'version': '1.2.3', 'buildhost': 'foo@bar'})

push_to_gateway('http://localhost:9091', job='Pushgateway', registry=registry, handler=my_auth_handler)

# import requests, os
# job_name='metrics'
# instance_name='10.0.0.1:9090'
# team_name='cpu'
# provider='Rpi'
# payload_key=os.system('ps –eo pid')
# payload_value=os.system('ps –eo %cpu')
#
# response = requests.post('http://localhost:9091/metrics/job/{j}/instance/{i}/team/{t}'.format(j=job_name, i=instance_name, t=team_name), data='{k} {v}\n'.format(k=payload_key, v=payload_value))
# print(response.status_code)
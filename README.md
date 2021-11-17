# Pebble

![Full screen](pebble.png)

Pebble is a stat's visualization tool, this will provide a skeleton to develop a monitoring tool.

- Prometheus: http://localhost:9090/graph
- Grafana: http://localhost:3000/

The combination of grafana and Prometheus is becoming a more and more common monitoring stack used by DevOps teams for storing and visualizing time series data. Prometheus acts as the storage backend and open source grafana as the interface for analysis and visualization.

Prometheus collects metrics from monitored targets by scraping metrics from HTTP endpoints on these targets.

# Getting Start:

We have deployed Prometheus and Grafana in Docker. (Note: Storing the Prometheus data to disk volue is yet to finish). 

```buildoutcfg
.
├── Makefile
├── README.md
├── docker-compose.yml
├── grafana
│   ├── config.ini
│   ├── dashboards
│   │   └── dashboard.json
│   └── provisioning
│       ├── dashboards
│       │   └── all.yml
│       └── datasources
│           └── all.yml
├── pebble.png
├── prometheus
│   ├── prometheus.yml
│   └── rules.yml
└── push.py
```

`docker-compose.yml` - starting configuration

`Make start` will start the container and the application will be exposed in the following urls

- Prometheus: http://localhost:9090/graph
- Grafana: http://localhost:3000/ The login by default is admin:admin.
- The metrics from the app: http://localhost:9001/metrics

`Make push` will push the data to `pushgateway` of metrics.

## Docs
PushGateWay Ref: https://github.com/prometheus/client_python#exporting-to-a-pushgateway

Grafana: https://grafana.com/tutorials/grafana-fundamentals/?utm_source=grafana_gettingstarted

Project Ref: https://github.com/Guardian-Development/yak/tree/main/yak-server/src/main/docker

Tutorial: https://levelup.gitconnected.com/metrics-reliably-configuring-prometheus-and-grafana-with-docker-2077541c8e6d

Push gateway Client: https://github.com/prometheus/client_python#exporting-to-a-pushgateway

`promhttp_metric_handler_requests_total` sample filter

Docker Ref: 
- https://levelup.gitconnected.com/metrics-reliably-configuring-prometheus-and-grafana-with-docker-2077541c8e6d
- https://gist.github.com/brunosimioni/2bcbb91edd4fbaeb8cccbbf490c5685c


# SRE aspects

## Services
All services are fully-managed by Google!

### Cloud Run
![](img/cloud-run-service.svg)
- Automatically scales up or down from zero to N depending on traffic, leveraging container image streaming for a fast startup time.

    Built to [rapidly scale out to handle all incoming requests](https://cloud.google.com/run/docs/about-instance-autoscaling). A service can rapidly scale up to one thousand container instances, or even more if you request a quota increase. If demand decreases, Cloud Run removes idle containers. If you're concerned about costs or overloading downstream systems, you can limit the maximum number of instances.
- Traffic management for application revisions

    Every deployment creates a new immutable revision. You can route incoming traffic to the latest revision, roll back to a previous revision, or split traffic to multiple revisions at the same time, [to perform a gradual rollout](https://cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration). This is useful if you want to **reduce the risk of deploying a new revision**. You can start with sending 1% of requests to a new revision, and increase that percentage while monitoring telemetry.
- Services are regional, automatically replicated across multiple zones.
- Out-of-the-box integration with Cloud Monitoring, Cloud Logging, Cloud Trace, and Error Reporting to ensure the health of an application.
- Each service gets an out-of-the-box stable HTTPS endpoint, with TLS termination handled for you.

    Every Cloud Run service is [provided with an HTTPS endpoint](https://cloud.google.com/run/docs/triggering/https-request) on a unique subdomain of the `*.run.app` domain – and you can configure custom domains as well. Cloud Run manages TLS for you, and includes support for WebSockets, HTTP/2 (end-to-end), and gRPC (end-to-end).
- Invoke and connect services with HTTP/1.*, HTTP/2, WebSockets, or gRPC (unary and streaming).

### Cloud SQL
- Easily scale up as your data grows—add processor cores, RAM and storage, and scale out by adding read replicas to handle increasing read traffic. Read replicas support high availability, can have their own read replicas, and can be located across regions and platforms.
- Data is encrypted when on Google’s internal networks and when stored in database tables, temporary files, and backups.
- Automate daily backups and binary logging
- Restore your instance to its state at an earlier point in time.

### Cloud Monitoring
- SLO monitoring
- Logging integration
- Alerting

## SLO/SLA/SLI

### SLA
Both service during the Term of the agreement under which Google has agreed to provide Google Cloud Platform to Customer (as applicable, the "Agreement"), the Covered Service will provide a Monthly Uptime Percentage to Customer of at least 99.95% (the "Service Level Objective" or "SLO"). 

### SLO
Known as Service Level Objective, is agreed upon objectives of how reliable a service is expected to be. It specifies a period of time in which the SLI is being measured. For example, 99% availability over a single day is different from 99% availability over a month. The first SLO would not permit more than 14 minutes of consecutive downtime (24 hrs * 1%), whereas the second SLO would allow consecutive downtime up to ~7 hours (30 days * 1%)."

Compliance period can be:
- **Calendar**: When you select Calendar as the Period Type, you also specify the Period Length, which can be a day, week or month. 
- **Rolling**: When you select Rolling as the Period Type, you also specify the number of days for the Period Length, for example, 30 days.

### SLI
Known as Service Level Indicator, is a metric over a period of time that informs about the health of a service and used to determine if SLOs are met.

- **AVAILABILITY**: How many requests have returned successfully, like `number of successful HTTP requests / total HTTP requests`
- **LATENCY**:How long does the application take to respond, like `number of HTTP requests that completed successfully in 200 ms / total HTTP requests`

### Error budget
The error budget for an SLO represents the total amount of time that a service can be noncompliant before it is in violation of its SLO. Thus, an error budget is `100% - SLO%`. For example, if you have a rolling 30-day availability SLO with a 99.99% compliance target, your error budget is 0.01% of 30 days: just over 4 minutes of allowed downtime each 30 days. A service required to meet a 100% SLO has no error budget

__Example__  
(Source: https://sre.google/workbook/implementing-slos/#proposed-slos-for-the-API)  
For example, over four weeks, the API metrics show:
- Total requests: 3,663,253
- Total successful requests: 3,557,865 (97.123%)
- 90th percentile latency: 432 ms
- 99th percentile latency: 891 ms

SLO for the API
| SLO type  | Objective  |
|---|---|
| Availability  | 97%  |
| Latency  | 90% of requests < 450 ms  |
| Latency  | 99% of requests < 900 ms |

Error budget over four weeks would be 3% of 3,663,253 (total requests) which equals to 109,897 bad requests
| SLO  | Allowed failures  |
|---|---|
| 97% availability  | 109,897  |
| 90% of requests faster than 450 ms  | 366,325  |
| 99% of requests faster than 900 ms  | 36,632 |

An SLO of **97% availability** allows a total of **109,897 bad requests** in a span of 4 weeks. 

__Microservice__
Current application stack is using `Cloud Run` which is configured with the default resource allocations and instance configuration. The cold start takes seconds which affects latency, that can be reduced with raising the [minimum instances](https://cloud.google.com/run/docs/configuring/min-instances) and [concurrency](https://cloud.google.com/run/docs/configuring/concurrency). Application `ping` endpoint can be set as ready health check for instances, it needs further development.

For better overview about the application also should done a performance test, to determine the base numbers for SLO and see where are the weak points and set error budget.
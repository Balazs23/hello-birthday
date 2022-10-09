# Deployment

Deployment process helps to ensure  and have the confidence that next deployment will be healthy. But deploying immediately to 100% of the traffic can be risky in the event something goes wrong. A best practice is to roll out changes gradually and observe any regressions or errors that might occur in the new version of the code.

## Pre-requisites
Always run tests before deploying any version of application into cloud environment, use `scripts/test.sh`. After the tests you can also build the same version with buildpacks as the `Cloud Build` does and run it with `scripts/start.sh`

## :blue_book: / :green_book: Gradual rollout

The way of "blue/ green" deployment. We’ll go gradually from the current revision (tagged "blue") to a new revision (tagged "green").

### :blue_book: Deploy current codebase
run command `scripts/preview.sh --deploy` to deploy current codebase as revision `BLUE` with 0% of live traffic. Every new deploy will be tagged as `GREEN`!

In this case, the application can be reach on specified `green--` url prefix, for an example run integration tests and check the current logs. Once this container has been vetted, it's time to push it to production.

### :vertical_traffic_light: Split traffic
run command `scripts/preview.sh --traffic 10` means, 10% of the live traffic will be routed to revision GREEN. We can now look at [Cloud Monitoring](https://cloud.google.com/monitoring), [Logging](https://cloud.google.com/logging) or [Error Reporting](https://cloud.google.com/error-reporting), filtering by revision to see if any new errors or latency show up.

Later we can increase the traffic to 20,30,40...100%!

### :red_circle: Rolling back
In case of errors, anytime before finalizing the deployment we can roll back to revision `BLUE` using command `scripts/preview.sh --rollback`. After fixing the application, we can start again with a deployment of the current codebase. Safety first!

### :green_book: Finalize deployment
After we are confidential of the new version of application running fine, we can set it as revision `BLUE` with command `scripts/preview.sh --production`

## Monitoring

Application also provides a "ping" endpoint, which can be used for at least for health check monitoring. This endpoint needs to be improved, like during request check the database is reachable or not.
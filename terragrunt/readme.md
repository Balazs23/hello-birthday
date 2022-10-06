# Infrastucture with terragrunt

## How do you deploy the infrastructure in this repo?

### Pre-requisites

1. Create or get GCP project parameters
1. Install [Terraform](https://www.terraform.io/) version `1.1.4` and
   [Terragrunt](https://github.com/gruntwork-io/terragrunt) version `v0.36.0` or newer.
1. Update the `bucket` parameter in the root `terragrunt.hcl`. We are using GCP [as a Terraform
   backend](https://www.terraform.io/language/settings/backends/gcs) to store
   Terraform state, and GSC bucket names must be globally unique. The name currently in
   the file is already taken, so you'll have to specify your own. Alternatives, you can
   set the environment variable `TG_BUCKET_PREFIX` to set a custom prefix.
1. Configure your GCP credentials using [gcloud CLI](https://cloud.google.com/sdk/gcloud).
    `source ../.project.env`
    `gcloud auth login`
    `gcloud config set project $GCP_PROJECT_ID`
    `gcloud auth application-default login`
1. Fill in your GCP Account ID's in `prod/account.hcl`

### Deploying a single module

1. `cd` into the module's folder (e.g. `cd non-prod/us-east-1/qa/mysql`).
1. Note: if you're deploying the MySQL DB, you'll need to configure your DB password as an environment variable:
   `export TF_VAR_master_password=(...)`.
1. Run `terragrunt plan` to see the changes you're about to apply.
1. If the plan looks good, run `terragrunt apply`.


### Deploying all modules in a region

1. `cd` into the region folder (e.g. `cd non-prod/us-east-1`).
1. Configure the password for the MySQL DB as an environment variable: `export TF_VAR_master_password=(...)`.
1. Run `terragrunt plan-all` to see all the changes you're about to apply.
1. If the plan looks good, run `terragrunt apply-all`.


### Testing the infrastructure after it's deployed

After each module is finished deploying, it will write a bunch of outputs to the screen. For example, the ASG will
output something like the following:

```
Outputs:

asg_name = tf-asg-00343cdb2415e9d5f20cda6620
asg_security_group_id = sg-d27df1a3
elb_dns_name = webserver-example-prod-1234567890.us-east-1.elb.amazonaws.com
elb_security_group_id = sg-fe62ee8f
url = http://webserver-example-prod-1234567890.us-east-1.elb.amazonaws.com:80
```

A minute or two after the deployment finishes, and the servers in the ASG have passed their health checks, you should
be able to test the `url` output in your browser or with `curl`:

```
curl http://webserver-example-prod-1234567890.us-east-1.elb.amazonaws.com:80

Hello, World
```

Similarly, the MySQL module produces outputs that will look something like this:

```
Outputs:

arn = arn:aws:rds:us-east-1:1234567890:db:terraform-00d7a11c1e02cf617f80bbe301
db_name = mysql_prod
endpoint = terraform-1234567890.abcdefghijklmonp.us-east-1.rds.amazonaws.com:3306
```

You can use the `endpoint` and `db_name` outputs with any MySQL client:

```
mysql --host=terraform-1234567890.abcdefghijklmonp.us-east-1.rds.amazonaws.com:3306 --user=admin --password mysql_prod
```


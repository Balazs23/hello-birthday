resource "google_sql_database" "database" {
  name     = var.database
  instance = google_sql_database_instance.instance.name
}

# See versions at https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance#database_version
resource "google_sql_database_instance" "instance" {
  name             = var.instance
  region           = var.region
  project          = var.project
  database_version = "POSTGRES_14"
  settings {
    tier = "db-f1-micro"
    database_flags {
      name  = "cloudsql.iam_authentication"
      value = "on"
    }
  }

  deletion_protection = "true"
}

resource "google_project_service" "sqladmin" {
  project = var.project
  service = "sqladmin.googleapis.com"

  timeouts {
    create = "30m"
    update = "40m"
  }

  disable_dependent_services = true
}

# create service account and grant permission for connection
resource "google_service_account" "service_account" {
  account_id = var.service_account_id
  project    = var.project
}

resource "google_project_iam_member" "sql_client" {
  project = var.project
  role    = "roles/cloudsql.client"
  member  = "serviceAccount:${google_service_account.service_account.email}"
}

resource "google_project_iam_member" "sql_instanceuser" {
  project = var.project
  role    = "roles/cloudsql.instanceUser"
  member  = "serviceAccount:${google_service_account.service_account.email}"
}

# add service account as user to database without ".gserviceaccount.com"
resource "google_sql_user" "sa_user" {
  name     = trimsuffix(google_service_account.service_account.email, ".gserviceaccount.com")
  instance = google_sql_database_instance.instance.name
  type     = "CLOUD_IAM_SERVICE_ACCOUNT"
}


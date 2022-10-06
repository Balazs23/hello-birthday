output "database" {
  value = google_sql_database.database.name
}

output "instance" {
  value = google_sql_database_instance.instance.name
}

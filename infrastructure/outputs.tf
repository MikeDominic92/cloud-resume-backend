output "website_bucket_url" {
  description = "The URL of the website bucket"
  value       = google_storage_bucket.website.url
}

output "function_url" {
  description = "The URL of the Cloud Function"
  value       = google_cloudfunctions_function.visitor_counter.https_trigger_url
}

output "firestore_database" {
  description = "The Firestore database details"
  value       = google_firestore_database.database.name
}

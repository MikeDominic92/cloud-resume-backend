terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.0"
    }
  }
  backend "gcs" {
    bucket = "cloud-resume-terraform-state"
    prefix = "terraform/state"
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

# Frontend Storage Bucket
resource "google_storage_bucket" "website" {
  name          = var.domain_name
  location      = var.storage_location
  force_destroy = true

  website {
    main_page_suffix = "index.html"
    not_found_page   = "404.html"
  }

  cors {
    origin          = ["*"]
    method          = ["GET", "HEAD", "PUT", "POST", "DELETE"]
    response_header = ["*"]
    max_age_seconds = 3600
  }
}

# Make bucket public
resource "google_storage_bucket_iam_member" "public_rule" {
  bucket = google_storage_bucket.website.name
  role   = "roles/storage.objectViewer"
  member = "allUsers"
}

# Cloud Function for visitor counter
resource "google_cloudfunctions_function" "visitor_counter" {
  name        = "visitor-counter"
  description = "HTTP Cloud Function to count website visitors"
  runtime     = "python39"

  available_memory_mb   = 256
  source_repository {
    url = "https://github.com/${var.github_owner}/${var.github_repo}"
  }

  trigger_http = true
  entry_point  = "visitor_count"

  environment_variables = {
    PROJECT_ID = var.project_id
  }
}

# Allow unauthenticated access to the function
resource "google_cloudfunctions_function_iam_member" "invoker" {
  project        = google_cloudfunctions_function.visitor_counter.project
  region         = google_cloudfunctions_function.visitor_counter.region
  cloud_function = google_cloudfunctions_function.visitor_counter.name

  role   = "roles/cloudfunctions.invoker"
  member = "allUsers"
}

# Firestore Database
resource "google_firestore_database" "database" {
  project                     = var.project_id
  name                       = "(default)"
  location_id                = var.region
  type                      = "FIRESTORE_NATIVE"
  concurrency_mode          = "OPTIMISTIC"
  app_engine_integration_mode = "DISABLED"
}

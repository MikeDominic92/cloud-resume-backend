variable "project_id" {
  description = "The GCP project ID"
  type        = string
}

variable "region" {
  description = "The default GCP region"
  type        = string
  default     = "us-central1"
}

variable "zone" {
  description = "The default GCP zone"
  type        = string
  default     = "us-central1-a"
}

variable "storage_location" {
  description = "The location for the storage bucket"
  type        = string
  default     = "US"
}

variable "domain_name" {
  description = "The domain name for the website"
  type        = string
}

variable "github_owner" {
  description = "GitHub repository owner"
  type        = string
}

variable "github_repo" {
  description = "GitHub repository name"
  type        = string
}

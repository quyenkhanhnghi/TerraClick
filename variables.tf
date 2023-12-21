variable "bucket_name" {
  default = "terraclick"
}

variable "region" {
  default = "us-east-1"
}

variable "image_files" {
  description = "A list of image files to upload to S3"
  type        = list(string)
  default     = ["weather.png", "rain.png", "wind.png", "humidity.png"]
}
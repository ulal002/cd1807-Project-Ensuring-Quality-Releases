# Resource Group/Location
variable "location" {}

variable "application_type" {}
variable "resource_type" {}
variable "resource_group_name" {
  type = string
  description = "The name of the resource group for the app service"
}

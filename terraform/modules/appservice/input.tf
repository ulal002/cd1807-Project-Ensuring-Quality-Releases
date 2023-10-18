# Resource Group/Location
variable "location" {}

variable "application_type" {}
variable "resource_type" {
  type    = string
  description = "Name of the Azure resource group"
}
variable "resource_group_name" {}

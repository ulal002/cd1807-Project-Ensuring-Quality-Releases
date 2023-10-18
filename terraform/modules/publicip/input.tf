# Resource Group/Location
variable "location" {}
variable "resource_group_name" {
  type    = string
  description = "Name of the Azure resource group"
}

variable "application_type" {}
variable "resource_type" {}

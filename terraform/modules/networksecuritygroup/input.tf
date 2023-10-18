# Resource Group/Location
variable "location" {}
variable "application_type" {}
variable "resource_type" {}
variable "resource_group_name" {
  type    = string
  description = "Name of the Azure resource group"
}
variable "subnet_id" {}
variable "address_prefix_test" {}

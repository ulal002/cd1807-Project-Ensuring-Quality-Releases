# Resource Group
variable "resource_group_name" {
  type    = string
  description = "Name of the Azure resource group"}
variable location {}
# Network
variable virtual_network_name {}
variable address_space {}
variable "application_type" {}
variable "resource_type" {}
variable "address_prefix_test" {}


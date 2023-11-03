provider "azurerm" {
  tenant_id       = "${var.tenant_id}"
  subscription_id = "${var.subscription_id}"
  client_id       = "${var.client_id}"
  client_secret   = "${var.client_secret}"
  features {}
  skip_provider_registration = true
}
terraform {
  backend "azurerm" {
    storage_account_name = "tfstate1338746"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
    access_key           = "VxHIHtqeyn9UN2SsC7qYGlUCB9XMYS26LKKioxvwCfKlG4+7UCuoDfLoRiLrb4b8rrkylws0nLjt+AStexIzSA=="
  }
}
module "resource_group" {
  source               = "../../modules/resource_group"
  resource_group_name  = var.resource_group_name
  location             = var.location
}

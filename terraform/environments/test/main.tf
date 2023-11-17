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
  resource_group_name  = "${var.resource_group_name}"
  location             = "${var.location}"
}
module "network" {
  source               = "../../modules/network"
  address_space        = "${var.address_space}"
  location             = "${var.location}"
  virtual_network_name = "${var.virtual_network_name}"
  application_type     = "${var.application_type}"
  resource_type        = "NET"
  resource_group_name  = module.resource_group.resource_group_name
  address_prefix_test  = "${var.address_prefix_test}"
  depends_on           = [module.resource_group]
}
module "nsg-test" {
  source           = "../../modules/networksecuritygroup"
  location         = "${var.location}"
  application_type = "${var.application_type}"
  resource_type    = "NSG"
  resource_group_name  = "${module.resource_group.resource_group_name}"
  subnet_id        = "${module.network.subnet_id_test}"
  address_prefix_test = "${var.address_prefix_test}"
}
module "appservice" {
  source           = "../../modules/appservice"
  location         = "${var.location}"
  application_type = "${var.application_type}"
  resource_type    = "AppService"
  resource_group   = "${module.resource_group.resource_group_name}"
}
module "publicip" {
  source           = "../../modules/publicip"
  location         = "${var.location}"
  application_type = "${var.application_type}"
  resource_type    = "publicip"
  resource_group   = "${module.resource_group.resource_group_name}"
}

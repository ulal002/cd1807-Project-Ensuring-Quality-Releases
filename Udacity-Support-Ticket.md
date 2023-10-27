##Error##
<img width="1725" alt="image" src="https://github.com/ulal002/cd1807-Project-Ensuring-Quality-Releases/assets/139964364/a8c59caf-52e6-4d93-9271-2dbe0b2f7967">

##Logs##
Starting: Terraform apply
==============================================================================
Task         : Terraform
Description  : Execute terraform commands to manage resources on AzureRM, Amazon Web Services(AWS) and Google Cloud Platform(GCP)
Version      : 3.209.24
Author       : Microsoft Corporation
Help         : [Learn more about this task](https://aka.ms/AAf0uqr)
==============================================================================
/home/urvesh/myagent/_work/_tool/terraform/1.2.9/x64/terraform providers

Providers required by configuration:
.
├── provider[registry.terraform.io/hashicorp/azurerm]
├── module.publicip
│   └── provider[registry.terraform.io/hashicorp/azurerm]
├── module.resource_group
│   └── provider[registry.terraform.io/hashicorp/azurerm]
├── module.appservice
│   └── provider[registry.terraform.io/hashicorp/azurerm]
├── module.network
│   └── provider[registry.terraform.io/hashicorp/azurerm]
└── module.nsg-test
    └── provider[registry.terraform.io/hashicorp/azurerm]

/home/urvesh/myagent/_work/_tool/terraform/1.2.9/x64/terraform apply -auto-approve
╷
│ Error: Invalid value for input variable
│ 
│   on main.tf line 29, in module "network":
│   29:   resource_group_name       = "${module.resource_group.resource_group_name}"
│ 
│ The given value is not suitable for module.network.var.resource_group_name
│ declared at ../../modules/network/input.tf:2,1-31: string required.
╵
╷
│ Error: Invalid value for input variable
│ 
│   on main.tf line 38, in module "nsg-test":
│   38:   resource_group_name   = "${module.resource_group.resource_group_name}"
│ 
│ The given value is not suitable for module.nsg-test.var.resource_group_name
│ declared at ../../modules/networksecuritygroup/input.tf:5,1-31: string
│ required.
╵
╷
│ Error: Invalid value for input variable
│ 
│   on main.tf line 54, in module "publicip":
│   54:   resource_group_name   = "${module.resource_group.resource_group_name}"
│ 
│ The given value is not suitable for module.publicip.var.resource_group_name
│ declared at ../../modules/publicip/input.tf:3,1-31: string required.
╵
╷
│ Error: Incorrect attribute value type
│ 
│   on ../../modules/appservice/appservice.tf line 4, in resource "azurerm_service_plan" "test":
│    4:   resource_group_name = var.resource_group_name
│     ├────────────────
│     │ var.resource_group_name is object with 6 attributes
│ 
│ Inappropriate value for attribute "resource_group_name": string required.
╵
##[error]Error: The process '/home/urvesh/myagent/_work/_tool/terraform/1.2.9/x64/terraform' failed with exit code 1
Finishing: Terraform apply

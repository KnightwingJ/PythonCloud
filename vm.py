import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-compute
# USAGE
    python virtual_machine_create_custom_image_vm_from_an_unmanaged_generalized_os_image.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():

    load_dotenv()
    subscription_id=os.getenv("595eaf3c-687f-419f-8dd3-35307403d329")
    resource_group_name=os.getenv("Lab4_2")
    vm_name=os.getenv("VM_NAME")
    admin_username=os.getenv("john")
    computer_name=os.getenv("COMPUTER_NAME")
    ssh_key=os.getenv("ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDmXp4J82fTo3GqZeoyVovjsJaux8UNYWlucQUJgu43il5Oc9HM2rPvZLrxwfFvcJ35KRg9o3Fg05nBxLNTFThvuFIEcQV7ANmfWydNrQa0iO57zCd52lc5l8KtBHICOFkNvf2p4Lh5kDz4QltFLbRI63Ngxr9RYkzZ7byT9iuDPhUyIgC33Khu/rabjDIbr0lsh1huIz7KgZILxzc7DUhlLWkbTEyaSCzu5e9rsuAIgwywEbiGR1jgXvicWEZ+FCmQ7CFEjURhMx5MOBjDwA9L9N9KoVQ4wWIG6GLkWr+1IQEFKWuqEiFuExcnYzSZ57DAoI8tCqNmuHGDyRkz0ce/W9VG6i6GITZwYSIGgu6dcT2CfUpgK3/MH1HcMxUIvAp9joASiIpNr4sW1LdAmX0beqTR1kixylQKiVDBO+ZhCkh1bxX/EEc/G8nupmJ7OehB4i6TdxCproYvUmzu6BfcRvKRsfhCkHNoYZaXe4DtV2ixGr8D/yFLKQBYgUO2110= generated-by-azure")
    nic=os.getenv("NIC")
    location=os.getenv("LOCATION")


    client = ComputeManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="595eaf3c-687f-419f-8dd3-35307403d329",
    )

    response = client.virtual_machines.begin_create_or_update(
        resource_group_name=resource_group_name,
        vm_name=vm_name,
        parameters={
                    "id": f"/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}",
                    "type": "Microsoft.Compute/virtualMachines",
                    "properties": {
                        "osProfile": {
                        "adminUsername": f"{admin_username}",
                        "secrets": [
                            
                        ],
                        "computerName": f"{computer_name}",
                        "linuxConfiguration": {
                            "ssh": {
                            "publicKeys": [
                                {
                                "path": f"/home/{admin_username}/.ssh/authorized_keys",
                                "keyData": f"{ssh_key}"
                                }
                            ]
                            },
                            "disablePasswordAuthentication": True
                        }
                        },
                        "networkProfile": {
                        "networkInterfaces": [
                            {
                            "id": f"/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkInterfaces/{nic}",
                            "properties": {
                                "primary": True
                            }
                            }
                        ]
                        },
                        "storageProfile": {
                        "imageReference": {
                            "sku": "16.04-LTS",
                            "publisher": "Canonical",
                            "version": "latest",
                            "offer": "UbuntuServer"
                        },
                        "dataDisks": [
                            
                        ]
                        },
                        "hardwareProfile": {
                        "vmSize": "Standard_D1_v2"
                        },
                        "provisioningState": "Creating"
                    },
                    "name":f"{vm_name}",
                    "location":f"{location}"
},
    ).result()
    print(response)


# x-ms-original-file: specification/compute/resource-manager/Microsoft.Compute/ComputeRP/stable/2023-07-01/examples/virtualMachineExamples/VirtualMachine_Create_CustomImageVmFromAnUnmanagedGeneralizedOsImage.json
if __name__ == "__main__":
    main()
import os
import subprocess
def createVM():
    # Name of the VM
    vname=input("Enter the name of your vm\n")
    # No of cpus allocated to the VM
    no_cpus=input("Enter the number of cpus dedicated to this\n")
    # Ram size of the VM
    ram_size=input("Enter the ram size\n")
    print("Creation of VM")
    list_dir = subprocess.Popen(["virt-install","--name",vname,"--description","Test VM with CentOS 7","--ram="+ram_size,"--vcpus="+no_cpus,"--os-type=Linux","--os-variant=rhel7","--disk","path=/var/lib/libvirt/images/"+vname+".qcow2,bus=virtio,size=10","--graphics","none","--location","/var/lib/libvirt/images/CentOS-7-x86_64-Minimal-1611.iso","--network","bridge:virbr0","--console","pty,target_type=serial","-x","console=ttyS0,115200n8 serial"])
    list_dir.wait()

    return

def commandsVM():
    # This function enters the selected guest VM and performs selected operations
    print("output of VM console")
    s = subprocess.Popen(["virsh","net-dhcp-leases","default"])
    s.wait()
    ip = input("enter the ip address of the guest vm: ")
    s2 = subprocess.Popen(["ssh","root@"+ip])
    s2.wait()
    for i in range(10000):
        continue

    return

def configurationVM():
    # This function configures vm
    vname = input("enter the name of the vm")
    v1 = subprocess.Popen(["virsh","dominfo",vname])
    v1.wait()
    return

def deleteVM():
    # This function deletes the vm
    print("Deletion of VM")
    vname=input("Enter the name of your vm for deletion\n")
    d = subprocess.Popen(["virsh","destroy",vname])
    d.wait()
    d1 = subprocess.Popen(["virsh","destroy",vname,"2>","/dev/null"])
    d1.wait()
    d2 = subprocess.Popen(["virsh","undefine",vname])
    d2.wait()
    d3 = subprocess.Popen(["virsh","pool-refresh","default"])
    d3.wait()
    d4 = subprocess.Popen(["virsh","vol-delete","--pool","default",vname+".qcow2"])
    d4.wait()
    return
def displayVM():
    # This function lists all the VMs present 
    list_all = subprocess.Popen(["virsh", "list", "--all"])
    list_all.wait()
    return


print("Select operation.")
print("1.Create VM")
print("2.Commands in VM")
print("3.Configuration VM")
print("4.Delete VM")
print("5.Display VMs")

while True:
    # Take input from the user
    print("Select operation.")
    choice = input("1.Create VM\n2.Commands in VM\n3.Configuration VM\n4.Delete VM\n5.Display VMs\nEnter choice(1/2/3/4/5):")	
    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5'):

        if choice == '1':
            createVM()

        elif choice == '2':
            commandsVM()

        elif choice == '3':
            configurationVM()


        elif choice == '4':
            deleteVM()

        elif choice == '5':
            displayVM()

    else:
        print("Invalid Input")
        continue

    res=input("Do you wish to continue y/n?")
    if(res!="y"):
        break

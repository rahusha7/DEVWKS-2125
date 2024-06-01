import os
import sys

intro = """
Welcome to DEVWKS-2125. Today, you are going to run a DNS application on Cisco IOS-XR. Let's get started!!
There are 6 steps to create an RPM. In order to execute each step, please press 'y'.

Are you ready? Press 'y' if yes.
"""

step1 = """
Step 1: The appmgr build scripts can be found on https://github.com/ios-xr/xr-appmgr-build. These scripts are utilized to generate an RPM.
        To generate an RPM for our application, it's necessary to clone this repository. Would you like me to proceed with this task for you?
"""

step2 = """
Step 2: Now, we must create a directory dedicated to our application, named 'bind9'. This directory will be housed within the 'xr-appmgr-build' 
        directory in the repository. Would you like me to proceed with creating this directory for you?
"""

step3 = """
Step3: We'll now include a compressed Docker image in this directory. Given that we're utilizing ubuntu/bind9 as our DNS server,we can conveniently 
       fetch this image from Dockerhub. After pulling the image, we'll generate a compressed version using the 'docker save' command. Would you 
       like me to do this step for you?
"""

step4 = """
Step 4: Once we have the compressed Docker image ready, we'll proceed to create a build.yaml file to define our build options. The build.yaml file 
        will include the following options:

        1. The name of our package, specified under the "name" field in the "packages" section. A single build.yaml file can define multiple 
           packages for installation.

        2. The "version" option allows us to assign a version tag to the built RPM.

        3. The "release" field should correspond to an entry in the "release_configs" directory. For instance, "ThinXR_7.3.15" is compatible with 
           most current IOS-XR router platforms, including those used in this workshop. To build applications for legacy IOS-XR routers, "eXR_7.3.1"
           must be specified.

        4. We need to specify the name and path to the Docker tarball under the "sources" field. The path specified is relative to the root directory
           of the xr-appmgr-build repository.

        5. [Optional] The "config-dir" and "data-dir" fields allow us to specify the name and path to the config directory and data directory, 
           respectively. In this example, we are not utilizing data or config directories. Once again, the path is relative to the root directory
           of the xr-appmgr-build repository.

        Shall I go ahead and create this yaml file for you?
"""

step5 = """
Step5: After the creation of our build.yaml file, we will proceed to incorporate configuration files tailored to our application. The ubuntu/bind9
       application relies on configuration files to define DNS options.

       The Devbox contains configuration files for this demonstration located in the /root/bind-configs/config directory. It is necessary to copy 
       these files to the xr-appmgr-build/bind9 directory.
"""

step6 = """
Step6: Once we have all our prerequisites ready, we will now create an RPM using 'appmgr_build' file in 'xr-appmgr-build' directory. Shall I create 
       an RPM for you?
"""


print(intro)

print()

#STEP1
print(step1)
user_input = input()
if user_input.lower() == 'y':
    os.system("git clone https://github.com/ios-xr/xr-appmgr-build.git")
else:
    print("Thanks for trying. Rolling back.")
    sys.exit(1)

print()

#STEP2
print(step2)
user_input = input()
if user_input.lower() == 'y':
    os.system("mkdir xr-appmgr-build/bind9")
else:
    print("Thanks for trying. Rolling back.")
    os.system("rm -rf ~/xr-appmgr-build")
    sys.exit(1)


print()
#STEP3
print(step3)
user_input = input()
if user_input.lower() == 'y':
    os.system('cd ~/xr-appmgr-build/bind9 && sudo docker pull ubuntu/bind9 && sudo docker save ubuntu/bind9 > bind.tar.gz')
else:
    print("Thanks for trying. Rolling back.")
    os.system("rm -rf ~/xr-appmgr-build")
    sys.exit(1)

print()

#STEP4
print(step4)
user_input = input()
if user_input.lower() == 'y':
    os.system(". ./config-bind.sh")
else:
    print("Thanks for trying. Rolling back.")
    os.system("rm -rf ~/xr-appmgr-build")
    sys.exit(1)

print()

#STEP5
user_input = input("Now you need to copy all the config files from ~/bind-configs/config to ~/xr-appmgr-build/bind9. Shall I proceed ahead?")

if user_input.lower() == 'y':
    os.system("cp -r ~/bind-configs/config ~/xr-appmgr-build/bind9")
else:
    print("Thanks for trying. Rolling back.")
    os.system("rm -rf ~/xr-appmgr-build")
    sys.exit(1)    

print()

#STEP6
print(step6)
user_input = input("")
if user_input.lower() == 'y':
    os.system("cd ~/xr-appmgr-build && ./appmgr_build -b bind9/build.yaml")
else:
    print("Thanks for trying. Rolling back.")
    os.system("rm -rf ~/xr-appmgr-build")
    sys.exit(1)


print("Congratulation")
<!-- Part of Corezoid docs. See docs/INDEX.md for full navigation. -->

## 4. Deployment Options
Virtualization Platforms notes

Corezoid is officially supported only on VMware (ESXi 6.5 or later) because VMware offers global, production-ready solutions optimized for marketplace deployments.

Other virtualization platforms (e.g., Hyper-V, KVM) are not officially supported due to limited use by enterprise clients and suboptimal production performance. However, converting Corezoid images for other virtualization platforms is possible.

Only RHEL 7 and CentOS 7 are officially supported for marketplace solutions, ensuring consistent performance and stability. Corezoid can run on other Linux distributions, such as CentOS 8, CentOS 9, Amazon Linux 2, and Amazon Linux 2023, but these are available only under specific agreements for production environments.


### 4.1 VMware
Requirements

Table 39: VMware requirements.


Deployment options

We offer two options of Corezoid Actor Engine deployment on VMware:

Deploying via OVF + VMDK

Attaching a disk image to a new virtual machine

Installation

Deploying via OVF + VMDK

Create a network: Click the Edit tab and in the dropdown list, select Virtual Network Editor.


Screenshot 280: VMware deployment.

In the upper-right corner of the Virtual Network Editor dialog, click Change Settings.
Note: You need to have the admin permission to change the configuration.

Screenshot 281: VMware deployment.

Click Add Network.

Screenshot 282: VMware deployment.

Select the network to add from the dropdown list.

Screenshot 283: VMware deployment.

Specify the subnet IP and mask, and click Apply.

Screenshot 284: VMware deployment.

Upload the previously downloaded ovf-image to the virtual machine: click the File tab and in the dropdown list, select Open.

Screenshot 285: VMware deployment.

Browse to the ovf-image file.

Screenshot 286: VMware deployment.

Specify the name for the new virtual machine.

Screenshot 287: VMware deployment.

Right click the uploaded image in the list on the left, and in the dropdown list, select Settings.


Screenshot 288: VMware deployment.

Before proceeding with the configuration of your virtual machine, make sure your hardware meets the minimum requirements (6 CPU cores, 10 GB RAM). To do that, select your virtual machine in the list, open the Settings menu on the Hardware tab.

Screenshot 289: VMware deployment.

In the Hardware list, select Network adapter, and in the adapter's settings select the network, which you've created in the Virtual network editor on the step 1. Click OK.

Screenshot 290: VMware deployment.

Select your virtual machine in the list and start it.

Screenshot 291: VMware deployment.

Enter the login.

Screenshot 292: VMware deployment.

Enter the password.

Screenshot 293: VMware deployment.

After logging in successfully, you see the Corezoid login screen.

Screenshot 294: VMware deployment.

Attaching disk image to new virtual machine

Requirements to the newly created virtual machine: 6 CPU cores, 10 GB RAM.

Launching

After installing the image, the IP address of the server is 172.16.0.254.

If necessary, you can change the IP address.
To change the web endpoint (domain or IP), you must run a script that is located in: /root/fix_domain.sh.
Web access: https://172.16.0.254 (or your value)
Web login: admin@corezoid.loc
Web password: Middleware2020-

SSH access:
Login: support
Password: corezoid
Get superuser by command: sudo -i

In case of having any questions, please do not hesitate to contact us: support@corezoid.com.


### 4.2 VMware Fusion
Requirements

Table 40: VMware fusion requirements.

Installation

Note: Before installing an image, make sure you have installed and activated a paid version of VMware Fusion. You won’t be able to deploy Corezoid on the Trial version of VMware Fusion.

Click VMwareFusion and in the dropdown list, select Preferences.

Screenshot 295: VMware fusion deployment.

In the Network dialog, click Network and add a new Network interface.

Screenshot 296: VMware fusion deployment.
Screenshot 297: VMware fusion deployment.
If you have troubles with setting Subnet IP and Subnet Mask parameters, go to Troubleshooting.

Create a new virtual machine: drag the .ovf file to the Select the Installation Method modal window.

Screenshot 298: VMware fusion deployment.

Select the existing virtual machine and click Continue.

Screenshot 299: VMware fusion deployment.

The installation starts.

Screenshot 300: VMware fusion deployment.

Click Customize Settings.

Screenshot 301: VMware fusion deployment.

In the menu, select Network Adapter.

Screenshot 302: VMware fusion deployment.

Select your network interface.

Screenshot 303: VMware fusion deployment.

Start up your virtual machine.

Screenshot 304: VMware fusion deployment.

Finish the deployment.

Screenshot 305: VMware fusion deployment.

Launching

A few minutes later, after the successful launch of the system, you can open a Corezoid in your browser.

Web access: https://172.16.0.254/ (or your value)
Login: admin@corezoid.loc
Password: Middleware2020-

SSH access:
Login: support
Password: corezoid
Get superuser by command: sudo -i

Additional Information

After the image is installed, the IP address of the server is 172.16.0.254.
Note: You can change the IP address if needed: run a script which is located in /root/fix_domain_crz.sh.

SSH access:
Login: support
Password: corezoid
Get superuser by command: sudo -i

Monitoring and restarting

You can also monitor and restart applications via the monit:

Output of all the monitoring processes: sudo monit status

Disabling monitoring of monit applications:monit unmonitor all

Enabling the monitoring:monit monitor all

If monit is used to start / stop the application, then stop / start the application using the monit commands:

monit stop conveyor_api_multipart

monit start conveyor_api_multipart

Troubleshooting

When starting the virtual machine, the following error appears.

Screenshot 306: VMware fusion VM start error.

Perform the following actions in the system security settings:

Go to the System Preferences tab, open the Security & Privacy, and click Allow.

Screenshot 307: VMware fusion troubleshooting.

If you get these errors when configuring the subnet, set the Subnet Mask to 255.255.255.0 and Subnet IP value to 172.16.0.0.

Screenshot 308: VMware fusion troubleshooting.

Change the Subnet Mask value to 255.255.255.192 and Subnet IP to 172.16.0.192.

Screenshot 309: VMware fusion troubleshooting.


### 4.3 Deploy Corezoid on Google Cloud Engine
To deploy Corezoid on Google Cloud Engine:

On the Corezoid Process Engine page, click Launch On Compute Engine.

Screenshot 310: Deployment on GCE.

Configure deployment options and click Deploy.

Screenshot 311: Deployment on GCE.

Wait until the deployment is complete.

Screenshot 312: Deployment on GCE.

Click the Menu icon and select Compute Engine -> VM instances.
Screenshot 313: Deployment on GCE.

Screenshot 314: Deployment on GCE.

Select the deployed Corezoid instance in the list.

Screenshot 315: Deployment on GCE.

Click Edit.

Screenshot 316: Deployment on GCE.

Scroll down to the Firewall section, then select the Allow HTTP traffic and Allow HTTPS traffic checkboxes.

Screenshot 317: Deployment on GCE.

Scroll down and click Save.

Screenshot 318: Deployment on GCE.

After the installation, you can get access to the installed Corezoid instance via the following link: https://<public_ip> (if your instance doesn't have a public_ip, you need to use your private IP: https://<private_ip>). E.g. https://34.89.217.248

Screenshot 319: Deployment on GCE.

Note: When first time logging in, you need to accept the self-signed SSL certificate in your browser. Then, you can log in to the Corezoid web interface using the following credentials:
Login: admin@corezoid.loc
Password: admin111

Screenshot 320: Deployment on GCE.

Useful info:

If you have issues with logging in to the Process, try updating your browser to the latest version or switching to the supported browsers: Chrome, Firefox or Internet Explorer/Edge.

If you want to use SSH, you may need to add a new login and public SSH Key in the settings of the Corezoid instance installed in the Google Cloud. For more information on SSH Keys management, go to this page.

Type "help" or "command /help" to find all the available commands for managing Corezoid.

If you have any questions, please do not hesitate to contact us: support@corezoid.com.


### 4.4 Deploy Corezoid on Azure Marketplace
To deploy Corezoid on the Azure Marketplace:

On the Corezoid Process Engine page, click Get it now.

Screenshot 321: Deployment on Azure Marketplace.

On the Corezoid Process Engine (preview) page, click the Create.

Screenshot 322: Deployment on Azure Marketplace.

Select the existing Resource group or create a new one.

Screenshot 323: Deployment on Azure Marketplace.

Create credentials for your SSH public key and click Next: Disks.

Screenshot 324: Deployment on Azure Marketplace.

Select the required Os disk type and click Next: Networking.

Screenshot 325: Deployment on Azure Marketplace.

Select the existing Virtual Interface or create a new one, and then, click Next: Management.

Screenshot 326: Deployment on Azure Marketplace.

(Optional) Select all the necessary settings or leave them as is, and click Review + create.

Screenshot 327: Deployment on Azure Marketplace.
Note: In the two optional tabs, Advanced and Tags, add settings if needed, and then click Review + create.

On the Review + create tab, check all the subscription details and click Create.

Screenshot 328: Deployment on Azure Marketplace.

Download the generated new SSH key pair to enter your instance via SSH after the deployment.

Screenshot 329: Deployment on Azure Marketplace.

The deployment process will be started and will take a few minutes.

Screenshot 330: Deployment on Azure Marketplace.

Review the deployment status on the screen.

Screenshot 331: Deployment on Azure Marketplace.

After the deployment completion, go to the created instance by clicking Go to resource in the upper-right corner of the page.

Screenshot 332: Deployment on Azure Marketplace.

On the resource screen, view all the Corezoid instance details and enter it via the public IP.

Screenshot 333: Deployment on Azure Marketplace.


### 4.5 Deploy Corezoid on AWS Marketplace
To deploy Corezoid on the AWS Marketplace:

Log in to your AWS account and go to the AWS Marketplace.

Choose Corezoid to deploy on your instance: go to the aws.com page and type Corezoid in the Search field.

Screenshot 334: Deployment on AWS Marketplace.

Note: you can browse through the categories (Categories->Financial Services, Vendors->Corezoid.com) to display the list of Corezoid options.

Screenshot 335: Deployment on AWS Marketplace.

Click Corezoid Actor Engine.

Screenshot 336: Deployment on AWS Marketplace.

Click Continue to Subscribe to start the subscription process.

Screenshot 337: Deployment on AWS Marketplace.

Review the terms and conditions of the subscription and click Accept Terms to proceed.

Screenshot 338: Deployment on AWS Marketplace.

Review the terms and conditions of the offer (product, effective and expiration date), and then click Continue to Configuration.

Screenshot 339: Deployment on AWS Marketplace.

Configure the launch settings, such as the fulfillment option, software version, and the region where you want to deploy your instance, and then click Continue to Launch.

Screenshot 340: Deployment on AWS Marketplace.

Before launching your Corezoid instance, configure its settings: launch action type, EC2 instance type, VPC settings, subnet settings, and security group settings.

Screenshot 341: Deployment on AWS Marketplace.

In the Security Group Settings dialog:

Leave the security group selected by default for newly created instances to configure it after the launch (see AWS documentation for more details).

Select the key pair you want to use for accessing your instance.

Click Launch.

Note: There are no key pairs created by default for new instances on AWS. Thus, you need to create a key pair for your instance (see AWS documentation for more details).

Screenshot 342: Deployment on AWS Marketplace.

You’ve successfully deployed and launched your Corezoid instance on AWS. Before it’s ready to be used you need to complete its configuration.
You can customize Corezoid based on your requirements. On the Corezoid Actor Engine dialog, you can:

View launch configuration details

View and configure your instance in the EC2 console (click to proceed with the configuration of your instance)

Launch the instance configuration again to start a new instance on AWS.

Screenshot 343: Deployment on AWS Marketplace.

To complete the instance configuration:

Open your instance in the AWS console by clicking EC2 console (or open AWS console-Instances).

Select the needed instance and check whether its state is Running.

Open the Security tab and click on the default security group to add the needed outbound security rules for the default group and open 22, 80, and 443 ports (For more information, go to AWS documentation).

Screenshot 344: Deployment on AWS Marketplace.

To configure access to your Corezoid instance from the website, the upper-right corner, click Connect.
Note: If you want to configure access to your instance from a local device, skip this step and proceed to the next one.

Screenshot 345: Deployment on AWS Marketplace.

On the EC2 Instance Connect tab, click Connect.

Screenshot 346: Deployment on AWS Marketplace.

To configure access to your Corezoid instance from a local device, add your key pair (For more information, go to AWS documentation for more details).

To complete your instance configuration, have the fix_domain command completed successfully in your terminal. See the example of a successful command run result below.

Screenshot 347: Deployment on AWS Marketplace.

Before logging in to Corezoid for the first time, accept the self-signed SSL certificate in your browser.

Log in to Corezoid using admin@corezoid.loc as login and ami-id of your Corezoid instance (For more information, go to Usage instructions). You can view and copy an ami-id for your instance in your AWS console.

Screenshot 348: Deployment on AWS Marketplace.



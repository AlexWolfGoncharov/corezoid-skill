<!-- Part of Corezoid docs. See docs/INDEX.md for full navigation. -->

## 2. Work Start and Core Concepts

### 2.1 Registration and Account Setup
To begin using Corezoid, follow these steps to register and set up your account:

Sign Up: Visit the Corezoid website and create an account using your email address.

Account Verification: Check your email for a verification link and confirm your registration.

Initial Configuration:

Workspace: Familiarize yourself with the Workspace, Activity Monitor, and Users & Groups tabs, Create button and toolbars.

API Keys: Generate API keys to enable system integrations and secure access.

Profile Settings: Customize your profile, language preferences, and notifications.

Diagram 2: Registration and configuration flow.

Screenshot 1: Illustration of the registration procedure and main dashboard view after logging in.


### 2.2 Interface Overview
Use Corezoid UI to manage workflows and monitor Processes through key features available in tabs and panel:

Screenshot 2: Corezoid main menu.

Workspace selection list: select a Corezoid Workspace.

Workspace tab: create and manage projects, Processes, dashboards, and State Diagrams.

Activity Monitor tab: get real-time info on task execution for the specified period broken down by Processes.

Users & Groups tab: view and manage users and user groups.

Docs: view the Corezoid documentation.

Notifications: view system notifications.

Profile: manage your profile.


### 2.2.1 Workspace tab
The Workspace is the tab for creating and managing your Corezoid objects, including Projects, Processes, and Dashboards. Here, you have the following items:

Screenshot 3: Workspace tab.

Search field: Enter a Process, Dashboard, or State Diagram name to find it in the current Workspace.

Create: Click to create objects depending on the currently selected Workspace. With the My Corezoid Workspace selected, you can select one of the items in the list to create the corresponding object.

Projects: Click to view all the Projects in the Workspace.

Folders: Click to view all the folders in the Workspace.

Aliases: Click to view all the Workspace-level aliases.

Shared with me: Open the list of objects shared with you by other users.

Recent: Open the list of the objects you've recently opened.

Starred: Open the list of favorite objects.

Trash: Open the recycle bin, where you can select objects to restore or delete permanently.

Workspace main window: View and manage your workspace objects here.

For more information on editing Processes and State Diagrams on the Workspace tab, go to Process Editor.

Screenshot 4: Create button menu for My Corezoid.

Process: Create a Process.

State Diagram: Create a State Diagram.

Dashboard: Create a Dashboard.

Folder:  Create a folder to store Processes, State Diagrams, Dashboards, aliases, API Keys, Projects.

Database: Create a database to use in the Database Call node.

From file: Select this item to upload a Process, State Diagram, Dashboard, or a folder with Corezoid objects stored in a JSON or a ZIP file to the currently selected Workspace.

With a user-created Workspace selected, you can select one of the items in the list to create the corresponding object:

Screenshot 5: Create button menu for user Workspace.

Project: Create a Project in the workspace.

From file: select this item to upload a Project stored in a ZIP file to the currently selected Workspace.


### 2.2.2 Activity Monitor
The Activity Monitor provides real-time visibility into system operations:

Task Execution: Monitor the status of active tasks.

Performance Metrics: Review throughput, latency, and other key performance indicators (KPIs) to optimize Processes.

Screenshot 6: Activity monitor tab.

On the Activity Monitor tab, you have the following:

Statistics: the window that shows the task processing statistics graph for the selected period.

Top 10 Processes: the window that shows ID, title, owner, and processed tasks count for the Processes with the highest task processing rate.

Filter: select the statistics sorting by

State changes

Tasks

Traffic (MB).

4. Statistics display range: select one of the following ranges for the statistics display on the tab:

Custom range: set the custom range.

Today.

Last 10 minutes.

Last hour.

Last 24 hours.

Last 7 days.

Last 30 days.

Previous hour.

Previous day.

Previous week.

Previous month.


### 2.2.3 Users & Groups Tab
On the Users & Groups tab, you can:

View info and manage users, user groups, and API keys in the Workspace.

View and manage users and user groups shared with you in the Workspace by other users.

Screenshot 7: Users & Groups tab.

On the Users & Groups tab, you have the following controls and tabs:

1. Create: click to create the following objects in the current Workspace

User: a profile used to log in and work in Corezoid.

API Key: a unique identifier used to authenticate requests made to an API

Group: users united in a group for an easier management.

Screenshot 8: Users & Groups Create menu.

2.   Users: Open the Workspace users list, where you can view each user's avatar, name, and login. You can:

View info for each user

Delete a user in the list.

Screenshot 9: Users & Groups tab - Users list.


## 3. API Keys: Open the Workspace API keys list, where you can:
Copy a key’s secret.

Delete a key in the list.

Screenshot 10: Users & Groups tab - API keys list.


## 4. Groups: Open the user groups list, where you can:
View the list of users included in the group by clicking the arrow near a group's name.

Specify the new owner for the group by clicking the change ownership icon.

Add users to the group by clicking the add user icon.

Rename the group by clicking the rename icon.

Delete the group by clicking the delete icon.

View the group user's info by clicking the info icon.

Delete a user by clicking the delete icon.

Screenshot 11: Users & Groups tab - Groups list.

5. Shared with me: Open the list of user groups shared with you by other users. Here, you can:

Add new users to shared groups by clicking the plus icon.

Delete users from groups by clicking the delete icon.

Screenshot 12: Users & Groups tab - Shared with me.


### 2.2.4 Docs Tab
You can access Corezoid documentation, including description of Processes, nodes and API using the Docs tab:

Screenshot 13: Docs tab.


Clicking the Docs tab redirects you to the Corezoid documentation portal, where you can:

Screenshot 14: Documentation portal menu.

Filter: enter a word or phrase to display only the documentation sections and subsections that match your search criteria. The filter instantly narrows down content as you type, helping you quickly locate relevant information.

Documentation structure: browse the documentation by clicking arrows to expand/collapse sections and access specific articles within sections and subsections.

Search: enter a phrase to view all articles and sections containing that phrase, then click to open the desired result.

Print: print the currently displayed article.

Share: share a link to the current article.

Theme: switch between dark and light color schemes.

Export: download the current article as a PDF file.


### 2.2.5 User Profile
The Profile page shows the user's email, account ID, personal information, and billing details. On the tabs of the Profile page, you can perform the following actions:

Profile: View and edit your profile information.

Billing: Check billing details and upgrade your license plan.

Dark mode: Change the platform UI display Light mode to the Dark mode by clicking the avatar and in the dropdown list, selecting Dark mode.

Log out: Log out from the platform by clicking the avatar and in the dropdown list, selecting Log out.

Screenshot 15: Profile menu.


#### View and edit your profile information
To view and edit your profile information:

In the upper-right corner of the page, click your avatar, and then in the dropdown list, select Profile.


Screenshot 16: Edit your Profile info.

On the Profile tab:

Click Choose file and upload a photo.

Enter a username in the Username field.

(Optional) Turn on the Enable Two-factor authentication toggle and follow the prompts in the dialog that appear to set the two-factor authentication.

Click Save.

Screenshot 17: Profile editing page.

Your profile information has been updated, and you can edit it anytime.


#### View and change your license parameters
To check your license details and change them:

In the upper-right corner of the page, click your avatar, and then in the dropdown list, select Billing.

Screenshot 18: Edit your Billing info.

On the Account Licenses & billing page, on the Licenses tab that opens, click an active license you want to upgrade. You can also buy a new license by clicking the Buy button in the right upper corner:

Screenshot 19: Upgrade your license or buy a new one.

On the Details tab of the open license, you can view the license parameters:

ID,

Type/Status

Price

Payment regularity

Payment method

Next payment date

Creation date

Expiration date

Storage space

Support level. 

Also, you can change and view the following license parameters:


Screenshot 20: Change your license parameters.


## 3.1 State changes: Increase your state changes by clicking Buy more.
A state change occurs when a task transitions between nodes. For example, a task passing through four nodes consumes three state changes. The formula for calculating state changes in a Process: SC = (N – 1) x T, where:
SC: number of state changes.

N: number of nodes in a Process.

T: total of tasks received in a Process.


## 3.2 State change statistics: View state change statistics on your license.
3.3 RPS: Change your current RPS by clicking Change.
RPS is the maximum number of tasks that can be processed across all Processes per second.
With 10 RPS license:

✓ 10 tasks/second: Successful processing

✗ 11 tasks/second: RPS limit reached error


## 3.4 Enter a comment.

## 3.5 Payment method: Change the payment method for the license by clicking Change.

## 3.6 Cancel license: Cancel the license by clicking Cancel. 
Note: This action is irreversible.
4. To view the license payment history, open the Payments tab:

Screenshot 21: Payments tab.

## 4.1 Search field: Search the payment by name or ID in the list.

## 4.2 Add filter: Click to add a search filter.
5. To view and change the users granted the license, open the Users tab:

Screenshot 22: Users tab.


## 5.1 Search field: Search the user by name or ID in the list.

## 5.2 Blocked/Active: Switch between active and blocked statuses of users granted the license by the license holder user. Blocking a user makes it impossible for the user to use the license. You can switch back to active to grant the user the license again.
6. To view the Dashboard on your license, open the Dashboard tab:
 
Screenshot 23: Dashboard tab.

### 2.2.6 Process Editor
To edit a Process or a State Diagram in the Process editor:

Open the Workspace Tab: Click the Process or State Diagram you want to edit.

Go to the Edit tab in the Process editor, you can use the following:

Edit Tab

On the Edit tab in the Process editor, you can use:

Screenshot 24: Process editor general panels

1. Process/State Diagram State Selection: Use the dropdown to toggle between Active, Paused, and Debug states:


Screenshot 25: Process state selection.


## 2. Deploy: Click to apply saved changes to the Process:
Screenshot 26: Process deployed indication.

3. Saved Indicator: Confirms all changes are auto-saved and ready for deployment.


## 4. View Tab: Switch to View mode to observe tasks.

## 5. Edit Tab (default): Switch to Edit mode to add or modify nodes.

## 6. Debug Tab: Use to track task movement step by step.

## 7. Undo: Undo recent actions.

## 8. Redo: Redo recent actions.

## 9. Errors: View Process or State Diagram errors.

## 10. Share: Manage sharing settings.

## 11. Task Parameters: Open the task parameters window.

## 12. Notifications: View notifications.

## 13. Three-Dot Menu: Click for additional options:
Screenshot 27: Three-dot menu.

History: View version history.

Info: View Process/State Diagram details.

Add Star: Mark as a favorite in the Workspace.

Move To: Relocate to a folder.

Make a Copy: Duplicate the Process/State Diagram.

Rename: Rename the Process/State Diagram.

Download: Save as a zip or JSON file.

Delete: Remove the Process/State Diagram.


## 14. Profile Menu:
Screenshot 28: Profile menu


## 15. Canvas: The main workspace to add, connect, and manage nodes.

## 16. Node Configuration Panel: Configure the selected node.

## 17. Nodes Panel: Add nodes to the canvas from the list.

## 18. Zoom in: zoom in on the canvas.

## 19. Zoom out: zoom out on the canvas.

## 20. Center: Center all nodes on the canvas.
View Tab

On the View tab, you have the following:

Screenshot 29: View tab controls.

Task search field: Search a task by REF.

New Task: Add a new task to the Process.

Import from CSV: Import a task from a CSV file.

For more details, see Working with Tasks.

Debug Tab

On the Debug tab, you have the following:

Screenshot 30: Debug tab controls.

New Task: add a new task to the Process in Debug mode.

Add breakpoint: click the icon and drag it to where you want to add a breakpoint for tasks in your Process.
Note: you can add breakpoints to the edges between nodes in your Process.

Add start point: click the icon and drag it to where you want to add a start point for tasks in your Process.
Note: you can add only one start point to your Process.

Repeat: repeat the last play - the movement of an added task from the start point to the nearest breakpoint.

Play: move an added task from the start point to the nearest breakpoint.

Rewind/back: rewind the last task movement.

Forward: move a task to the next breakpoint.

REF: view and change the task reference. Click the  icon to generate the new reference value automatically, or enter the value manually.

Code editor tab: switch to the code editor view of the current task content.

Add "key-value": click to add a key-value pair to the task.

Clear "values": clear values for all keys in the task.

Add task: click to add the task to the Process.

For more details, see Debugging a Process.


### 2.2.7 Sharing Settings Menu
You can use the Shared menu to share a Process or a State Diagram with new users or user groups, or change the existing sharing settings. To share with new users/user group, you need to invite them first:

Open a Process or a State Diagram in the Process editor.

Click the share icon to open the Sharing settings menu:

Screenshot 31: Sharing settings menu icon.


## 3. In the menu:
a. Enter the user/user group email or name.

b. Select the sharing permissions to be granted to the user/user group: View (view only), Task management (allow sending tasks), Modify (allow editing the Process or a State Diagram).

c. Select the Send notifications about update by email checkbox if you want the notifications on the sharing settings updates to be sent to the user/user group.

d. Click Send invitation.

Screenshot 32: Configuring share permissions and sending an invitation.

The invitation has been sent. After the user confirms the invitation in their email, they are redirected to the shared Process or a State Diagram with the set permissions.

To change the sharing settings:

Open the Sharing settings menu for the needed Process or a State Diagram.

Set the new permissions in the list.

Click Save.

Screenshot 33: Saving sharing changes.



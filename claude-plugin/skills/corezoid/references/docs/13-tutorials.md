<!-- Part of Corezoid docs. See docs/INDEX.md for full navigation. -->

## 8. Tutorials

### Google OAuth
Google OAuth 2.0 is an authorization protocol that allows a service (application) to be granted access rights to user resources on another service. The protocol can prevent an application to be entrusted with login and password data and grant only a restricted set of rights rather than all of them at once.

Before setting up Google OAuth 2.0, review Using OAuth 2.0 to Access Google APIs for essential background.

The general flow for setting up Google OAuth and Corezoid is the following:

Create a project on the Google Cloud Console.

Enable the Google OAuth API for your project.

Learn the requirements and flowchart for queries to Google APIs.

Create the OAuth 2.0 project folder in Corezoid.

Create Google credentials.

Obtain the Google code using your credentials.

Create the Corezoid process for generating the Google API access token.

Create and configure an API Call node in the token generation process.

Generate a Google API access token.

Create the Refresh token process for refreshing the Google API access token.

Configure token refresh.

Create and configure a state diagram for access token storage.


#### 1. Create project on the Google Cloud Console
Go to console.developers.google.com and in the upper-left corner, click Select a project.

In the Select a project dialog, click New project.

In the New Project dialog:

Enter your project name in the Project name field.

Select your project organization in the Organization dropdown list.

Select your project location in the Location dropdown list.

Click Create.

Your project has been created on the Google Cloud Console.


#### 2. Enable Google OAuth API
On the APIs & Services page, click + Enable APIs and services.

In the list of APIs, select Gmail API.

In the Gmail API dialog, click Enable.

Google OAuth API has been enabled.


#### 3. Learn requirements and flowchart for queries to Google APIs
All queries to Google APIs require authorization via the OAuth 2.0 protocol.
The flowchart below shows how Google services interact using OAuth 2.0.

Each request to API must contain the following parameters in the Header:
: Bearer {{ACCESS_TOKEN}}
where:
ACCESS_TOKEN authorizes queries and stores user details (such as user_id and user_role). It verifies your account before accessing the Google API.
Note: To reuse ACCESS_TOKEN across projects, use a unified storage process.

You can obtain ACCESS_TOKEN by adding the Set Parameters node in the following structure {{conv[process_id].ref[reference_of_request].name_of_the_parameter_the_ACCESS_TOKEN_is_located_in}}

For example: {{conv[4].ref[gmail].ACCESS_TOKEN}}
You need to create three unified processes in Corezoid to manage tokens:

Create Token: A process for generating the ACCESS_TOKEN via API calls.

Refresh Token: A process for refreshing the ACCESS_TOKEN.

Token Storage: A state diagram for storing and refreshing the ACCESS_TOKEN.

These processes will interact with Google OAuth 2.0, as shown in the figure below.

At his point, you have completed the Google project creation stage.


#### 4. Create OAuth 2.0 project folder in Corezoid
In the upper-left corner of your workspace page, click Create and in the dropdown list, select Folder.

In the Create folder dialog, enter the Google OAuth 2.0 folder name in the Title field and click Ok.

The Google OAuth 2.0 folder has been created.


#### 5. Create Google credentials
On the Credentials tab of the APIs & Services page, click + Create Credentials and in the dropdown list, select OAuth client ID.

On the Auth client ID page, click Configure consent screen.

On the Credential Type page, select Gmail API in the Select an API dropdown list, select User data, and click Next.

On the App information page, fill in all the required fields and click Save and continue.

(Optional) On the Scopes page, add scopes by clicking Add or remove scopes and click Save and continue.

On the OAuth Client ID page:

Select application type in the Application type dropdown list.

Enter an application name in the Name field.

Enter the redirect URI by clicking + Add URI.

On the Your Credentials page, download the credentials you've created and click Done.

Your Google credentials have been created and downloaded.


#### 6. Obtain Google Code
In your web browser, enter the following URL: https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=http://localhost:3000/auth/google/callback&response_type=code&access_type=offline&scope=https://mail.google.com&client_id=client_id
where:

redirect_uri: Is the redirect URI that you've entered at step 7 when creating credentials http://localhost:3000/auth/google/callback.

response_type: Is the code to obtain the code value (step 3).

access_type: Is used offline.

scope: Is the Google API you want to gain access to. As we use the Gmail API in this tutorial, the value is https://mail.google.com.
Note: You can find the list of available Google API scopes here.

client_id: Is the OAuth Client ID you've obtained when creating your Google credentials (step 8).

On the Google Account access confirmation page, click Allow.

On the Unable to connect page, copy and save the page URL to get the OAuth code.


#### 7. Create Process for Access Token Generation
On https://admin.corezoid.com/, open the OAuth 2.0 folder (that you've created) click Create, and from the dropdown list, select Process.

In the New process dialog:

Enter Create access token in the Title field.

Enter ACCESS_TOKEN generation process for using Google API in the Description field.

Click Ok.

The Create access token process has been created.


#### 8. Create and configure API Call node in token generation process
In the Create access token process, add the API Call node, which will call Google OAuth 2.0 API for generating ACCESS_TOKEN.

In the API Call node details panel:

Enter "https://oauth2.googleapis.com/token" in the URL field.

Select Default in the Request format dropdown list.

Select GET in the Request method dropdown list.

Select json in the Data format dropdown list.

Enter "application/json; charset=utf-8" in the Content-Type field.

Enter redirect_uri, grant_type, client_id, client_secret, and code in the Key fields.

Enter http://localhost:3000/auth/google/callback, authorization_code, {{client ID}}, {{client secret}}, and {{code}} in the Value fields.

In Other, select the Header parameters checkbox and add Authorization and Bearer {{conv[@config].ref[google].access_token}} in the Key and Value fields correspondingly.

To ensure automatic parameter entry upon manual request for ACCESS_TOKEN generation, add the credentials parameters to the process tasks:

In the upper-right corner of the process page, click the task parameters icon.

In the Task parameters dialog, click Add parameter, add the client_id, code, client_secret parameters and click Save.

The API Call you've configured is ready to request a call which will result in obtaining ACCESS_TOKEN from Google OAuth 2.0 API.


#### 9. Generate Google Access Token
In the configured Create access token process, send a new task: If ACCESS_TOKEN is successfully created, your request appears in the Final node. Click the node to view the request details, where the ACCESS_TOKEN is included as one of the parameters.


#### 10. Create Refresh token process
In your process folder, create a new process called Refresh token to configure the Google access token refresh.


#### 11. Configure token refresh
According to the Google OAuth protocol, the token expiration time is one hour, thus, you need to configure a Google API call for the token refresh.

In the Refresh Token process, add the Condition and API Call nodes.
Note:

The Condition node is required to forward a request to the API Call node for the token to be refreshed under the grant_type == refresh_token condition.

The API Call node is required to call Google API for a token refresh after this condition.

In the Condition node, add refresh_token receipt verification to the grant_type parameter.

In the API Call node details panel:

Enter https://oauth2.googleapis.com/token in the URL field.

Select Default in the Request format dropdown list.

Select POST in the Request method dropdown list.

Select json in the Data format dropdown list.

Enter "Application/X-Www-Form-Urlencoded" in the Content-Type field.

Enter refresh_token, grant_type, client_id, and client_secret in the Key fields.

Enter {{refresh_token}}, refresh_token, {{client_id}}, and {{client secret}} in the Value fields.

The process for ACCESS_TOKEN refresh has been created.


#### 12. Create and configure state diagram for access token storage
To avoid repeatedly calling the Create Token and Refresh Token processes for each Google API request, implement a mechanism to store and manage ACCESS_TOKEN. This approach will help optimize API calls and reduce latency. You can use a state diagram to illustrate the token lifecycle and management strategy.

On https://admin.corezoid.com/, open the OAuth 2.0 folder (that you've created above), click Create, and from the dropdown list, select State diagram.

In the Create state diagram dialog:

Enter Token storage in the Title field.

Enter Token storage process in the Description field.

Click Ok.

In the first Set State node details panel:

Change the default name to Active token.

Click Other, select the Maximum interval, for which the task stays in the node before being forwarded checkbox, enter 1 in the field below, and select Hour.
Note: According to the Google OAuth protocol, token expiration time is one hour.

Add the Copy Task node.

In the Copy Task node details panel:

Enter the Create/Refresh token name in the Add title field.

Enter the Create/Refresh token process in the Process field.

Enter {{root.ref}} in the Reference of the task copy field.

Select Default in the Request format dropdown list.

Enter refresh_token, grant_type, client_id, client_secret, and code in the Key fields.

Enter {{refresh_token}}, refresh_token, {{client_id}}, {{client secret}}, and {{code}} in the Value fields.

You create a request for ACCESS_TOKEN generation in the Create/Refresh Token process, and a copy of this request is sent to the Token storage state diagram. When it is time to refresh ACCESS_TOKEN during the Token storage process, the request will be passed through the Copy Task node for ACCESS_TOKEN refresh and wait for modification in the next Set State node.

In the Set state node details panel:

Change the default name to Waiting for the refreshed token.

Click + Condition and enter access_token == to check the presence of the access token parameter after the request modification.

Click Other, select the Alert if the number of tasks in the node queue reaches the following number checkbox, and enter 30 in the field below.

On the Set State node:

Click the plus icon next to access_token, add the Final node and rename it to Token is not refreshed.
Note: If an empty parameter is received, the request will be forwarded to the Token is not refreshed node.

Click the plus icon next to Tasks queued:30, add the Final node and rename it to Timeout refresh token.
Note: If a response is not received within 30 seconds, the request will be directed to the Timeout refresh token node.

Go to the Create/Refresh Token process in the Token storage state diagram and add the Copy Task node after the Create access token node.

In the Copy task node details panel:

Enter Save access and refresh token in the Add title field.

Add the Token storage diagram in the Process to which you want to copy the task field.

Enter gmail in the Reference of the task copy field.

Enter access_token, expires_in, code, client_id, and refresh_token in the Key fields.

Enter {{access_token}}, {{expires_in}}, {{code}}, {{client_id}}, and {{refresh_token}} in the Value fields.

In the Create/Refresh Token process add the Modify Task node after the Refresh access token node.

In the Modify task node details panel:

Enter Save access and refresh token in the Add title field.

Add the Token storage diagram in the Process to which you want to copy the task field.

Enter {{root.ref}} in the Reference of the task copy field.

Enter refresh_token, access_token, and expires_in in the Key fields.

Enter {{refresh_token}}, {{access_token}}, and {{expires_in}} in the Value fields.
Note:

refresh_token is a token to refresh ACCESS_TOKEN.

ACCESS_TOKEN is a token to access Google API.

expires_in is ACCESS_TOKEN expiration time.

Repeat the point of getting CODE and create a new request for ACCESS_TOKEN generation in the Create/Refresh Token process, thereby launching a process of the token storage and refreshing in the Token Storage state diagram.
Note: If ACCESS_TOKEN is created successfully, your request will be in the Active token state. Click it to review the request that contains access_token as one of its parameters.

Below, you can see the interaction of the Corezoid processes with the unified Token Storage state diagram and Google APIs.

You can use the ACCESS_TOKEN obtained in all the processes of your company to work with any Google APIs by adding it to the Header as follows:
Authorization: Bearer {{conv[DIAGRAM_ID].ref[REFERENCE].access_token}},
where:
DIAGRAM_ID is the ID of the Token storage state diagram.

To get the DIAGRAM_ID:

In the Token Storage state diagram, click the Edit mode.

Click the Start node of the state diagram and copy the number in the ID process value.

Example of Google API call via the API Call node using Google OAuth 2.0.



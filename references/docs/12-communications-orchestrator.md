<!-- Part of Corezoid docs. See docs/INDEX.md for full navigation. -->

## 7. Communications Orchestrator
Overview

Communications Orchestrator is a set of out-of-the-box Corezoid Processes for creating and managing bots in different messengers. Corezoid enables you to create universal Processes for managing business logic in different messengers instead of developing the business logic individually for each messenger.

Communications Orchestrator supports the following messengers:

Facebook Messenger

Viber

Telegram

Apple Messages for Business

Slack

Note: Whatsapp and Line are coming soon.


### Orchestrator Deployment Issue in On-Premise Environments
Orchestrator deployment doesn't work in on-premise environments. This feature is designed for Simulator cloud where orchestrator creation is a mass operation.

Workaround for using Orchestrator in on-premise environments:

Create orchestrator in Corezoid cloud environment.

Manually transfer it (Project with processes) to your on-premise environment for further development

Diagram 25: Communications Orchestrator architecture.

Here's the sequential flow of component interactions in Communications Orchestrator, from user input to response:

User sends a message via one of the messenger channels (Telegram, Viber, Facebook Messenger, Apple Messages)

Message Reception:

The corresponding Receiver Process captures the incoming message

Converts messenger-specific format into unified standard format with fields: channel, chat_id, event, message

Main Logic Processing:

Processes standardized message data

Checks events and user profiles

Creates/updates user profiles when needed

Routes messages to appropriate business processes

Router Operation:

Receives commands and messages from Main Logic

Identifies target Process based on command type

Routes requests to appropriate Process (Process 1, Process 2, Process n)

Controls and monitors business Process execution

Business Process Execution:

Specific Process handles the user request

Generates response data

Prepares data for sending back to user

Send Message Processing:

Receives output from business processes

Converts unified message format to messenger-specific format

Manages message formatting and attachments

Applies localization if needed

Sends formatted messages back to the appropriate messenger channel

User Receives Response:

Message is delivered through the original messenger channel

Displayed to user in the messenger interface

Supporting Components Throughout Flow:

User Profile: Stores and manages user data

System Diagram: Maintains system configuration

Commands: Manages available bot commands

Attachments: Handles file and media processing

Localization: Provides multi-language support

Tokens: Manages messenger authentication tokens


## Creating Bots in Messengers and Connecting Them to Your Communications Orchestrator
A bot in Corezoid represents a separate project, which is created from scratch following a simple procedure:

Step 1. Create bots in messengers:

Telegram

Viber

Facebook Messenger

Apple Messages for Business

Step 2. Connnect bots to Communications Orchestrator in Corezoid

You can connect Communications Orchestrator to new or earlier created messenger bots.

Step 1. Create bots in messengers

Communications Orchestrator accesses bots in the messengers using HTTP API with token identification. A token is a key for accessing your bot. Anyone who possesses this key can control your bot. The token storage and access to it must comply with security requirements for sensitive data.

To connect an existing bot to Communications Orchestrator, go to step 2. Connect bots to Communications Orchestrator in Corezoid.

Telegram

Begin a chat with BotFather and click Start.

Send the /newbot command to BotFather to create a new bot.

Follow the BotFather’s instructions:

Name your bot.

Give your bot a username to be displayed in contacts, chats, and addresses.
Note: A username must have the bot ending, for example, TetrisBot or tetris_bot. The name and username of a bot must be unique in Telegram.

Save the provided access token to your bot.

Viber

Follow the contact form link to submit your application for a Viber bot registration. Our Support team will guide you through the procedure and provide all the necessary information.

Facebook Messenger

Log in to your Facebook account.

Create a new page that your bot will be connected to by following the instructions.
Note: You must connect each Facebook bot to a Facebook page.

Go to Facebook for Developers.
Note: If you are new here, register as a developer.

Hover over My Apps, and then click Create New App.

In the Create a New App ID dialog, fill in all the fields and click Create App ID.

Screenshot 362: Create a Facebook messenger bot.

Click the app creation icon.

Screenshot 363: Create a Facebook messenger bot.

On the left navigation panel, click Dashboard, and in the Add a Product list, find Messenger and click Set Up below.

Screenshot 364: Create a Facebook messenger bot.

In the Page dropdown list of Access Tokens on the Messenger Settings page, select Edit Permission.
Note: This is the page you created in step 2.

Screenshot 365: Create a Facebook messenger bot.

In the new browser dialog, click Continue as [Your Profile Name] to confirm assigning your bot to your Facebook account.

Screenshot 366: Create a Facebook messenger bot.

In the next dialog, select the checkbox of the page your bot will be attached to and click Next.
Note: This is the page you created in step 2.

Screenshot 367: Create a Facebook messenger bot.

In the next dialog, set the toggle for your page to YES to allow your bot to participate in the P2P chats in the messenger and click Done.

Screenshot 368: Create a Facebook messenger bot.

In the next dialog, click Ok.

Screenshot 369: Create a Facebook messenger bot.

In the Page Access Token field, copy and save the access token.

Screenshot 370: Create a Facebook messenger bot.

Step 2. Connect bots to Communications Orchestrator in Corezoid

Go to admin.corezoid.com, open the Workspace tab, and click the Projects folder.

Select the needed stage, create a new project, or open an existing one.
Note: To create a Communications Orchestrator project, choose a non-immutable stage.

In the upper-left corner, click Create and from the dropdown list, select Orchestrator.

Screenshot 371: Create Communications Orchestrator.

In the Communications Orchestrator dialog:

Select the messengers you want to integrate.

Paste the access token you copied when creating the bot

Click Next.

Screenshot 372: Messenger selection dialog.

Note:

If the connection procedure didn’t succeed, check each token to be valid.

If you connect Facebook Messenger, you need to subscribe to Facebook Webhooks in the Facebook admin panel. For more information, go to Subscribe to Facebook Webhook.

In the dialog, click Open the created Bot to open the Communications Orchestrator folder.

The bot is connected to the Communications Orchestrator folder, and you can start working in the folder. For more information, go to Components.

Screenshot 373: Communications Orchestrator folder.

Subscribe to Facebook Webhook

When you select other messengers, these steps are done automatically.

Go to your Facebook app’s page for developers.

Copy your access token created above Facebook Messenger, step 14).

In the Communications Orchestrator dialog of Corezoid, click Copy under the Webhook URL for Facebook Messenger.

Screenshot 374: Facebook Messenger token copy.

In the left navigation panel, go to Messenger > Settings and click Subscribe to Events.

Screenshot 375: Facebook Messenger account settings.

In the New Page Subscription dialog:

Enter the copied Webhook URL in the Callback URL field.

Enter the copied token in the Verify Token field.

Select the messages, messaging_postbacks, and messaging_optins checkboxes.

Click Verify and Save.

Screenshot 376: Facebook Messenger subscription settings.

In the Select a Page dropdown list of the Webhooks page, select the page to which your page will be subscribed for events and click Subscribe.

Screenshot 377: Facebook Messenger Webhooks section.

You’ve created your first Communications Orchestrator.

Create Communications Orchestrator

Create a bot for one or multiple messengers you plan to use with Communications Orchestrator and save the access token for that/those messenger(s).

Create a Communications Orchestrator project in Corezoid.
Note: For more information on creating a project, go to Project.

Add the Git Call node to your account:

Go to Messengers → Simulator → API → upload → git call - simulator - upload - Upload file.

Click the Git Call node and click Build.

In the upper-right corner, click Deploy.

Screenshot 378: Git Call predefined code build.

The project folder with main components located in Projects > Stages > develop > Communications Orchestrator stores the following required basic Processes and functionality:

Viber/Telegram/Facebook Receiver Process

Main Process

Event types

Router Process

Send Message Process

Configs folder

Messengers > Simulator

Account components

Screenshot 379: Contents of the created Communications Orchestrator folder.

Receiver Process

The Viber Receiver, Telegram Receiver, Facebook Receiver, ABC Receiver (Apple Business Chat), Slack Receiver Processes are located in the corresponding messenger folders: Projects > Stages > Communications Orchestrator > Messengers > [Messenger Name].

Screenshot 380: Communications Orchestrator Messengers subfolders.

The Receiver Processes are the work starting points of each bot: a [messenger name] Webhook connects to the [same-messenger-name] Receiver Process during Communications Orchestrator creation.
The Receiver Processes perform the following actions:

Receive events (messages and files sent, buttons clicked, links followed, and so on) from users.

Convert received data into the unified standard data structure:

channel – the message channel. Available options: telegram, facebook, viber, and abc.

chat_id – identifier of a chat, user, and so on.

event – event type.

message – message object.

Forward the converted data to the Main Process.

To attach another bot to an existing project in Communications Orchestrator, connect a webhook of this bot to the corresponding Receiver Process manually:

Click the corresponding [Messenger name] Receiver Process and in the upper-right corner, click View details.

Screenshot 381: Telegram Receiver Process.

On the Webhook tab of the selected [Messenger name] Receiver Process details panel, click Connect to messenger.

Screenshot 382: Telegram Receiver Process webhook.

In the Connect to messenger dialog:

Select the needed messenger.

Screenshot 383: Connect to messenger.


Note: you can connect multiple bots in all the supported messengers to your Communications Orchestrator anytime by changing the settings in your Communications Orchestrator project.

Enter an access token to the new bot in the text box field and click OK.

Screenshot 384: Connect to messenger token input.

Update the token in the Tokens state diagram.

Note: The Task REF should have the token name.

The Webhook is connected to the Receiver Process, and the bot is attached to the selected Process in Communications Orchestrator.

Main Process

The Main Process receives the converted data from the messengers and runs the initial business logic of the bot before routing tasks to sub-Processes.
Input JSON example

{

"channel": "viber",

"chat_id": "12312321",

"event": "message",

"message": {

"type": "text",

"text": "Lorem ipsum..."

}

}

Incoming data parameters to the Main Process


Screenshot 385: Incoming data parameters to the Main Process.

Event types

Examples of data transmission using context:

Viber: viber://pa?chatURI={{public_account_name}}&context={{params}}

Facebook Messenger: http://m.me/{{bot_name}}?ref={{params}}

Telegram: https://telegram.me/{{bot_name}}?start={{params}}

Event Types Overview 

The system processes four main types of events:

start - Triggered when:

User connects to the bot for the first time

In Viber - each time chat dialog is opened

Used for initial user setup and welcome messages

context - Triggered when:

Incoming message has additional context parameters

Used with deep links and reference parameters

Can be used for campaign tracking or specific scenario initialization

message - Triggered when:

User sends any type of message

Main event type for regular user interactions

command - Triggered when:

User sends a message in /commandName format

Used for specific bot function activation

Context Data Transmission Examples: Each messenger has its specific format for passing context:

Viber:

viber://pa?chatURI={{public_account_name}}&context={{params}}

Facebook Messenger:

http://m.me/{{bot_name}}?ref={{params}}

Telegram: 

https://telegram.me/{{bot_name}}?start={{params}}

Typical Processing Logic:

For start events:

User profile creation

Welcome message sending

Initial bot menu presentation

Setting up user preferences

For context events:

Parameter extraction and validation

Specific scenario activation

Campaign tracking

Deep link processing

Special offer activation

For message events:

Message type identification

Content processing

Response generation

User state management

Dialog flow control

For command events:

Command validation

Permission checking

Function execution

Response formatting

State updates

Common Use Cases:

Marketing Campaigns:

Using context parameters for tracking sources

Activating special offers

Campaign-specific flows

User Authorization:

Initial user registration

Session management

Access control

Multi-step Processes:

State management

Progress tracking

Process continuation

Feature Access:

Command-based feature activation

Permission validation

Feature-specific flows

Event Processing Pattern:

{

"channel": "viber", // messenger type

"chat_id": "12312321", // unique user identifier

"event": "message", // event type

"message": {

"type": "text",

"text": "..."  // event content

}
}

Integration Points:

With User Profile:

Profile creation and updates

User preferences storage

State management

With Router:

Event routing to appropriate handlers

Process selection

Flow control

With Main Process:

Business logic execution

Response generation

State transitions

Router Process

The Router Process implements the main logic of processing Communications Orchestrator events. All the event types can be processed here.

Diagram 26: Router Process flow.

Router Process Overview


1. Router Process Core Function:

Serves as the main logic implementation for processing Communications Orchestrator events

Handles all event types centrally

Coordinates message flow and command execution

Main Process Flow:

Starts with getting user's last command

Proceeds to current message check

Has two key conditions branches based on message type:

Message equals command with non-empty last command

Message equals command with empty last command

Core Decision Points:

Check Current Message

Validates incoming message content

Determines message type and format

Routes based on message characteristics

Check Other Conditions

Evaluates additional routing criteria

Handles special cases

Manages Process flow control

Command Processing:

When command detected:

Gets Process ID by command

Sends task to the Process by process_id

Sets last state and command

Saves user's last state and command

When no command:

Routes to appropriate handler

Maintains Process continuity

Manages state transitions

Exit Handling:

Special /exit command processing

Deletes callback from last Process

Provides clean exit from current Process

Returns to main menu state

End States:

Two main termination paths:

/exit path: Cleanup and return to main menu

/end path: Complete current Process and send main menu

Integration Points:

With User Profile:

User state management

Preference tracking

Session handling

With Commands:

Command validation

Process ID lookup

Command execution

With Last Active Process:

Process state management

Callback handling

Process transitions

Output Handling:

Manages message sending to users

Handles localization requirements

Manages attachments

Coordinates with appropriate messenger APIs

Send Message Process

The Send Message Process is responsible for sending messages to users. It receives text templates, attachments, and argument values to compose them together dynamically into a single ready-for-sending message and does message localization.

Diagram 27: Send Message Process flow.

Send Message Process Overview

Process Overview:

Responsible for sending messages to users across different messaging platforms

Handles message localization and attachment processing

Manages both standard and dynamic message attachments

Distributes messages to specific platform endpoints (Viber, Telegram, Facebook, etc.)

Core Process Flow:

A. Initial Setup:

Starts with gathering user information

GET user's language from User Profile

Retrieves localized texts from Localization store

Obtains localized attachments from Attachments store

B. Content Processing:

GET localized texts - pulls appropriate language versions

GET localized attachments - retrieves platform-specific attachment formats

Check attachment type - determines if Standard or Dynamic

C. Attachment Handling:

Two distinct paths based on attachment type:

Standard: Direct replacement of variables

Dynamic: Creates dynamic attachments with additional processing

Merges back into main flow after processing

Key Components Integration:

User Profile Integration:

Language preferences

User settings

Personalization data

Localization System:

Text content in multiple languages

Message templates

Error messages

Attachments Management:

Button templates

Rich media content

Interactive elements

Platform-Specific Distribution:

Separate handlers for each platform:

Send Message to Viber

Send Message to Telegram

Send Message to Facebook

Send Message to Sender (generic)

Variable Processing:

Replace variables in texts/attachments:

User-specific data

Dynamic content

System variables

Contextual information

Dynamic Attachment Creation:

Handles complex attachment types

Processes templates

Generates interactive elements

Manages carousel and list formats

Key Features:

Multi-language support

Platform-specific formatting

Dynamic content generation

Template processing

Variable substitution

Error handling

Message Delivery:

Platform-specific API integration

Delivery confirmation

Error handling and retries

Rate limiting compliance

Table 48: Send message parameters.
 
Input JSON Example

{

"channel": "viber",

"chat_id": "12345...",

"text_id": "main_text",

"attachment_id": "main_keyboard"

}

Input JSON Example (Dynamic attachment)

{

"channel": "viber",

"chat_id": "12345...",

"text_id": "exchange_rates",

"attachment_id": "carousel_pattern",

"items": [{

"name": "AED",

"value": 4.283634

},

{

"name": "AFN",

"value": 85.711652

},

{

"name": "ALL",

"value": 126.118624

},

...

"currentPage": 1

}

Configs folder

To store data, Communications Orchestrator has the following State Diagrams in the Configs folder:

User Profile: Users’ profiles received from bots.

Chats - by userId: Saved dialogs with userId reference.

Chats - by eventId: Saved dialogs with eventId reference.

Attachments:Templates of message attachments are stored in JSON.

Tokens: Access tokens to bots in messengers and credentials for integration with the Simulator.

Localization: Texts for content localization.

Simulator Cache: Cache of the main Simulator entities for quick access.

Screenshot 386: Configs folder.

The Communications Orchestrator Processes interact with the State Diagrams using the dynamic construction for data receiving.

User profile

This User Profile State Diagram stores user data. When a user refers to the bot for the first time, a new user profile is created; then the profile is updated in future activities. A task with user data is created and edited in the Main Process using a reference of the strict template:

{{channel}}_{{chat_id}},
where:

channel is the name of a messenger a user referred from.

chat_id is a unique user identifier in the messenger.

Example: viber_2yOPxC85DSpJCJHpYzjqTw=

As the channel and chat_id parameters are required in all the Communications Orchestrator Processes, the user data can be received and edited at any step.

Attachments

Messengers support various attachments to messages, such as buttons, keyboards, carousels, and so on. The Attachments State Diagram stores templates in JSON format for various attachment types, such as buttons, keyboards, carousels, and lists. These templates are used to dynamically construct and send interactive messages to users.

 
Diagram 28: Attachments scheme.

When adding an attachment to the State Diagram, it is recommended to specify the name of the Task Reference according to the target action for which this attachment will be used. For example:

mainMenu for displaying the Main menu

exit for a button to exit the current Process

This value is given in the attachment_id parameter when sending a message to a user.

To send a message with an attachment to a user, a bot uses the following logic:

The Send Message Process uses the dynamic construction {{conv[{{attachment_state_diagram_id}}].ref[{{attachment_id}}]}} to receive an object that describes all attachments for all messengers.

The attachment parameter gets an attachment that matches the channel parameter.

The attachment is localized. Texts from Localization are put instead of all the {{t'<key>}} variables.

Values are dynamically inserted into the attachment. The values of parameters incoming to the Send Message Process with a task are put instead of all the Send Message Process with a Task are put instead of all the {{param}} parameters used in the attachment description.

The composed message is sent to a user.

Examples

By default, the Attachments State Diagram contains ready-made attachments, for example, mainKeyboard – the main menu keys:

Facebook Messenger

Screenshot 387: Main menu.

Viber

Screenshot 388: Main menu bot options.

Telegram

Screenshot 389: Main menu bot options.

Apple Messages for Business

Screenshot 390: Apple messages for business.

For more information on attachment types, go to the API documentation of each messenger:

Viber

Facebook Messenger

Telegram

Apple Messages for Business

Attachment JSON Example:

REF: exit

{

"telegram": {

"type": "inline_keyboard",

"buttons": [

[{

"text": "🚪 {{t'exit}}",

"callback_data": "/exit"

}]

]

},

"viber": {

"type": "keyboard",

"buttons": [{

"Columns": 6,

"Rows": 1,

"BgColor": "#F3F3F3",

"Text": "🚪 {{t'exit}}",

"ActionType": "reply",

"ActionBody": "/exit",

"TextVAlign": "middle",

"TextHAlign": "center",

"TextSize": "regular",

"Silent": true

}]

},

"facebook": {

"type": "quick_replies",

"buttons": [{

"content_type": "text",

"title": "🚪 {{t'exit}}",

"payload": "/exit"

}]

}

}

Dynamic Attachment and template

When developing a bot, there is often a need to display data with a homogeneous structure, like a catalog of products, a cart with selected goods, a list of current special offers, and so on which is considered a dynamic attachment. The Send Message Process supports the creation of attachments using a template for a varying number of items.
In the example below, you can see how to add a template for displaying exchange rates using an included-in-attachment template.

JSON Example (Dynamic attachment)

REF: carousel_pattern

{

"attachment": {

"facebook": {

"type": "carousel",

"items": [

{

"title": "{{value}} {{name}}",

"subtitle": "1 USD"

}

]

},

"viber": {

"type": "carousel",

"carouselRows": "1",

"carouselColumns": "6",

"items": [

{

"Columns": 6,

"Rows": 1,

"ActionType": "reply",

"ActionBody": "none",

"Text": "1 USD = {{value}} {{name}}",

"TextSize": "small",

"TextVAlign": "middle",

"TextHAlign": "middle",

"Silent": true,

"BgColor": "#FFFFFF"

}

]

},

"abc": {

"type": "text_list_picker",

"maxItemsCountToShow": 10,

"items": [

{

"identifier": "{{name}}",

"order": 0,

"style": "small",

"subtitle": "per 1 EUR",

"title": "{{value}} {{name}}"

}

],

"order": 0,

"title": "💱 {{t'/exchangeRates}}",

"multipleSelection": false,

"receivedMessage": {

"style": "small",

"subtitle": "",

"title": "💱 {{t'/exchangeRates}}"

},

"replyMessage": {

"style": "small",

"title": "💱 {{t'/exchangeRates}}",

"subtitle": ""

}

}

}

}

There is no template for Telegram because Telegram does not support this kind of message.

Items Sourcing Array
For creating a carousel, an array is needed for providing values to the template:
"items": [

{

"value": "4.183966 AED",

"name": "1 USD"

},

{

"value": "85.890287 AFN",

"name": "1 USD"

}

]

Parameters for Send Message Process
Calling the Send Message Process requires passing the following parameters:
{

"attachment_id": "carousel_pattern"

"items": "items"

"currentPage": 1

"disableExitButton": false|true (a flag to      show the Exit button)

}

A Code node named createDynamicAttachment performs all other necessary actions over an object.

Screenshot 391: The createDynamicAttachment Code node.

The Send Message Process considers messenger limitations and does corresponding pagination automatically: it breaks the array into pages and adds the navigation buttons. The Exit button is added if disableExitButton = false.

Converted JSON:
"message": {

"quick_replies": [{

"content_type": "text",

"title": "🚪 Exit",

"payload": "/exit"

}],

"attachment": {

"type": "template",

"payload": {

"template_type": "generic",

"elements": [

{

"title": "4.183966 AED",

"subtitle": "1 USD"

},

{

"title": "85.890287 AFN",

"subtitle": "1 USD"

},

...

]

}

}

}

Examples of Displaying:

Facebook Messenger

Screenshot 392: Facebook Messenger.

Viber

Screenshot 393: Viber exchange rate menu.

Apple Business Chat

Screenshot 394: Apple business chat exchange rate menu.

Tokens

The Tokens State Diagram stores bots access tokens and credentials for integration with Simulator.
JSON Example:

REF: token

{

"abc": "",

"facebook": "",

"simulator": {

"token": "",

"developersGroupId": "",

"id": "",

"accId": "",

"baseUrl": "https://api.simulator.company/v/1.0"

},

"slack": "",

"telegram": "",

"viber": ""

}

Localization

The Localization state diagram stores all texts of all messages and attachments in one Task:

Task example:
REF: localization

{

"/exit": {

"en": "Exit",

"ru": "Выход",

"uk": "Вихід"

},

"mainMenu": {

"en": "Main Menu",

"ru": "Главное меню",

"uk": "Головне меню"

},

"no": {

"en": "No",

"ru": "Нет",

"uk": "Ні"

},

"yes": {

"en": "Yes",

"ru": "Да",

"uk": "Так"

},

...

}

The approach allows you to:

Manage all bot texts from one place.

Send messages by only specifying a key of the necessary text in the localization object.

Localize bot interface. By default, the texts are in the en, ru and ua, languages, but any language can be added.

To send a text message, specify the key name key from the localization task as a value of the text_id parameter:
1. Use the text_id parameter and set its value to a key name that exists in the localization task/object. This allows the system to look up the appropriate localized text.

2. The actual message sending requires providing several parameters to the Send Message Process (see the example below).
3. The system will automatically:

Look up the text in the localization object using the provided key

Send the message in the user's preferred language (stored in User Profile State Diagram)

Default to English ('en') if no language preference is set

The language can be changed using the Set Parameters node named "SET default language == EN"

Example. To send the Main menu to a bot, you need to provide the Send Message Process with the following parameters and values:

Screenshot 395: Send Message Process.

{

"attachment_id": "mainKeyboard",

"channel": "viber",

"chat_id": "...",

"text_id": "mainMenu"

}

For localization, attachments should have their parameters of UI texts (button names, labels, etc.) to meet the {{t'<key>}} template, where <key> is the key of a necessary text in the localization object.

Example. Localization of the Exit button:

{

"content_type": "text",

"title": "🚪 {{t'/exit}}",

"payload": "/exit"

}

The Send Message Process sends a message in the same language as the one stored for a user in the User Profile State Diagram. The default language is en and can be changed in the Set Parameters node named SET default language == EN of the Send Message Process.

Simulator folder

Overview

The Simulator folder path:
Stages → Stage name → Communications Orchestrator → Messengers → Simulator folder.

Screenshot 396: Communication Orchestrator Simulator folder.

A solution for organizing live chat between a client and a human operator is built on the Simulator within the Communications Orchestrator. The Simulator folder stores:

Processes for the operator's workspace to handle dialogs

Chat history, client profiles, analytics, and dashboards

BP: business processes that you can reconfigure:

bp > chats > freeze chat: The Process that handles the freeze event in dialogs = dialog closure. In this Process, transactions against customer and operator accounts are made for analytics collection and the change of dialog connections with streams.

bp > chats > create employee > create dashboards: The Process starts with the Creation of the new employees actor event and creation of new dashboards for a new operator.

bp > chats > send file from operator to client: In this Process, sending files from an operator to a customer is performed.

bp > chats > update agent status: If the Status field is altered, the Process starts when the Update actor employees event occurs. In this Process, transactions against operator accounts are made to track the time the operator was in each status.

bp > chats > done chat: In this Process, the Done reaction in the operator chat is handled.

bp > chats > get available chatId: The Process retrieves a free new chatId from a queue.

Scripts: Stores the Processes for each script, which handles all requests from the Smart Forms.

Widget: Widget Processes.

Generator chatId: Processes for generating a unique chatId.

Setup Simulator Cache: The process starts automatically when the Communications Orchestrator is created. It goes through all the entities created in Simulator and unites them into a single cache object. This object is stored in the Simulator Cache State Diagram and is used in most processes for quick access to Simulator objects.

Simulator entities in folder

After creating a Communications Orchestrator in Corezoid, a set of necessary forms, actors, and accounts for orchestrating messages between the client and the operator, as well as for collecting analytics, is imported into your workspace in Simulator:

Forms

Actors

Events

Dialog components

Dashboards

Widgets

Scripts

Forms

To access forms, go to Editors → Forms → Custom Forms.

Screenshot 397: Forms in Communications Orchestrator.

With forms, you can describe the data structure for uniform objects (actors). Forms are very flexible, and their model can be changed or extended as needed. Any attributes described in the form can be used to build filters or selections of actors. The following form types were created:

employees: Describes the data structure of employees (operators, supervisors, and so on):

The Group field refers to the filter for all actor groups and describes the structure of groups. Groups can be used to combine several employees and apply any mass actions to the group.
Note: Groups are added as an example and are not used by default in the logic of Communications Orchestrator.

The Status field refers to the filter for all operator statuses.

Screenshot 398: Status field in the Form.

users: Describes the structure of clients’ data from various channels.

Screenshot 399: User data from various channels.

chats: Describes the structure of chats data:

The User field refers to the filter by all user actors.

The Operator field refers to the filter by all employee actors.

The Channel field refers to the filter by all channel actors.

The Status field refers to the filter by all chatStatuses actors.

Screenshot 400: Chat fields in the Form.

The channels, chatStatuses, and operatorStatuses forms serve as dictionaries. You can create as many dictionaries as needed and use them in your Processes.

Actors

To access actors, go to Simulator → Actors bag.

Screenshot 401: Actors bag page.

Actors bag is a place where we work with the actual actors. An actor can be a specific operator, a specific client, a specific chat, and so on.
On the Actors bag page, you can do the following:

Apply filters or configure the needed ones.

Screenshot 402: Applying filters.

Create new actors, view actor details, edit an actor, and so on.
Note: To create an actor of the employee type in the form, turn the Optional fields toggle on and choose the corresponding user in the Single account user field, who is registered in the system. Doing this establishes a connection between the actor and the actual user in the system. A user can only be associated with one actor in the workspace at a time. This action is necessary for the logic of distributing dialogs between operators, which you can configure in the /startChat Process. When creating a Communications Orchestrator, one employee actor is created per the user who created the Communications Orchestrator.

View actor’s accounts. Accounts can be used to track any action, event, or other changes. After creating Communications Orchestrator, several accounts were created for clients and operators, where the following are accounted for:

The number of chats per operator (active / total)

Ratings given by clients to the operator

The time that the operator spent in different statuses.

Correspondingly, in Corezoid, Processes are built that respond to triggers to create transactions and update account balances. Account balances can also be used in business logic. For example, the activeChats account on actor-employees is involved in the logic of distributing dialogs between operators. If you need to start keeping track of anything else, simply open an account for the corresponding type of actors, specify the currency - what to track, and build Processes to create transactions. For more information, go to the /startChat Process.

Events

To access events, go to Simulator → Events.

Screenshot 403: Events page.

The Events page is the main working space for agents handling dialogs.
There are two modes for viewing the list of events: Regular and Split. For working with multiple dialogs simultaneously, we recommend using the Split mode. It allows you to switch between conversations with one click while seeing the full picture of your dialogs: the appearance of new dialogs, new reactions in current dialogs, and so on.
You can distribute events (dialogs) to different stream tabs. Stream tabs are a feature on the Events page that allow users to organize and view events in different streams. Key Features:

Users can create custom stream tabs to organize events into different categories

Stream tabs appear on the right side of the existing system tabs

There are default system tabs that cannot be reordered: All, To Sign, To Do, and Starred

Users can reorder custom stream tabs by dragging and dropping them

The selected order of stream tabs is saved

Adding an event to a stream tab equals creating a connection (edge) between event actors and stream actors. There are three system stream tabs: To Do, To Sign, and Starred.

To stop displaying system stream tabs and enable the display of the ones you need, click the settings icon and select the checkboxes for the stream tabs you want to display.

After creating the Communications Orchestrator, two new stream tabs are added:

Active chats: New dialogs get listed in this stream and remain there until they are closed. The logic for adding a new dialog to this stream is configured in the /startChat Corezoid Process.

Closed chats: These are dialogs moved from the Active chats stream tab immediately after the chat status changes to Closed.

Screenshot 404: Active and Closed chats streams.

The same dialog can be maintained in multiple stream tabs simultaneously. You can create new stream tabs and configure the needed logic for adding dialogs to them, for example:

Streams based on the themes of inquiries or based on the channels of inquiries

Streams based on the duration of the dialog

Dialog components

The dialog has the following components (actors, parameters, Smart Forms, snippets and Process logic):

Dialog name: A dialog can have any name and has the following dynamic structure:
{channel} - {chatId} - {userName}
Where:

channel: The channel of the inquiry.

chatId: A unique chat ID generated in the chatId generator Process. The algorithm can be modified.

userName: Username retrieved from a user actor.

Card of an actor: A card of a chats actor, which characterizes the dialog itself, is added to the dialog.

Shared with: indicates who has been added to the dialog and with what roles. The operator can manually share the dialog with another operator or a group.

Linked actors: A list of actors associated with the dialog. Linking the dialog to actors is necessary for displaying the selected dialog in the history of events for these actors. Currently, history is linked to actors in:

Stream tabs: activeChats and closedChats.

Employees: The actor of the operator who is handling the dialog.

Users: The actor of the client who contacted support.

Done: The action is linked to the logic of completing the dialog from the operator's side. The Simulator Receiver Corezoid Process tracks the dialog completion event and triggers the /NPS Process.
Note: You can modify this logic.

Scripts: Are run within the dialog with the option to specify the recipients.

Snippets: Allow the fast use of predefined phrases.

Dashboards

To access dashboards, go to Graphs → Dashboards.

Screenshot 405: Dashboards view on the Graphs page.

Using analytics with dialogs

When account balances are tracked for actors such as operators or users, on the dashboards, you can visualize the balances or transaction dynamics.

Configure Dashboards

The architecture of Communications Orchestrator inherently includes the logic for automatically creating four dashboards as soon as an employee actor is created. A separate layer is created for each employee with metrics specific to them. This logic is built in the bp → chats → create employee → create dashboards Process and can be changed or expanded.

To switch between the layers, use the bottom panel.

Screenshot 406: Switching between layers.

Widgets

To access widgets, go to Editors → Communications → Widgets or Comments Widgets.

Screenshot 407: Widgets.

After the Communications Orchestrator has been created, a widget actor is created, which you can access on the Communications page. Click the widget, and on the Embed code tab, you can obtain the embed code for the widget and add it to your website or any test environment.

Screenshot 408: Embed code.

Scripts

To access Smart Forms (former Scripts), go to Editors → Smart Forms.

Screenshot 409: Smart Forms (former Scripts).

The widget has the following Smart Forms:

Together with the widget, the Welcome and Chat rating Smart Forms were created.

Screenshot 410: Welcome and Chat rating Smart Forms.

Start Script: Executes when the widget is launched.

Final Script: Executes when the user clicks the close button (X) in the widget.

The configuration of the Smart Forms and their execution logic can be modified.

In Corezoid, Processes for interacting with Smart Forms are located in the Communications Orchestrator → Messengers → Simulator → Scripts folder.

To use Smart Forms:

After creating Orchestrator, replace Corezoid credentials in the script settings with your own.

Create an API Key in Corezoid and grant Task management access to this API Key for each main receiver script (Process “script - {scriptName} - main receiver”).

Fill in the corresponding parameters in the settings of each script: API login, API secret, Company ID, Dev process ID, and Prod process ID.
Note: You can specify the same Dev and Prod Processes if needed.

Agent panel Smart Form

Is used for changing the operator's status to avoid giving operators direct access to actors-employees.

You can add the script to favorites to add it to the side panel (it appears on the panel after refreshing the page).

Screenshot 411: Welcome and Chat rating Smart Forms.

Every change in the operator's status is logged on the respective accounts and displayed on dashboards.

The logic is configured in the Process bp → chats → update agent status.

When adding new statuses, modify this Process accordingly.



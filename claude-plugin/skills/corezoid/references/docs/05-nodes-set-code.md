<!-- Part of Corezoid docs. See docs/INDEX.md for full navigation. -->

### 3.5 Set Parameters
Overview


Screenshot 183: Set Parameters node view

The Set Parameters node offers a simple way to work with task variables and parameters. By using this node, you can:

Add new parameters to a task going through the Process.

Update the existing task parameters.


Diagram 9: Set Parameters node flow.

Node Settings

The Set Parameters node has the following parameters:


Screenshot 184: Set Parameters node settings.

Title [Optional] [Field] [String]: Node title.

Description  [Optional] [Field] [String]: Node description.

Show more [Optional] [Action]: Long descriptions are reduced to a compact view to simplify node settings. Click to see the whole description.

Copy node [Optional] [Action]: Creates a copy of the current node with all settings.

Remove node [Optional] [Action]: Deletes current node from Process.

Remove links [Optional] [Action]: Removes all connections to/from current node.

Info [Optional] [Action]: Displays node ID.

Errors info [Optional] [Action]: Displays node errors.

Key [Required] [Field] [String]: Key to specify a static name or a variable in {{}} curly brackets
To add a new parameter, specify a unique name, to update an existing parameter, use its original name as a key.

Value [Required] [Field] [Any]: The value you want to assign to the corresponding Key parameter. See data types descrition for more details.

Code editor [Optional] [Field] [Any]: Shows the JSON format of the entered Key and Value. Click Code editor to open the code editor tab, where:

Screenshot 185: Code editor tab.

Code editor field [Optional] [Field] [Any]: Enter new keys and values or edit the existing ones in JSON format.

Full-screen mode [Optional] [Action]: Opens the Code editor field in the full-screen mode, where:

Screenshot 186: Code editor full-screen view.

Code editor field [Optional] [Field] [Any]: Edit or add keys in values.

Format code [Optional] [Action]: Format your current code.

Quit the full-screen mode [Optional] [Action]: Quit the full-screen mode.

Type of data [Required] [Action]: Selects the data type for the Value:
	* String (S)
	* Number (N)
	* Boolean (B)
	* Array (A)
	* Object (O)
	
	Note: For more information, go to Data types.

Delete key-value [Optional] [Action]: Delete the key-value pair.

Add key-value [Optional] [Action]: Add a new key-value pair.

Alert if the number of tasks in the node queue reaches the following number [Optional] [Action]: Helps monitor whether the number of tasks in the node exceeds the specified threshold.

Number of tasks in the queue [Optional/Required if Alert if the number of tasks in the node queue reaches the following number is selected] [Field] [Number]: Number of tasks in the queue which triggers an alert when reached. Set to 30 by default.

Maximum interval, for which the task stays in the node before being forwarded [Optional] [Action]: The amount of time a task is allowed to be in the node can be set in seconds, minutes, hours, and days.

Maximum interval [Optional/Required if Maximum interval, for which the task stays in the node before being forwarded is selected] [Field] [Number]: The amount of time a task is allowed to be in the node. Has a minimum value of 30 seconds. You can set a shorter interval by using the Unixtime function.

Maximum interval measuring unit [Required] [Action]: Selects the measuring unit for the maximum interval:

Seconds

Minutes

Hours

Days.

Examples

Defining a new parameter

In the example below, you can see how to define a new parameter as a constant in a Process.

The value of a new parameter doesn't have to be a constant. You can assign it a value based on a task parameter or a value stored in a State Diagram.

Changing parameter value

Below, you can see examples of two ways of modifying the parameter value:

Replacing a value of an existing parameter with a new one.

Screenshot 187: Updating a parameter value in Set Parameters.

To perform the replacement, the parameter key specified in the Set Parameters node must exactly match the key of an existing task parameter. The parameter matching the key ensures that the correct parameter value is updated and prevents accidentally creating a new parameter with the same name.

Modifying a value of an existing parameter by using the $.math() function to add or subtract a certain value from the original value.
If the task goes to the Error node for any reason after passing through the Set Parameters node, no parameters will be modified or added, and none of the changes specified by the Set Parameters node will be applied.


Screenshot 188: Modifying a parameter in Set Parameters.

You can access a single task parameter or a whole task stored in a State Diagram by Getting Task Parameters from State Diagrams.

Error handling & troubleshooting

When an error occurs during the task processing, you may see the following error parameter names in the task.

*The error __conveyor_set_param_return_type_tag__may have the following values.

Table 6: Error parameter names.

Table 7: Set Parameters errors.

When working with your Process or State Diagram, you may encounter the following issues.

Table 8: Set Parameters issues.


### 3.6 Code
Overview

Screenshot 189: Code node view

The Code node provides a convenient way to add custom functionality to your Process by allowing you to access, modify, and create task parameters based on JavaScript or Erlang code you input in the node.

Compared to the Git Call node, the Code node offers faster execution and does not require warming up before the first use. It also makes more efficient use of resources.

Although the Code node is highly efficient in speed, you may encounter a timeout error if your code is computationally intensive and takes an extended period to execute or if it includes an infinite loop. If your code requires extra processing power, you can create a dedicated microservice and call it from Corezoid. If you need further assistance, don't hesitate to contact us for custom solutions that will better fit your needs.

The Code node is designed for handling simple code snippets. For more complex code running, we recommend using the Git Call node as a better alternative.

Key Features

Parameter manipulation

Custom logic implementation

Fast execution

No warm-up required

Resource efficient

Limitations

Simple code snippets only

Risk of timeout with:

Computationally intensive operations

Infinite loops

Extended execution times

Recommendations

Use for basic code operations

For complex code, consider:

Git Call node

Dedicated microservices

Custom solutions

Compared to Git Call

Table 9: Code vs Git Call comparison.

Diagram 10: Code node flow.

Node Settings

The Code node has the following parameters:


Screenshot 190: Code node settings.

Title [Optional] [Field] [String]: Node title.

Description  [Optional] [Field] [String]: Node description.

Show more [Optional] [Action]: Long descriptions are reduced to a compact view to simplify node settings. Click to see the whole description.

Copy node [Optional] [Action]: Creates a copy of the current node with all settings.

Remove node [Optional] [Action]: Deletes current node from Process.

Remove links [Optional] [Action]: Removes all connections to/from current node.

Info [Optional] [Action]: Displays node ID.

Errors info [Optional] [Action]: Displays node errors.

Language [Required] [Action]: Selects the programming language to be used in the Code editor:

JavaScript (default)

Erlang.

Use code completion [Optional] [Action]: When checked, activates the AI to automatically complete the code in the Code editor. For instance, you can type "//" to generate automatic comments for the current code fragment or type command for the AI to complete the code line automatically.

Code editor [Required] [Field] [Any]: Code editor field to enter your code.

Full-screen mode [Optional] [Action]: Opens the Code editor field in the full-screen mode, where:

Screenshot 191: Code editor full-screen view.


## 12.1 Code editor field [Optional] [Field] [Any]: Edit or add keys in values.

## 12.2 Format code [Optional] [Action]: Format your current code.

## 12.3 Explain code [Optional] [Action]: Activates the AI to generate the explanation for the code in the Code editor.

## 12.4 Quit the full-screen mode [Optional] [Action]: Quit the full-screen mode.
Verify code [Optional] [Action]: Check your code in the Code editor. If verification succeeds, the message “Code is valid” will appear instead of the Verify code button:


Screenshot 191.1: Code editor: code validation success.

Explain code [Optional] [Action]: Activates the AI to generate an explanation for the code in the Code editor. The explanation will be displayed in a panel below the code:

Screenshot 191.2: Code editor: code explanation panel.

To close the generated explanation, click the cross icon in the explanation panel.

Alert if the number of tasks in the node queue reaches the following number [Optional] [Action]: Helps monitor whether the number of tasks in the node exceeds the specified threshold.

Number of tasks in the queue [Optional/Required if Alert if the number of tasks in the node queue reaches the following number is selected] [Field] [Number]: Number of tasks in the queue which triggers an alert when reached. Set to 30 by default.

Maximum interval, for which the task stays in the node before being forwarded [Optional] [Action]: The amount of time a task is allowed to be in the node can be set in seconds, minutes, hours, and days.

Maximum interval [Optional/Required if Maximum interval, for which the task stays in the node before being forwarded is selected] [Field] [Number]: The amount of time a task is allowed to be in the node. It has a minimum value of 30 seconds. You can set a shorter interval by using the Unixtime function.

Maximum interval measuring unit [Required] [Action]: Selects the measuring unit for the maximum interval:

Seconds

Minutes

Hours

Days.

Languages Supported in the Code Editor


The Code editor supports the following programming languages:

Javascript: Task parameters can be found within the data object, and you can access them using dot notation.
data.parameter_name

List of supported JavaScript libraries:

moment v2.11.1 (example)

moment-timezone v2.11.1 (example)

CryptoJS v3.1.2 (limited)

Available CryptoJS methods:

Hashing: MD5, SHA-1, SHA-512, HMAC MD5, HMAC SHA-1, HMAC SHA-256

Ciphers: AES, DES, Triple DES, Rabbit, RC4

Encoders: base64
Below you can see an example of your code where Data is the task object, and param is one of its parameters.

-module(node).

-export([main/1]).

main(Data) -> [{<<"param">>, <<"Hello World!!!">>} | Data].

XRegExp: XRegExp is an extensive regular expression library for JavaScript, enhancing native RegExp with new capabilities and syntaxes. It simplifies complex regex operations and supports Unicode matching.

Examples

Working with date/time using moment.js

In the Code editor field of the Code node details panel, you can write your code in JavaScript using the supported libraries.


Screenshot 192: Code editor field with JavaScript language selected.

You can see the example below.

require("libs/moment.js");

let datetime = moment().format('MMMM Do YYYY, h:mm a');

data.message = "Hi " + data.name + ". Today is " + datetime +". What a great time to learn Corezoid!" ;

require("libs/moment.js"): Import the moment.js library used to obtain the current date and time.

let datetime = moment().format('MMMM Do YYYY, h:mm a'): Use the moment() method to obtain the current date and time and the format() method to convert it into a string. The resulting value is assigned to a local variable.

data.message = "Hi " + data.name + ". Today is " + datetime +". What a great time to learn Corezoid!": Create a string using the value of the name parameter from the data object and the value of the datetime variable generated. Assign this string to data.message, which creates a new task parameter with the message key and the value of the string.

The data object stores the task parameters: name is an existing task parameter, and message is added as a new one. datetime is a local variable that will not be part of the task; it only exists temporarily while the node processes it.

Moment-timezone

require("libs/moment-timezone.js");

data.date = moment().tz('Europe/Kiev').format("DD-MM-YYYY HH:mm:ss");

require("libs/moment-timezone.js"): Import the moment-timezone.js library used to convert and format dates for different time zones.

data.date = moment().tz('Europe/Kiev').format("DD-MM-YYYY HH:mm:ss"): Use the moment() method to obtain the current time, the format() method to define the desired format, and the tz() method to change the time zone to Europe/Kiev.

Hashing

MD5
require("libs/md5.js");

data.md5 = CryptoJS.MD5(data.variable).toString();

JavaScript

Copy

data.variable: Task parameter that will be hashed.

data.md5: Task parameter that will store the hash.

SHA-1
require("libs/sha1.js");

data.sha1 = CryptoJS.SHA1(data.variable).toString();

data.variable: Task parameter that will be hashed.

data.sha1: Task parameter that will store the hash.

SHA-512
require("libs/sha512.js");

data.sha512 = CryptoJS.SHA512(data.variable).toString();

data.variable: Task parameter that will be hashed.

data.sha512: Task parameter that will store the hash.

HMAC SHA-1
require("libs/hmac-sha1.js");

var hash = CryptoJS.HmacSHA1(data.message, data.secret);

data.hashInHex = hash.toString(CryptoJS.enc.Hex);

data.message: Task parameter that will be hashed.

data.secret: Task parameter that stores the secret.

data.hashInHex: Task parameter that will store the hash as a hexadecimal string.

HMAC SHA-256
require("libs/hmac-sha256.js");

var hash = CryptoJS.HmacSHA256(data.message, data.secret);

data.hashInHex = hash.toString(CryptoJS.enc.Hex);

data.message: Task parameter that will be hashed.

data.secret: Task parameter that stores the secret.

data.hashInHex: Task parameter that will store the hash as a hexadecimal string.

Ciphers

AES
Encrypting
require("libs/aes.js");

data.encrypted = CryptoJS.AES.encrypt(data.message, data.password).toString();

data.message: Task parameter that will be encrypted.

data.password: Task parameter that contains the password.

data.encrypted: Task parameter that will store the encrypted string.

Decrypting
require("libs/aes.js");

data.decrypted = CryptoJS.AES.decrypt(data.encrypted, data.password).toString(CryptoJS.enc.Utf8);

data.encrypted: Task parameter that will be decrypted.

data.password: Task parameter that contains the password.

data.decrypted: Task parameter that will store the decrypted string.

DES
Encrypting
require("libs/tripledes.js");

data.encrypted = CryptoJS.DES.encrypt(data.message, data.password).toString();

data.message: Task parameter that will be encrypted.

data.password: Task parameter that contains the password.

data.encrypted: Task parameter that will store the encrypted string.

Decrypting
require("libs/tripledes.js");

data.decrypted = CryptoJS.DES.decrypt(data.encrypted, data.password).toString(CryptoJS.enc.Utf8);

data.encrypted: Task parameter that will be decrypted.

data.password: Task parameter that contains the password.

data.decrypted: Task parameter that will store the decrypted string.

Triple DES
Encrypting
require("libs/tripledes.js");

data.encrypted = CryptoJS.TripleDES.encrypt(data.message, data.password).toString();

data.message: Task parameter that will be encrypted.

data.password: Task parameter that contains the password.

data.encrypted: Task parameter that will store the encrypted string.

Decrypting
require("libs/tripledes.js");

data.decrypted = CryptoJS.TripleDES.decrypt(data.encrypted, data.password).toString(CryptoJS.enc.Utf8);

data.encrypted: Task parameter that will be decrypted.

data.password: Task parameter that contains the password.

data.decrypted: Task parameter that will store the decrypted string.

Rabbit
Encrypting
require("libs/rabbit.js");

data.encrypted = CryptoJS.Rabbit.encrypt(data.message, data.password).toString();

data.message: Task parameter that will be encrypted.

data.password: Task parameter that contains the password.

data.encrypted: Task parameter that will store the encrypted string.

Decrypting
require("libs/rabbit.js");

data.decrypted = CryptoJS.Rabbit.decrypt(data.encrypted, data.password).toString(CryptoJS.enc.Utf8);

data.encrypted: Task parameter that will be decrypted.

data.password: Task parameter that contains the password.

data.decrypted: Task parameter that will store the decrypted string.

RC4
Encrypting
require("libs/rc4.js");

data.encrypted = CryptoJS.RC4.encrypt(data.message, data.password).toString();

data.message: Task parameter that will be encrypted.

data.password: Task parameter that contains the password.

data.encrypted: Task parameter that will store the encrypted string.

Decrypting
require("libs/rc4.js");

data.decrypted = CryptoJS.RC4.decrypt(data.encrypted, data.password).toString(CryptoJS.enc.Utf8);

data.encrypted: Task parameter that will be decrypted.

data.password: Task parameter that contains the password.

data.decrypted: Task parameter that will store the decrypted string.

Encoders

Base64

Encoding
require("libs/base64.js");

var wordArray = CryptoJS.enc.Utf8.parse(data.variable);

data.base64 = CryptoJS.enc.Base64.stringify(wordArray);

data.variable: Task parameter that will be encoded.

wordArray: Tocal variable that stores a wordArray representation of data.variable.

data.base64: Task parameter that will store the encoded string.

Decoding
require("libs/base64.js");

var words = CryptoJS.enc.Base64.parse(data.base64);

data.parsedStr = words.toString(CryptoJS.enc.Utf8);

data.base64: Task parameter that will be decoded.

words: Tocal variable that stores a wordArray representation of data.base64.

data.parsedStr: Task parameter that will store the decoded string.

JWT Token

Encoding
require("libs/hmac-sha256.js");

require("libs/base64.js");

// Custom function to base64URL encode a string manually (pure JS)

function base64UrlEncode(input) {

// Convert the input to a word array

const wordArray = CryptoJS.enc.Utf8.parse(input);

// Convert the word array to a base64 string

let base64String = CryptoJS.enc.Base64.stringify(wordArray);

// Perform base64URL encoding (replace characters and remove padding)

base64String = base64String.replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');

return base64String;

}

// Function to create a secure HMAC SHA-256 signature

function createSignature(message, secret) {

// Generate HMAC SHA-256 signature using the loaded library

const hash = CryptoJS.HmacSHA256(message, secret);

// Convert the hash to a base64-encoded string

const base64 = CryptoJS.enc.Base64.stringify(hash);

// Convert base64 to base64url

return base64.replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');

}

// Function to generate the JWT token

function generateJwtToken(header, payload, secret) {

// Step 1: Encode the header and payload

const encodedHeader = base64UrlEncode(JSON.stringify(header));

const encodedPayload = base64UrlEncode(JSON.stringify(payload));

// Step 2: Create the signature using HMAC-SHA256

const message = `${encodedHeader}.${encodedPayload}`;

const signature = createSignature(message, secret);

// Step 3: Return the final JWT

return `${message}.${signature}`;

}

const header = {

alg: "HS256",

typ: "JWT"

};

const payload = data.payload;

const secret = data.secret;

data.jwtToken = generateJwtToken(header, payload, secret);

Decoding
require("libs/base64.js");

require("libs/hmac-sha256.js");

// Base64Url encode function

function base64UrlEncode(input) {

return CryptoJS.enc.Base64.stringify(input)

.replace(/\+/g, '-')

.replace(/\//g, '_')

.replace(/=+$/, '');

}

// Base64Url decode function

function base64UrlDecode(input) {

let base64 = input.replace(/-/g, '+').replace(/_/g, '/');

while (base64.length % 4) {

base64 += '=';

}

return CryptoJS.enc.Base64.parse(base64);

}

// Create HMAC SHA-256 signature

function createSignature(message, secret) {

const hash = CryptoJS.HmacSHA256(message, secret);

return base64UrlEncode(hash);

}

// Decode and validate JWT token

function decodeAndValidateJwtToken(token, secret) {

const parts = token.split('.');

if (parts.length !== 3) {

throw new Error('Invalid JWT token format');

}

// Decode header and payload

const header = JSON.parse(CryptoJS.enc.Utf8.stringify(base64UrlDecode(parts[0])));

const payload = JSON.parse(CryptoJS.enc.Utf8.stringify(base64UrlDecode(parts[1])));

const providedSignature = parts[2];

// Store decoded parts and original signature

data.jwtHeader = header;

data.jwtPayload = payload;

data.jwtSignature = providedSignature;

// Validate signature if secret is provided

if (secret) {

const message = `${parts[0]}.${parts[1]}`;

const expectedSignature = createSignature(message, secret);

data.signatureValidation = (expectedSignature === providedSignature) ? 'success' : 'failed';

} else {

data.signatureValidation = 'not performed';

}

// Validate token expiration

const currentTime = Math.floor(Date.now() / 1000);

if (payload.exp && payload.exp < currentTime) {

data.tokenStatus = 'expired';

} else {

data.tokenStatus = 'valid';

}

}

// Main execution

try {

const token = data.token;

const secret = data.secret || null; // Optional secret for validation

decodeAndValidateJwtToken(token, secret);

} catch (error) {

data.error = error.message;

}

XRegExp

Extended Syntax: This example demonstrates named capture groups for improved readability and maintainability.

Input (data.input - a text string):

[2024-11-06 14:23:00] INFO: User login successful, User ID: 12345, IP: 192.168.1.1

[2024-11-06 14:23:15] ERROR: Failed to load data, User ID: 12345

[2024-11-06 14:23:30] WARN: User requested invalid action, IP: 192.168.1.2

Code:

require("libs/xregexp.js");

// Define the complex multiline regex pattern

const logPattern = XRegExp(`

^                                 # Start of the line

(?<timestamp>\\[[^\\]]+\\])        # Capture timestamp in square brackets

\\s+                               # Match one or more spaces

(?<level>\\w+)                     # Capture the log level (INFO, ERROR, etc.)

:\\s+                              # Match colon and space after level

(?<action>[^,]+)                   # Capture the user action description (until the first comma)

(?:,\\s+User\\sID:\\s+(?<userId>\\d+))?  # Optionally match User ID (if available)

(?:,\\s+IP:\\s+(?<ip>[^\\s,]+))?       # Optionally match IP address (if available)

$                                 # End of the line

`, 'gm'); // Use 'g' for global matching and 'm' for multiline flag

data.output = [];

// Parse the log text using XRegExp.exec and iterate through matches

let match;

while ((match = XRegExp.exec(data.input, logPattern)) !== null) {

const logEntry = {

timestamp: match.timestamp,

level: match.level,

action: match.action,

};

if (match.userId) {

logEntry.userId = match.userId;

}

if (match.ip) {

logEntry.ip = match.ip;

}

// Output will now be stored in `data.output`

data.output.push(logEntry);

}

Output (data.output - a JSON array):

[

{

"timestamp": "[2024-11-06 14:23:00]",

"level": "INFO",

"action": "User login successful",

"userId": "12345",

"ip": "192.168.1.1"

},

{

"timestamp": "[2024-11-06 14:23:15]",

"level": "ERROR",

"action": "Failed to load data",

"userId": "12345"

},

{

"timestamp": "[2024-11-06 14:23:30]",

"level": "WARN",

"action": "User requested invalid action",

"ip": "192.168.1.2"

}

]

Unicode Matching: This pattern matches any Unicode letter, showcasing XRegExp's Unicode property support.

require("libs/xregexp.js");

XRegExp('\\p{L}');

Error handling & troubleshooting

When an error occurs in the Code node, a task goes to the auxiliary Condition output node that
is used for storing error parameters.

Screenshot 193: Forwarding an error occurred in the Code node to the auxiliary Condition node.

When an error occurs during the task processing, you may see the following error parameter names in the task.

*The error tag __conveyor_code_return_type_tag__ may have the following values.

Table 10: Error parameter names.

Table 11: Code node errors.

When working with your Process or State Diagram, you may encounter the following issues.

Table 12: Code node issues.



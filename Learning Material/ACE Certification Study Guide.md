# Let's Get Familiar with AiDE Agent

## Development Environment Setup

Visit [Imagine's AiDE homepage](https://aide.imagine.tech/),and  signing with your Microsoft account. Once you are here, click on the "Plugins" page and then select the "IDE Plugins" tab. Here you will find all available AiDE plugins, however, you should pick the "AiDE Agents" plugin for VS Code. 

Clicking on it will start the download for a `.vsix` directory. Once the download is complete, open VS Code and open the extensions tab or run the `Extensions: Install Extension` command with the command pallet. Click on the context menu and select "Install from VSIX", this will open your file browser, finally pick navigate and pick the extension we just downloaded.

### Requesting a Token

You may be tempted to use the "API Tokens" tab in Imagine to generate your token, however, these are tokens to interact with AiDE Chat through it's API to develop AI Powered applications. The agent requires a separate token with must be requested from: `[mail-here]`. 

Once you have received your token, open the AiDE Agent tab available through the sidebar or run the `AiDE Agent: Focus on View` command in the command palette. Click on the context menu and select settings. In the setting's `Providers` tab enter your token on the `API Key` input text field.
### Agent Permissions

As you delegate tasks to the Agent, it will request your permission to perform certain tasks. You may allow the agent to perform a set of tasks without this confirmation. To configure this, open the settings tab just as we did in the step before and visit the `Auto-Approve` tab. As a starting point, I would suggest you disable all options besides `Read` and `Browse`. 

This will allow the agent to read your project's files freely as context and allow it to either search the web for documentation resources or event interact should it be needed with your web application through the web browser..

As you build up your mastery and familiarity with the Agent, you could visit these settings and enable new permissions, however, these 2 are good sane defaults.

## Enabling Checkpoints

When you enable the agent to edit code, you can enable it to create a safe recovery point in case it commits and error and you would like to easily rollback to a working or safe state. To enable this feature open the `Checkpoints` settings tab and enable the "Enable automatic checkpoints" checkbox.

## Updating  Web-store with Flask



## Bootstrapping our Project with Plan Mode
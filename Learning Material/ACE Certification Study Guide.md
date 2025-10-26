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

## Simulating your test

When you start the test, you will be given a list of projects to pick from, there is a ton of variety fitting most use cases. To demonstrate this, we will be updating a simple Python Flask web store by building new features with AiDE. 

> [!Important] 
> Remember, the goal of this test is to showcase you ability to use AI tools such as AiDE Agent to accelerate your capabilities.

## Developers

We have been asked by the local mom and pop shop to update the website their son has left abandoned ever since he started college. Since we are mostly focused on our daily job, we can't spend too much time on this project, but since the owners have always been part of the community, we have decided to make some improvements to their site over the upcoming weekends.

Since we work at Value Labs, we have access to AiDE Agent, an AI coding agent which could help us get these features done rather quickly. First, clone the repository code.

```shell
git clone https://github.com/Je12emy/AIDE-Adoption-Program
```

Navigate to the `Code > WebStore` directory and open the directory with Visual Studio code, if you have not, check the [Development Environment Setup](#Development%20Environment%20Setup) guide.

```shell
cd Code
cd Webstore
code .
```
## Basic UI Enhancements

The site seems pretty basic, there are barely any items listed and it lacks the most basic aspects you would expect from a web store like a navigation bar, other pages like "About Us" and a "Contact" form could also help.

Since we are lacking some context, lets use `Plan Mode` to get familiar with the project, the stack and how it is structured.

Open the AiDE Plugin tab in VSCode by clicking on the icon in the primary sidebar or run the command `AiDE Agent: Focus on view` in the command palette.  `Tasks` are a unit of work you define, once you build a prompt, your agent will build a local todo list with the required steps to complete it's work. AiDE has various modes which dictate how it will complete a given tasks and how it will interact with itself and you as the developer.

You can switch between modes using the drop down at the bottom left, click on it an select `Plan`. Plan mode is used as an analysis mode for the agent to scan the code base and document as much context for other modes. These documentation artifacts known as "mementos"will be used by other modes as context or an internal memory, for tracking task progress, results, pending changes and of course, by you the engineer monitoring the whole Software Development Life Cycle (SDLC) .

> Memento: an object that you keep to remember a person, place, or event

> [!Tip]  Takeaway
> Plan mode will produce documentation which can be used by the agent to complete tasks and the engineer to audit progress.

Your first prompt does not need to be complicated, however, let's be specific with what we want, since this is exactly what we would expect from our project managers as engineers.

> Implement a responsive navigation bar located at the top of the site, it should be displayed on all pages. You should be use it to navigate to the landing page which lists all items and a empty "About Us" page and an empty "Contact" page
## Quality Assurance Engineers

## Bootstrapping our Project with Plan Mode
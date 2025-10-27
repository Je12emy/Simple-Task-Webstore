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

### Using Plan Mode

Since we are lacking some context, lets use `Plan Mode` to get familiar with the project, the stack and how it is structured.

Open the AiDE Plugin tab in VSCode by clicking on the icon in the primary sidebar or run the command `AiDE Agent: Focus on view` in the command palette.  `Tasks` are a unit of work you define, once you build a prompt, your agent will build a local todo list with the required steps to complete it's work. AiDE has various modes which dictate how it will complete a given tasks and how it will interact with itself and you as the developer.

You can switch between modes using the drop down at the bottom left, click on it an select `Plan`. Plan mode is used as an analysis mode for the agent to scan the code base and document as much context for other modes. These documentation artifacts known as "mementos"will be used by other modes as context or an internal memory, for tracking task progress, results, pending changes and of course, by you the engineer monitoring the whole Software Development Life Cycle (SDLC) .

> Memento: an object that you keep to remember a person, place, or event

> [!Tip]  Takeaway
> Plan mode will produce documentation which can be used by the agent to complete tasks and the engineer to audit progress.

Your first prompt does not need to be complicated, however, let's be specific with what we want, since this is exactly what we would expect from our project managers as engineers.

> Help me implement a responsive navigation bar located at the top of the site, it should be displayed on all pages. You should be use it to navigate to the landing page which lists all items and a empty "About Us" page and an empty "Contact" page.

After entering this prompt, the agent will begin producing memento artifacts for track it's reasoning on how it will complete your tasks. 

> [!Reminder] LLM's are based on token prediction
> Giving it a more actionable phrasing *may* incite it to jump into act mode and implement the feature,  Always keep in mind that LLMs work by predicting the next token using the previous tokens as input, this prediction may not always be the same, so your results may vary. 

Make sure you **always** audit the memento files, the agent will display each produced artifact and the reasoning for it's creation.

> After establishing the initial project documentation, I will proceed to analyze the existing files to integrate the new navigation bar.

```markdown
<!-- memento/productContext.md-->

# Product Context: Webstore Navigation

## 1. The Problem

Currently, the webstore lacks a centralized navigation system. Users cannot easily move between different sections of the site, such as the home page and other informational pages. This leads to a disjointed user experience and makes the site difficult to scale with new content.

## 2. The Solution

A persistent, responsive navigation bar will be implemented at the top of every page. This provides a consistent and intuitive way for users to navigate the site, improving usability and ensuring key pages are always accessible.

## 3. User Experience Goals

- **Effortless Navigation:** Users should be able to find and click on navigation links with minimal effort, regardless of the device they are using.
- **Consistency:** The navigation bar's appearance and location should remain consistent across all pages, reinforcing the site's structure and branding.
- **Clarity:** The links should be clearly labeled and lead to the correct pages.
```

In my case I noticed that there is no mention of web accessibility, this makes sense, I didn't mention this in my first prompt so the agent did not take this into consideration. I have 3 options, start a prompt from scratch and mention it, update the memento file or enter a follow up prompt, this is a pick your own adventure sort of guide so feel free to choose any option. I will enter the next follow up prompt.

> Consider web accessibility, include aria tags and semantic HTML tags like `nav` in your code.

This has modified the project brief memento, here is the new entry.

```markdown
- **Accessibility:** The navigation bar will be built with semantic HTML (e.g., `<nav>`) and ARIA attributes to ensure it is accessible to users with disabilities, including those who use screen readers.
```

I'm pretty happy with this, the agent will ask you to allow it to save the memento to move on. Click on "Save". Continue reviewing each memento, remember that memento outputs may vary but this is a great moment to familiarize yourself with the code base specially if like me, you are not familiar with Flask.

Once the agent is done planning, it will ask you read the source code, make sure you audit what the agent wants to read, specially if the are API secrets within the code base somewhere. Soon after, the agent will ask you to allow it to move into `Act Mode` or continue refining your current plan.


> [!Tip] Controlling the agent with `.aiderules`
> You can provide a global project based context for all prompts, this can be done in a file named `.aiderules`. Here you can provide additional context, you could for example instruct the agent to NOT read a sensible file. For example
> 
> > Do NOT read the contents of the file named `.env`, if not, make sure to ask for permission

### Act Mode

This is the mode you agent will use to actively perform changes on your code base, here it will continue to generate or update your memento files to keep track of changes and it's progress towards completing your tasks. Feel free to continuously request for changes until you are happy with the result. 

A great feature to keep in hand is "Checkpoints", these are points in time where the agent is keeping a snapshot of your code, allowing you to rollback changes in case you would like to branch off from a given point if not check which changes where made. This is great in case the LLM causes unexpected issues and you would like to  start off from a working state.

With our working navbar, I challenge you to build the content of the "About Us" page and the "Contact" page, but here is a twist:

- In act mode, instruct the agent to use a markdown file as the text content to generate the page. This would allow the store owners to update it as needed without needing your help.

I was able to complete this task using the following prompt.

> Fill the content in the about page, let me use a markdown file to declare content of the page.

- In plan mode, build the contact form and implement email sending through `flask-mail` and catch those emails locally using `mail-hog`.

Here is a prompt that worked for me.

> Implement a contact form in the "Contact" page, it should allow the user to enter his first and last name, his contact email and a message. A mail should be sent using flask-mail to `mailhog` running with it's default settings.

### Crafting Multiple Tasks with Cook Mode

Our Webstore is looking much better, let's see if we can add sorting and filtering. To do this, let's explore *Cook Mode*. This mode is used to allow the agent to divide a task into smaller units of work for other modes. For example, using the following prompt.

> Help me implement product sorting based on price and filtering based on categories with a select picker and pricing with a slider

Caused the agent to craft the following sub-task for *Act Mode*.

> Creating a new subtask in Act mode...
> 
> Update the main route in app.py to handle product sorting and filtering.
> 
> Instructions:
> 
> Modify the main route (/) to accept the following query parameters:
> sort_by: for sorting by price (price_asc or price_desc).
> category: for filtering by product category.
> min_price and max_price: for filtering by price range.
> Implement the logic to query the database based on these parameters.
> Pass the sorted and filtered products to the index.html template.
> Ensure that all categories are fetched from the database and passed to the template so they can be displayed in a filter.
> Do not implement any frontend changes in this subtask.
> Signal completion by using the attempt_completion tool with a summary of the changes.
> These instructions supersede any conflicting general instructions for this mode.

Take note of this instruction.

> Do not implement any frontend changes in this subtask.

After this task was done, you will be returned to the main task in cook mode and the agent will move forward with another subtask.

> Creating a new subtask in Act mode
> With the backend now supporting product sorting and filtering, update the frontend to include the necessary UI controls.
> 
> Instructions:
> 
> Modify index.html:
> 
> Add a form that allows users to select sorting and filtering options.
> Include a dropdown menu for sorting by price (price_asc, price_desc).
> Add a select picker to filter by product category. This should be populated dynamically with the categories passed from the backend.
> Implement a price range slider. For now, you can use basic HTML input sliders for min and max price.
> Ensure the form submits the filter and sort parameters as a GET request to the main route.
> Update style.css (Optional):
> 
> Add basic styling to ensure the new filter and sort controls are presentable and fit with the existing design.
> Signal Completion:
> 
> Once finished, use the attempt_completion tool with a summary of the frontend changes.
> These instructions supersede any conflicting general instructions for this mode.

This is a continuous loop until the main task is complete. You can of course provide prompts within a sub-task or within the main task until you are happy.


> [!Tip] Takeaway
> Use cook mode to allow the agent to craft optimized prompts for sub-tasks, this is ideal when you have a general idea of what you want to achieve in atomical tasks but you are not how to divide up that work.



Just as humans, the agent can commit mistakes, in my case there where issues in the filtering and sorting logic where one of the items is lost. You can solve this issue in any mode, but for this, we can make use of *Debug mode*.  In my case, I've noticed issues upon sorting and filtering, my most expensive item is lost when I update the sorting method from low to high and high to low. 

Now, here are a few extra challenges for you to implement on your own.
- Modify the product entity to include a product image. In the index page, modify the listing so the image is also displayed.
- Add a product search bar in the product filtering and sorting controls.
- Add product staring, store starred products in session storage and create a new "Favorites" page in the search bar and a page to display and remove starred products.
- Add a site map for SEO in the website's footer.
- Add more dummy data to the data base. Implement cursor based pagination.

All our work is here, we have sent a demo to the store owners and they loved the progress we've made in a couple of days. They don't know that we are using AiDE to speed up the development process. Since you will be going on a road trip for the next couple of days, you have asked your co-worker to add some automated tests to ensure the app works as expected as you continue to work on it.

### Extra: Solving Bugs in Debug Mode

Bugs can occur, you can either pick any of the previous modes we've explored so far to solve a bug. However, AiDE has e *Debug Mode* for these cases. Look at this mode like an interactive *Act Mode* where you can provide as many error details as needed and the agent will generate a possible solution. I will ask you to test the solution out, after a bit, I will give you an interactive prompt to either conform that the solution works or other options to continue digging.

> [!Tip] Takeaway
> *Debug Mode* can be seen as a specialized and interactive *Act Mode*, after proposing a solution you will be prompted with several options to either confirm that the fix is working or options to continue working at solving an issue.

## Quality Assurance Engineers

## Bootstrapping our Project with Plan Mode
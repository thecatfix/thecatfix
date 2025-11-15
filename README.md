<img src="https://media.giphy.com/media/qsG9kDQCJYuiO9JOtS/giphy.gif" width="25%">

## Let me start by making one thing absolutely clear: I'm not a developer.

If you see a pull request from me, it was probably a mistake, OR I figured something out and you just stumbled upon someone who really wants to contribute. More than likely, it will be the former rather than the latter. <br> Github blows my mind because of its wealth of incredible resources and the vibrant community it hosts. <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaHJ0ZTA5bDI3bjhzbXI5a2c2cXB1dDlsaThjbHdzbm9sdGk5bWFmZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/TBf2czxR420jCORE0o/giphy.gif" width="5%"> <br> I clone, fork and paste code into my experiments in order to learn. <br>

### Here are my Gists

[Gists Home Page](https://gist.github.com/thecatfix)

### What Am I learning:<br>

<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTluenh0Z2d1dG9zMjFncTN5ZG94MGRibTB3cTdmOXIzYmd0dzVveCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/LpvRzoMpaL4FZkdXzM/giphy.gif" width="5%"> [All Things Google Cloud](https://www.credential.net/d704cea3-c104-4441-a13d-e6154ca5d750?utm_medium=profile&utm_source=linktree&utm_campaign=google%20cloud%20certification)

<img src="https://media.giphy.com/media/UtEd87cLAH789bR5sk/giphy.gif" width="5%"> [Python](https://automatetheboringstuff.com/)

<img src="https://media.giphy.com/media/GrPgFtvyLlgElFiO7m/giphy.gif" width="5%"> [Decision Science, Artificial Intelligence and Machine Learning](https://onlineexeced.mccombs.utexas.edu/online-ai-machine-learning-course)

# My Story

A stroke of serendipity brought me into the orbit of pioneering minds at ING and Katana Labs, where I played a key role in selling their state-of-the-art intellectual property that identified bond pair trades that were dislocated and would revert to their mean spread difference.

## Identifying Less Obvious Highly Correlated Pair Trades

If you're unfamiliar with pair trades or bonds, here's an example using Walmart (WMT) and Costco (COST) in the stock market. Both companies excel at selling products but have different business models. Costco sells in bulk and requires a membership, while Walmart has numerous stores and sells individual items. Their stock prices are highly correlated and usually move together.

Now, imagine Costco starts doing exceptionally well, and people flock to shop there. Their stock price surges, but Walmart's stock price remains relatively unchanged. This scenario is known as a "dislocation," where the stock prices of the two companies no longer move in tandem as they typically do.

A trader or money manager would notice this anomaly and think, "Costco and Walmart are usually priced similarly. Something unusual must be happening." They might decide to "short" Walmart (bet that its stock will go down) and "long" Costco (bet that its stock will go up). This strategy is known as a "pair trade."

The concept is that eventually, Costco and Walmart's stock prices will "revert to the mean," returning to their usual correlated movement. If Costco's stock price decreases and Walmart's increases, the trader or money manager profits from their pair trade.

Now, let's apply this concept to the fixed income market. Walmart and Costco might each have 20 or more active bonds. The correlation metrics for their bonds differ slightly from those for their stock prices due to different factors. Attributes such as industry, currency, and issuer rating remain consistent. While pair trades for highly correlated issuers are well known, Katana has solved the challenge of identifying less well-known highly correlated bond pairs that are predicted to revert to the mean with high confidence.

## How Does It Work?

Good question! When I first acquired the technology, I would have told you, "I have no idea, but these invoices from Google Cloud are not cheap!"

The technology was developed by a multidisciplinary team of experts in quantitative modeling, machine learning, distributed systems engineering, and financial markets trading. The team included a PhD in Astrophysics, a PhD in Statistics from Oxford University with post-doctoral research in next-generation sequencing data analysis, a 10-year veteran cloud systems engineer, and the former Global Head of Credit Trading at ING Bank with 20 years of financial markets experience. They had a unique combination of quantitative skills, machine learning expertise, distributed systems engineering, and deep domain knowledge that refined an intricate architecture pivotal in pinpointing mean-reverting fixed income pair trades.
In my opinion, they developed an ETL tool that was ahead of its time for the fixed income market. Of course, I am very biased because I own the technology, but this is all I have worked on for a long period of time. Trust me, your Excel spreadsheet or Power BI tool cannot do this. This is data engineering, and I can only try to understand.
The data pipelines utilize a scalable, distributed processing framework with Apache Beam to analyze vast amounts of bond reference and pricing data. The algorithm employs the Cartesian product to exhaustively compare each bond with every other bond, identifying highly correlated pairs.
A neural network was then used to forecast pairs with the highest probability of mean reversion. The service went to market in early 2020 (worst luck ever!) and delivered some very profitable pair trade ideas for the early adopters of the product.

## What is the Tech Stack?

I have been trying to come up with a good acronym, but if you can think of one, let me know. Here are the key components:

- **Languages and Frameworks**: Go, Node.js, JavaScript, TypeScript, React, Python
- **Databases**: PostgresDB
- **Hosting and Authentication**: Firebase
- **Cloud Platform**: Google Cloud Platform (GCP)
- **Data Processing**: Apache Beam
- **API**: GraphQL for connecting to Bloomberg Terminal and App Store
- **GCP Services**: Cloud Functions, BigQuery, GCP data storage, and more, totaling about 25 services
- **Bonus**: Frontend includes an application on the Bloomberg App Store

## What Have I Been Doing with the Product?

I've been focusing on cutting costs without touching a line of code by identifying which cloud services can be turned off and which need to be retained for a minimal architecture. Imagine my surprise when I discovered Terraform and then found Terraform files scattered throughout our mono-repo!
I've had to dive into the deep end to control costs effectively. I am immersed in the complexities of pair trading strategies, data engineering (ETL, ELT, Big Data… you name it), and cloud-based platforms. I'm always actively exploring a range of technologies to deepen my understanding of what I own and how to make it more cost-efficient.
My learning curve has been steep, and I currently consider myself a student. I've been gaining knowledge from The University of Texas, where I completed the Cloud Computing program and am currently enrolled in the Full Stack Development program. It might not be the formal McCombs School of Business, but it's damn good.

## What Now?

My plan for the future is to leverage all that I've learned to build a product and business plan suited for the market. While Katana was originally designed for fixed income, I'm discovering that it has many more potential use cases.

### 'It’s down there somewhere, let me take another look,'

<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGFlOThkcHIxYWdobjE0ODQ0djg3MTdkczFydzBqb2o2b2t2eHl1byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JPmjZal3DjRLGMAAxL/giphy.gif" width="50%">

### Posts From The Soggy Blog

<!-- BLOG-POST-LIST:START -->

- [The LEI is the key &amp;#38; the key is the LEI](https://www.catfix.biz/posts/the-lei-is-the-key-the-key-is-the-lei)
- [Where the hell did my axe go?](https://www.catfix.biz/posts/where-the-hell-did-my-axe-go)
- [Sooooo.....that&#39;s what a cluster is!!!](https://www.catfix.biz/posts/explain_a_cluster_to_me_as_if_i_was_15)
- [Explaining Software Development for the Rest of Us](https://www.catfix.biz/posts/explaining-software-development-for-the-rest-of-us)
- [Quick History of Apache Beam](https://www.catfix.biz/posts/beam-history)<!-- BLOG-POST-LIST:END -->

## ⭐ thecatfix's Latest Starred Repositories

- [archcraft-os/archcraft](https://github.com/archcraft-os/archcraft): // Source : ISO
- [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills): A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows — particularly Claude Code
- [and-rs/dotfiles](https://github.com/and-rs/dotfiles): i love fzf
- [superstarryeyes/lue](https://github.com/superstarryeyes/lue): Terminal eBook Reader with Audiobook-quality Text-to-Speech Narration 
- [ThePrimeagen/dev](https://github.com/ThePrimeagen/dev): my next gen build for starting my system
- [ThePrimeagen/tmux-sessionizer](https://github.com/ThePrimeagen/tmux-sessionizer): 
- [nektos/act](https://github.com/nektos/act): Run your GitHub Actions locally 🚀
- [yks0000/starred-repo-toc](https://github.com/yks0000/starred-repo-toc): Generates Markdown table for all Starred Repositories by a GitHub user.
- [Dicklesworthstone/mcp_agent_mail](https://github.com/Dicklesworthstone/mcp_agent_mail): Like gmail for your coding agents. Lets various different agents communicate and coordinate with each other.
- [LazyVim/lazyvim.github.io](https://github.com/LazyVim/lazyvim.github.io): LazyVim Website
- [okuuva/auto-save.nvim](https://github.com/okuuva/auto-save.nvim): 🧶 Automatically save your changes in NeoVim
- [OXY2DEV/markview.nvim](https://github.com/OXY2DEV/markview.nvim): A hackable markdown, Typst, latex, html(inline) & YAML previewer for Neovim
- [numToStr/Comment.nvim](https://github.com/numToStr/Comment.nvim): :brain: :muscle: // Smart and powerful comment plugin for neovim. Supports treesitter, dot repeat, left-right/up-down motions, hooks, and more
- [folke/snacks.nvim](https://github.com/folke/snacks.nvim): 🍿 A collection of QoL plugins for Neovim
- [folke/flash.nvim](https://github.com/folke/flash.nvim): Navigate your code with search labels, enhanced character motions and Treesitter integration
- [SylvanFranklin/keyboard](https://github.com/SylvanFranklin/keyboard): 
- [tpope/vim-fugitive](https://github.com/tpope/vim-fugitive): fugitive.vim: A Git wrapper so awesome, it should be illegal
- [lambdalisue/nvim-aibo](https://github.com/lambdalisue/nvim-aibo): 🐶 Aibo -  AI Bot Integration and Orchestration for Neovim
- [karpathy/nanochat](https://github.com/karpathy/nanochat): The best ChatGPT that $100 can buy.
- [virattt/dexter](https://github.com/virattt/dexter): An autonomous agent for deep financial research
- [lewis6991/gitsigns.nvim](https://github.com/lewis6991/gitsigns.nvim): Git integration for buffers
- [nvim-mini/mini.diff](https://github.com/nvim-mini/mini.diff): Work with diff hunks. Part of 'mini.nvim' library. 
- [microsoft/amplifier](https://github.com/microsoft/amplifier): 
- [cloudflare/cloudflare-typescript](https://github.com/cloudflare/cloudflare-typescript): The official Typescript library for the Cloudflare API
- [anthropics/skills](https://github.com/anthropics/skills): Public repository for Skills
- [imputnet/helium](https://github.com/imputnet/helium): Private, fast, and honest web browser
- [github/spec-kit](https://github.com/github/spec-kit): 💫 Toolkit to help you get started with Spec-Driven Development
- [colin-ho/Sashimi4Talent](https://github.com/colin-ho/Sashimi4Talent): 
- [steveyegge/beads](https://github.com/steveyegge/beads): Beads - A memory upgrade for your coding agent
- [zbirenbaum/copilot.lua](https://github.com/zbirenbaum/copilot.lua): Fully featured & enhanced replacement for copilot.vim complete with API for interacting with Github Copilot
- [firecrawl/firecrawl-app-examples](https://github.com/firecrawl/firecrawl-app-examples): 🔥 This repository contains complete application examples, including websites and other projects, developed using Firecrawl.
- [nvim-lualine/lualine.nvim](https://github.com/nvim-lualine/lualine.nvim): A blazing fast and easy to configure neovim statusline plugin written in pure lua.
- [github/copilot.vim](https://github.com/github/copilot.vim): Neovim plugin for GitHub Copilot
- [qdrant/mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant): An official Qdrant Model Context Protocol (MCP) server implementation
- [datalab-to/marker](https://github.com/datalab-to/marker): Convert PDF to markdown + JSON quickly with high accuracy
- [asadm/markdowndown](https://github.com/asadm/markdowndown): 
- [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master): An AI-powered task-management system you can drop into Cursor, Lovable, Windsurf, Roo, and others.
- [neovim/neovim.github.io](https://github.com/neovim/neovim.github.io): Neovim website
- [mastra-ai/mastra](https://github.com/mastra-ai/mastra): The TypeScript AI agent framework. ⚡ Assistants, RAG, observability. Supports any LLM: GPT-4, Claude, Gemini, Llama.
- [snarktank/code-editing-agent](https://github.com/snarktank/code-editing-agent): A simple AI developer agent
- [snarktank/ai-dev-tasks](https://github.com/snarktank/ai-dev-tasks): A simple task management system for managing AI dev agents
- [snarktank/ai-pr-review](https://github.com/snarktank/ai-pr-review): A robust GitHub Actions workflow that provides AI-powered code reviews using Amp or Claude Code
- [starship/starship](https://github.com/starship/starship): ☄🌌️  The minimal, blazing-fast, and infinitely customizable prompt for any shell!
- [aciidic/thegreatsuspender-notrack](https://github.com/aciidic/thegreatsuspender-notrack): A chrome extension for suspending all tabs to free up memory, privacy-oriented with no analytics tracking.
- [gradle/gradle](https://github.com/gradle/gradle): Adaptable, fast automation for all
- [cashapp/licensee](https://github.com/cashapp/licensee): Gradle plugin which validates the licenses of your dependency graph match what you expect
- [deepseek-ai/DeepSeek-V3.2-Exp](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp): 
- [sjarmak/deploy-sourcegraph-docker](https://github.com/sjarmak/deploy-sourcegraph-docker): Sourcegraph with Docker Compose deployment reference
- [sjarmak/amp-orchestra-sdk](https://github.com/sjarmak/amp-orchestra-sdk): 
- [sourcegraph-sj/amp-session-orchestrator](https://github.com/sourcegraph-sj/amp-session-orchestrator): 
- [sphamba/smear-cursor.nvim](https://github.com/sphamba/smear-cursor.nvim): 🌠 Neovim plugin to animate the cursor with a smear effect in all terminals
- [folke/dot](https://github.com/folke/dot): ☕️   My Dot Files
- [yusukebe/gh-markdown-preview](https://github.com/yusukebe/gh-markdown-preview): GitHub CLI extension to preview Markdown looks like GitHub.
- [folke/sidekick.nvim](https://github.com/folke/sidekick.nvim): Your Neovim AI sidekick
- [stefanoamorelli/sec-edgar-toolkit](https://github.com/stefanoamorelli/sec-edgar-toolkit): 🏛️ Open-source toolkit for accessing SEC EDGAR financial data with Python and TypeScript/JavaScript SDKs. Features comprehensive parsing for 10-K, 10-Q, 8-K forms, XBRL financial data extraction, and real-time company filings retrieval.
- [bahdotsh/blogr](https://github.com/bahdotsh/blogr): Write, edit, and publish your blog without ever leaving your terminal!
- [shadcn/cult-ui](https://github.com/shadcn/cult-ui): Components crafted for Design Engineers. Styled using Tailwind CSS, fully compatible with Shadcn, and easy to integrate—just copy and paste. MIT 🤌
- [dive-into-machine-learning/dive-into-machine-learning](https://github.com/dive-into-machine-learning/dive-into-machine-learning): Free ways to dive into machine learning with Python and Jupyter Notebook. Notebooks, courses, and other links. (First posted in 2016.)
- [eriklindernoren/ML-From-Scratch](https://github.com/eriklindernoren/ML-From-Scratch): Machine Learning From Scratch. Bare bones NumPy implementations of machine learning models and algorithms with a focus on accessibility. Aims to cover everything from linear regression to deep learning.
- [shadcn-ui/ui](https://github.com/shadcn-ui/ui): A set of beautifully-designed, accessible components and a code distribution platform. Works with your favorite frameworks. Open Source. Open Code.
- [Kiranism/next-shadcn-dashboard-starter](https://github.com/Kiranism/next-shadcn-dashboard-starter): Admin Dashboard Starter with Nextjs 15 and Shadcn ui
- [DariusLukasukas/stocks](https://github.com/DariusLukasukas/stocks): Modern stock tracking application built with Next.js 14, React.js, Shadcn and Tailwind CSS. Leverages the Yahoo Finance API for real-time quotes, company financials, customizable charts, and relevant market news.
- [neovim/tree-sitter-vimdoc](https://github.com/neovim/tree-sitter-vimdoc): Tree-sitter parser for Vim help files
- [nanotee/nvim-lua-guide](https://github.com/nanotee/nvim-lua-guide): A guide to using Lua in Neovim
- [pim97/scrappey.js](https://github.com/pim97/scrappey.js):  Scrappey.js: A versatile JavaScript wrapper for Scrappey API for solving Cloudflare, datadome, enabling seamless web scraping of anti-bot protected websites. Simplify data extraction with robust functionality and reliable results. Unlock valuable insights effortlessly. Get started with Scrappey
- [nvim-mini/mini.nvim](https://github.com/nvim-mini/mini.nvim): Library of 40+ independent Lua modules improving Neovim experience with minimal effort
- [shreyas44/s3-url-handler](https://github.com/shreyas44/s3-url-handler): 
- [allyourcodebase/ffmpeg](https://github.com/allyourcodebase/ffmpeg): FFmpeg Zig package
- [seatedro/glyph](https://github.com/seatedro/glyph): convert images, video to ascii!
- [Sin-cy/dotfiles](https://github.com/Sin-cy/dotfiles): ⌨️ The never ending updates of my dotfiles config
- [trailofbits/mcp-context-protector](https://github.com/trailofbits/mcp-context-protector): MCP security wrapper
- [BlueBubblesApp/bluebubbles-server](https://github.com/BlueBubblesApp/bluebubbles-server): Server for forwarding iMessages to clients within the BlueBubbles App ecosystem
- [ThariqS/ClaudeCodeSDK-EmailAgentExample](https://github.com/ThariqS/ClaudeCodeSDK-EmailAgentExample): 
- [oxsecurity/megalinter](https://github.com/oxsecurity/megalinter): 🦙 MegaLinter analyzes 50 languages, 22 formats, 21 tooling formats, excessive copy-pastes, spelling mistakes and security issues in your repository sources with a GitHub Action, other CI tools or locally.
- [specpulse/specpulse](https://github.com/specpulse/specpulse): Specification-Driven Development (SDD) Framework
- [popcorntime/popcorntime](https://github.com/popcorntime/popcorntime): Popcorn Time™ puts everything in one place. Your favorite platforms, your shows, your movies-ready when you are.
- [jorhelp/LinuxDotfiles](https://github.com/jorhelp/LinuxDotfiles): Some config files for Linux
- [theja-m/Data-Structures-and-Algorithms](https://github.com/theja-m/Data-Structures-and-Algorithms): Data Structures and Algorithms in Python
- [L3MON4D3/LuaSnip](https://github.com/L3MON4D3/LuaSnip): Snippet Engine for Neovim written in Lua.
- [ejmastnak/dotfiles](https://github.com/ejmastnak/dotfiles): ejmastnak's dotfiles
- [Bisiar/mcp-snagit](https://github.com/Bisiar/mcp-snagit): A Model Context Protocol server for Snagit screen capture integration
- [xdevplatform/xurl](https://github.com/xdevplatform/xurl): OAuth2.0 enabled curl for the X API
- [dontriskit/awesome-ai-system-prompts](https://github.com/dontriskit/awesome-ai-system-prompts): 🧠 Curated collection of system prompts for top AI tools. Perfect for AI agent builders and prompt engineers. Incuding: ChatGPT, Claude, Perplexity, Manus, Claude-Code, Loveable, v0, Grok, same new, windsurf, notion, and MetaAI. 
- [firecrawl/open-lovable](https://github.com/firecrawl/open-lovable): 🔥 Clone and recreate any website as a modern React app in seconds
- [stevearc/oil.nvim](https://github.com/stevearc/oil.nvim): Neovim file explorer: edit your filesystem like a buffer
- [Eventual-Inc/Daft](https://github.com/Eventual-Inc/Daft): Distributed query engine providing simple and reliable data processing for any modality and scale
- [GothenburgBitFactory/clog](https://github.com/GothenburgBitFactory/clog): Clog is a colorized log tail utility
- [facundoolano/google-play-scraper](https://github.com/facundoolano/google-play-scraper): Node.js scraper to get data from Google Play
- [GothenburgBitFactory/timewarrior](https://github.com/GothenburgBitFactory/timewarrior): Timewarrior - Commandline Time Tracking and Reporting
- [vague-theme/vague.nvim](https://github.com/vague-theme/vague.nvim): A cool, dark, low contrast colorscheme for Neovim. Pastel yet vivid, like a fleeting memory...
- [Myriad-Dreamin/tinymist](https://github.com/Myriad-Dreamin/tinymist): Tinymist [ˈtaɪni mɪst] is an integrated language service for Typst [taɪpst].
- [chomosuke/typst-preview.nvim](https://github.com/chomosuke/typst-preview.nvim): Low latency typst preview for Neovim
- [hulufei/diary.nvim](https://github.com/hulufei/diary.nvim): A simple and efficient diary plugin for Neovim
- [toppair/peek.nvim](https://github.com/toppair/peek.nvim): Markdown preview plugin for Neovim
- [wallpants/github-preview.nvim](https://github.com/wallpants/github-preview.nvim): Live Preview of your Markdown (GFM) files & local git repositories for Neovim.
- [MeanderingProgrammer/render-markdown.nvim](https://github.com/MeanderingProgrammer/render-markdown.nvim): Plugin to improve viewing Markdown files in Neovim
- [hat0uma/csvview.nvim](https://github.com/hat0uma/csvview.nvim): A Neovim plugin for CSV file editing.
- [brianhuster/live-preview.nvim](https://github.com/brianhuster/live-preview.nvim): A Live Preview Plugin for Neovim that allows you to view Markdown, HTML (along with CSS, JavaScript), AsciiDoc, SVG files in a web browser with live updates.
- [SylvanFranklin/omni-preview.nvim](https://github.com/SylvanFranklin/omni-preview.nvim): Manage previews for all filetypes in neovim
- [SylvanFranklin/.config](https://github.com/SylvanFranklin/.config): Secret Forum

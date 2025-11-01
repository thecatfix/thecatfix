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

- [nektos/act](https://github.com/nektos/act): Run your GitHub Actions locally 🚀
- [yks0000/starred-repo-toc](https://github.com/yks0000/starred-repo-toc): Generates Markdown table for all Starred Repositories by a GitHub user.

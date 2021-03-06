# Django-Blog

A blog system build with `Python 3.7.3` and `Django 2.2.7`.

# Main Features

- Recent Articles, Archives, Categories, Tags. Articles support `Markdown` language.
- Comment feature. Users can comment on each article with user name and email.
- Generate excerpt automatically. Extract the first 54 characters of each article as its excerpt.
- Generate table of contents automatically for articles.
- Sidebar features: tags, categories etc.

This project is still in building status. I will add more features to this project in the future!

# Other features

- Search engine
- Sign in 
- Generate some statistics for each article.
- Get notified if someone commented on the article.
- etc.

# Degisn 

This project has mainly two apps called blog and comments. One is reponsible for the basic functions of the blog system. The other one is reponsible for the comment system used for storing the comments of articles. 

In the blog app, there are three models. They are `Categorys`, `Posts` and  `Tags`. We can assign each article to different categorys and tags. In the comment app, there is only one model called `Comments`. In order to comment on an article, users have to send their names and emails addresses to the system. 

# Database Engine

We use `SQLite3` as the database system which is embeded in the Django framework. SQLite is lightweight and can be used for internal data storage. We can also use MySQL as the database system. But for our blog system, it is enough for us to use SQLite.

# Sample GUI Screenshots 

At present, this blog system can only be run in local environment. 

**The Homepage**

![Homepage](https://res.cloudinary.com/dq4ytg1fv/image/upload/v1579544105/Homepage_b9txw1.png)

**Article Page**

![ArticlePage](https://res.cloudinary.com/dq4ytg1fv/image/upload/v1579544847/ArticlePage_hluvsv.png)

**Markdown and TOC Support**

![MarkdownSupport](https://res.cloudinary.com/dq4ytg1fv/image/upload/v1579544847/MarkdownSupport_kawqyd.png)

# Special Thanks

Thanks to the free Django tutorial posted by yangxg. Here is a [Link](https://github.com/HelloGitHub-Team/HelloDjango-blog-tutorial) of the tutorial. 

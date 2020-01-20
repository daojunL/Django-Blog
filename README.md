# Django-Blog
A blog system build with `Python 3.7.3` and `Django 2.2.7`

[![license](https://img.shields.io/github/license/liangliangyy/djangoblog.svg)]()  

# Main Features:
- Recent Articles, Archives, Categories, Tags. Articles support `Markdown` language.
- Comment feature. Users can comment to each article with user name and email.
- Generate excerpt automately. Extract the first 54 characters of each article as its excerpt.
- Generate table of contents automately for articles.
- Sidebar features: tags, categories etc.

This project is still in building status. I will add more features to this project in the future!

# Other features includes:

- Search engine
- Sign in 
- Generate some statistics for each article.
- Get notified if someone commented on the article.
- etc.

# Degisn 

This project has mainly two apps called blog and comments. One is reponsible for the basic functions of the blog system. The other one is reponsible for the comment system used for storing the comments of articles. 

In the blog app, there are three models. They are `Categorys`, `Posts` and  `Tags`. We can assign each article to different categorys and tags. In the comment app, there is only one model called `Comments`. In order to comment an article, users have to send their names and emails addresses to the system. 

# Database Engine

We use `SQLite3` as the database system which is embeded in the Django framework. SQLite is lightweight and can be used for internal data storage. We can also use MySQL as the database system. But for our blog system, it is enough for us to use SQLite.

# Sample GUI Screenshots 

For present, this blog system can only be run in local environment. 

**The Homepage**

![Homepage](https://res.cloudinary.com/dq4ytg1fv/image/upload/v1579544105/Homepage_b9txw1.png)

**Article Page**

![ArticlePage](https://res.cloudinary.com/dq4ytg1fv/image/upload/v1579544105/ArticlePage_uwjn6f.png)

**Markdown and TOC Support**

![MarkdownSupport](https://res.cloudinary.com/dq4ytg1fv/image/upload/v1579544105/MarkdownSupport_c3vwag.png)

# Special Thanks

Thanks to the free Django tutorial posted by yangxg. Here is [Link](https://github.com/HelloGitHub-Team/HelloDjango-blog-tutorial) of the tutorial. 

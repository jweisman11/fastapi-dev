<!-- Inspo for creating a great README -->
<!-- https://github.com/othneildrew/Best-README-Template/tree/master#readme-top -->


<!-- Create anchor for "back to top" links -->
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<div align="center">
   
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
</div>

<!-- PROJECT LOGO -->
<div align="center">
  <a href="https://github.com/jweisman11/fastapi-dev">
    <img src="images/zoidberg.png" alt="Zoidberg" width="80" height="120">
  </a>

</div>

# Zoidberg API




## Features

General Items
* Containerization using Docker
* WSGI server - likely Unicorn
* Web Proxy - NGINX ?
* Logging with Graylog using graypy
* TBD

Backend
* Pydantic models for data validation
* JWT tokens
* Authentication & Authorization ??
* Strawberry for GraphQL
* HTTPS
* Rate limiting feature
* Pagination
* Sorting
* Filtering
* Task Scheduling and Background Jobs with a Job Queue
* CORS
* Custom middlewear
* Prevent SQL injection attack
* TBD

Frontend
* Analytics Dashboard with Data Visualization of API usage
* TBD




## Best Practices

* Resource names should be known -> /carts
* Resource names should be plural -> items
* All endpoints should be versioned -> /v1/items
* Resource "cross reference" each other -> /carts/{123}/items/{123} 

## Resource

* https://python.plainenglish.io/a-comprehensive-guide-to-structuring-a-fastapi-project-for-reproducibility-and-maintainability-1705c41dac41
* https://medium.com/@alamincoders/a-complete-api-development-guide-common-terms-tools-and-best-practices-7bd9abba4624
* https://github.com/zhanymkanov/fastapi-best-practices





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/jweisman11/fastapi-dev.svg?style=for-the-badge
[contributors-url]: https://github.com/jweisman11/fastapi-dev/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jweisman11/fastapi-dev.svg?style=for-the-badge
[forks-url]: https://github.com/jweisman11/fastapi-dev/network/members
[stars-shield]: https://img.shields.io/github/stars/jweisman11/fastapi-dev.svg?style=for-the-badge
[stars-url]: https://github.com/jweisman11/fastapi-dev/stargazers
[issues-shield]: https://img.shields.io/github/issues/jweisman11/fastapi-dev.svg?style=for-the-badge
[issues-url]: "https://github.com/jweisman11/fastapi-dev/issues"

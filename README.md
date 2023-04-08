<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a name="readme-top"></a>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->

<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
<!-- PROJECT LOGO -->

<br />
<div align="center">
  <a href="https://github.com/AlexGarciaG/networkchuck_pihole_for_arm">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">networkchuck_pihole_for_arm</h3>

<p align="center">
    Recreation of “thenetworkchuck/networkchuck_pihole” container for arm architecture.
    <br />
    <a href="https://github.com/AlexGarciaG/networkchuck_pihole_for_arm"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/AlexGarciaG/networkchuck_pihole_for_arm">View Demo</a>
    ·
    <a href="https://github.com/AlexGarciaG/networkchuck_pihole_for_arm/issues">Report Bug</a>
    ·
    <a href="https://github.com/AlexGarciaG/networkchuck_pihole_for_arm/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Currently, there is no official way to deploy the "thenetworkchuck/networkchuck_pihole" container on a Raspberry Pi, as it was designed specifically for the amd64 architecture. However, this issue can be addressed by utilizing the latest container from "pihole/pihole," which supports the arm architecture. To recreate the "thenetworkchuck/networkchuck_pihole" container for arm architecture, the scripts made by NetworkChuck will be integrated into the pihole container.

In addition to this, several enhancements will be made to improve the user experience. For instance, the API for blocking and unlocking will be set to auto-start when the container is deployed. The addition of logs will also be implemented for better debugging and monitoring. Furthermore, users will have the option to create multiple lists of blocking websites, providing them with greater control over their network security.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
* [![Python][Python.js]][Python-url]
* [![Flask][Flask.js]][Flask-url]
* [![Docker][Docker.js]][Docker-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

Install Docker by following the official documentation [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/AlexGarciaG/networkchuck_pihole_for_arm.git
   ```
2. Compile the docker file
   ```sh
   cd networkchuck_pihole_for_arm/docker
   docker build -t networkchuck_pihole_for_arm -f Dockerfile .
   ```
3. Deploy container 
    1. Using Network Chuck’s script , which was modified to use the container for arm.

      Modify pihole.sh “-v "/myPath:/home/network" \” line 14  to the path were you will edit and create your domain list files. 

        ```sh
        cd networkchuck_pihole_for_arm/
        sudo chmod u+x ./pihole.sh
        sudo ./pihole.sh
        ```

    2. Using a yaml file witch based on the [pihole/pihole](https://hub.docker.com/r/pihole/pihole) container. 

      Change “- /my_path:/home/network”  from the yaml in the “volumes:” to the path were you will edit and create your domain list files. 
        
        
        ```yaml
          # More info at https://github.com/pi-hole/docker-pi-hole/ and https://docs.pi-hole.net/
          services:
            pihole:
              container_name: pihole
              image: networkchuck_pihole_for_arm
              # For DHCP it is recommended to remove these ports and instead add: network_mode: "host"
              ports:
                - "53:53/tcp"
                - "53:53/udp"
                - "67:67/udp" # Only required if you are using Pi-hole as your DHCP server
                - "8080:80/tcp"
                - "8081:8080"
              environment:
                TZ: 'America/Chicago'
                WEBPASSWORD: 'cd6akobKg3i94kQKMWD*_aCcqN4_JD'
              # Volumes store your data between container upgrades
              volumes:
                - './etc-pihole:/etc/pihole'
                - './etc-dnsmasq.d:/etc/dnsmasq.d'
                - /my_path:/home/network
              #   https://github.com/pi-hole/docker-pi-hole#note-on-capabilities
              cap_add:
                - NET_ADMIN # Required if you are using Pi-hole as your DHCP server, else not needed
              restart: unless-stopped
        ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

The current version no longer works as the original version [BLOCK EVERYTHING w/ PiHole on Docker, OpenDNS and IFTTT](https://www.youtube.com/watch?v=dH3DdLy574M&t=934s) . To use the new version check the following tutorial.
If we wish to have control over our favorite entertainment  websites like Netflix, Disney +, Prime Video and YouTube, the steps are: 
1. Create a domain list. 
  
  Create a copy of ` template.sh` and rename, example `entertainment.sh` and change domain1, domain2, domain3,.. to the desired domains.
    ```sh
    '(^|\.)Netflix\.com$' '(^|\.)disneyplus\.com$' '(^|\.)primevideo\.com$' '(^|\.)youtube\.com$'
    ```
  
  Note: The format '(^|\.)domain1\.com$' is used to block anything related to that domain. If you want to be more specific check the [Pi-hole documentation](https://docs.pi-hole.net/regex/tutorial/)

2. Block domain list.

  Send a POST request to ` http://localhost:8080/block` with the body 
    ```
    {
      "list_name": "blockdomains.sh"
    }
    ```

3. Unblock domain list

  Send a POST request to ` http://localhost:8080/unblock` with the body 
    ```
    {
      "list_name": "blockdomains.sh"
    }
    ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [X] Recreate original container for arm.
- [X] Execute the API for blocking and unlocking when the container is deployed
- [ ] Add option to create multiple lists of blocking websites
    - [x] Using files.
    - [ ] Using data bases.
- [ ] Add Logs for better debugging and monitoring

See the [open issues](https://github.com/AlexGarciaG/networkchuck_pihole_for_arm/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Your Name - Alexis Garcia Gutierrez - contact@alexgarciag.com

Project Link: [https://github.com/AlexGarciaG/networkchuck_pihole_for_arm](https://github.com/AlexGarciaG/networkchuck_pihole_for_arm)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

* [NetworkChuck](https://www.youtube.com/@NetworkChuck)
* [othneildrew](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/AlexGarciaG/networkchuck_pihole_for_arm.svg?style=for-the-badge
[contributors-url]: https://github.com/AlexGarciaG/networkchuck_pihole_for_arm/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AlexGarciaG/networkchuck_pihole_for_arm.svg?style=for-the-badge
[forks-url]: https://github.com/AlexGarciaG/networkchuck_pihole_for_arm/network/members
[stars-shield]: https://img.shields.io/github/stars/AlexGarciaG/networkchuck_pihole_for_arm.svg?style=for-the-badge
[stars-url]: https://github.com/AlexGarciaG/networkchuck_pihole_for_arm/stargazers
[issues-shield]: https://img.shields.io/github/issues/AlexGarciaG/networkchuck_pihole_for_arm.svg?style=for-the-badge
[issues-url]: https://github.com/AlexGarciaG/networkchuck_pihole_for_arm/issues
[license-shield]: https://img.shields.io/github/license/AlexGarciaG/networkchuck_pihole_for_arm.svg?style=for-the-badge
[license-url]: https://github.com/AlexGarciaG/networkchuck_pihole_for_arm/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/garcia-alexis
[product-screenshot]: images/screenshot.png
[Python.js]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Flask.js]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/2.2.x/
[Docker.js]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/

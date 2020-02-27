<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/LouisKlimek/Reddit2Video">
    <img src="images/logo.png" alt="Reddit2Video" width="80" height="80">
  </a>

  <h3 align="center">Reddit2Video</h3>

  <p align="center">
    With Reddit2Video you can create AskReddit Text2Speech Videos just by specifying your wished Video Length.
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Contributing](#contributing)
* [License](#license)



<!-- ABOUT THE PROJECT -->
## About The Project

With this Project i tried to create an easy to use Tool which you use to generate AskReddit Text2Speech Videos.

### Built With
To make it all work the Project uses:
* [Python](https://www.python.org/)
* [FFmpeg](https://ffmpeg.org/)
* [IBM Watson Text to Speech](https://www.ibm.com/cloud/watson-text-to-speech)


<!-- GETTING STARTED -->
## Getting Started

To set up the Project locally you will need
* Python
* FFmpeg
* A Reddit Account


### Installation

1. Clone the repo.
```sh
git clone https://github.com/LouisKlimek/Reddit2Video
```
3. Install FFmpeg.
```sh
https://ffmpeg.org/download.html#build-windows
```

4. Get your Reddit API Key.
```sh
https://www.reddit.com/wiki/api
```

5. Enter your API Key, Password etc. in "reddit.py".

6. Enter your "videoLengthInMin" in "reddit.py".

7. Now you can let "reddit.py" run and it will automatically create Videos.


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the Apache License 2.0. See `LICENSE` for more information.

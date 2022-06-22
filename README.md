# :film_strip: Insta To Video

Use photos of an Instagram account to create a short video.

You can upload this short video to TikTok, Youtube, Kwai, or any other platform.

## :ballot_box_with_check: Setup

Choose **one option**:

**1)** Run the `setup.py` file located in the root directory:

```shell
python setup.py
```

OR

**2)** Create a copy of the `.env.template` file, rename it to `.env`, and type your Instagram username and password.

## :page_with_curl: Usage

```shell
python src/main.py -m youtube_video_id -i instagram_username -d duration_in_seconds -n number_of_photos
```

**Options**

|         Option         |  Type   |      Required      |           Description            |
| :--------------------: | :-----: | :----------------: | :------------------------------: |
|      -m, --music       | string  | :heavy_check_mark: |     Youtube video ID or URL      |
|    -i, --instagram     | string  | :heavy_check_mark: |   Instagram username. Ex: nasa   |
|     -d, --duration     |  float  |        :x:         | Duration of the video in seconds |
| -n, --number_of_photos | integer |        :x:         |         Number of photos         |

## :file_folder: Examples

Check out the [examples folder](/examples) to see videos created using this library.

## :handshake: Contribution

Every contribution is appreciated :heart:. Check out the [issues](https://github.com/LuanEdCosta/insta-to-video/issues) tab to see how to contribute.

## :man: Author

Luan Eduardo da Costa | [Follow me on Linkedin](https://www.linkedin.com/in/luaneducosta/)

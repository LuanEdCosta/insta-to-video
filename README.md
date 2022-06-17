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

Example:

```shell
python src/main.py -m youtube_video_id -i instagram_username -d duration_in_seconds -n number_of_photos
```

**Options**

|         Option         |  Type  |      Required      |         Description          |
| :--------------------: | :----: | :----------------: | :--------------------------: |
|      -m, --music       | string | :heavy_check_mark: |   Youtube video ID or URL    |
|    -i, --instagram     | string | :heavy_check_mark: | Instagram username. Ex: nasa |
|     -d, --duration     | number |        :x:         |             :x:              |
| -n, --number_of_photos | number |        :x:         |             :x:              |

## :file_folder: Examples

Check out the [examples folder](/examples) to see videos created using this library.

## :man: Author

Luan Eduardo da Costa | [Follow me on Linkedin](https://www.linkedin.com/in/luaneducosta/)

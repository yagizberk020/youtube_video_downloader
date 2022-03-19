import pytube




def download_video(url, path):
    yt = pytube.YouTube(url)
    # Title of video
    print("Title: ", yt.title)
    # Number of views of video
    print("Number of views: ", yt.views)
    # Length of the video
    print("Length of video: ", yt.length, "seconds")
    # Description of video
    # print("Description: ", yt.description)
    # Rating
    print("Ratings: ", yt.rating)
    yt.streams.get_lowest_resolution().download(path)


    return True


def getpath():
    # get path from user and create if not exist
    # user enters path to save the video to
    path = input("please select path to download: ")

    # if no path provided save to a default directry
    if len(path) == 0:
        path = default_path
        print("using the default path")
    return path


default_path = "videos"
def main():
    # user enters video url to download
    url = input("Please enter youtube url: ")

    path = getpath()


    # download the video
    status = download_video(url, path)

    # inform the user about the result
    if status == True:
        print("Video downloaded to",path)
    else:
        print("Sorry we couldn't download the video")

if __name__ == '__main__':
    main()

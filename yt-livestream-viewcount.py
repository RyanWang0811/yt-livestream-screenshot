# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import json

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():

    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey="")

    request = youtube.videos().list(
        part="liveStreamingDetails",
        id="R2iMq5LKXco"
    )
    response = request.execute()
    concurrentViewers = response['items'][0]['liveStreamingDetails']['concurrentViewers']

    print(response)
    print(concurrentViewers)


if __name__ == "__main__":
    main()

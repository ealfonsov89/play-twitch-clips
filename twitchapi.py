import json
import requests

grant_type = 'client_credentials'

def get_access_token(client_id, client_secret, grant_type):
    url = f"https://id.twitch.tv/oauth2/token?client_id={client_id}&client_secret={client_secret}&grant_type={grant_type}"
    response = requests.request("POST", url)
    response_credential_data = json.loads(response.text)
    access_token = response_credential_data['access_token']
    return access_token

def get_broadcaster_id(client_id, chanel_name, access_token):
    url = f"https://api.twitch.tv/helix/users?login={chanel_name}"
    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.request("GET", url, headers=headers)
    response_user_data = json.loads(response.text)
    
    return response_user_data['data'][0]['id']

def get_clips(client_id, access_token, broadcaster_id):
    url = f"https://api.twitch.tv/helix/clips?broadcaster_id={broadcaster_id}&first=100"
    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.request("GET", url, headers=headers)
    response_data = json.loads(response.text)
    data = response_data['data']
    
    return data

def prepare_donwload_clip_url(clip):
    thumbnail_url: str = clip.get('thumbnail_url')
    video_id = thumbnail_url.removeprefix('https://clips-media-assets2.twitch.tv/').split('-preview-')[0]
    direct_video_url = f"https://clips-media-assets2.twitch.tv/{video_id}.mp4"

    return direct_video_url



def get_play_list(channel_name, client_id, client_secret):
    access_token = get_access_token(client_id, client_secret, grant_type)
    broadcaster_id = get_broadcaster_id(client_id, channel_name, access_token)
    data = get_clips(client_id, access_token, broadcaster_id)
    clip_urls = []

    for clip in data:
        clip_url = prepare_donwload_clip_url(clip)
        clip_urls.append(clip_url)

    return clip_urls

if __name__ == '__main__':
    get_play_list('prettycludda')
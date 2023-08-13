import obspython as obs
import twitchapi


def script_description():
    return "Randomly play twitch clips"


twitch_channel = "twitch_channel"
vlc_source_name = "vlc_source_name"
twitch_client_id = "twitch_client_id"
twitch_access_token = "twitch_access_token"
client_id = "client_id"
client_secret = "client_secret"


def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_text(
        props, twitch_channel, "Twitch Channel", obs.OBS_TEXT_DEFAULT
    )
    obs.obs_properties_add_text(
        props, vlc_source_name, "VLC video source name", obs.OBS_TEXT_DEFAULT
    )
    obs.obs_properties_add_text(
        props, client_id, "Twitch client Id", obs.OBS_TEXT_DEFAULT
    )
    obs.obs_properties_add_text(
        props, client_secret, "twitch client secret", obs.OBS_TEXT_DEFAULT
    )
    return props


def push_clips_to_vlc_video(
    twitch_channel_property, vlc_source_name_property, client_id, client_secret
):
    clips = twitchapi.get_play_list(twitch_channel_property, client_id, client_secret)
    vlc_source = obs.obs_get_source_by_name(vlc_source_name_property)
    vlc_source_settings = obs.obs_source_get_settings(vlc_source)

    if vlc_source is not None:
        playlist = obs.obs_data_array_create()
        for clip in clips:
            if clip.endswith(".mp4"):
                item = obs.obs_data_create()
                obs.obs_data_set_string(item, "value", clip)
                obs.obs_data_set_bool(item, "selected", False)
                obs.obs_data_set_bool(item, "hidden", False)
                obs.obs_data_array_push_back(playlist, item)
                obs.obs_data_release(item)

        obs.obs_data_set_array(vlc_source_settings, "playlist", playlist)
        obs.obs_source_update(vlc_source, vlc_source_settings)

        obs.obs_data_array_release(playlist)
    obs.obs_source_release(vlc_source)
    obs.obs_data_release(vlc_source_settings)


def do_update(settings):
    twitch_channel_property = obs.obs_data_get_string(settings, twitch_channel)
    vlc_source_name_property = obs.obs_data_get_string(settings, vlc_source_name)
    client_id_property = obs.obs_data_get_string(settings, client_id)
    client_secret_property = obs.obs_data_get_string(settings, client_secret)
    if (
        twitch_channel is not None
        and vlc_source_name is not None
        and client_id is not None
        and client_secret is not None
    ):
        push_clips_to_vlc_video(
            twitch_channel_property,
            vlc_source_name_property,
            client_id_property,
            client_secret_property,
        )


def script_load(settings):
    do_update(settings)

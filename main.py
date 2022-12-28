from dandi.dandiapi import DandiAPIClient
dandiset_id = '000005'
filepath = "sub-anm184389/sub-anm184389_ses-20130207_behavior+ecephys.nwb"
with DandiAPIClient() as client:
    asset = client.get_dandiset(dandiset_id, 'draft').get_asset_by_path(filepath)
    s3_url = asset.get_content_url(follow_redirects=1, strip_query=True)

from pynwb import NWBHDF5IO

print('\nGot S3 URL:', s3_url)

print('\n-------------- Creating NWB IO Object --------------\n')
with NWBHDF5IO(s3_url, mode='r', load_namespaces=True, driver='ros3') as io:

    print('\n-------------- Begin streaming NWB data from S3 bucket... --------------\n')
    nwbfile = io.read()

    print('\n-------------- NWB File Contents --------------\n')
    print(nwbfile)
    # print(nwbfile.acquisition['lick_times'].time_series['lick_left_times'].data[:]) # This is not 

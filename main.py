# Import helper functions to track performance
from time import perf_counter

# Import DANDI API
from dandi.dandiapi import DandiAPIClient
dandiset_id = '000005'
filepath = "sub-anm184389/sub-anm184389_ses-20130207_behavior+ecephys.nwb"
with DandiAPIClient() as client:
    asset = client.get_dandiset(dandiset_id, 'draft').get_asset_by_path(filepath)
    s3_url = asset.get_content_url(follow_redirects=1, strip_query=True)
    print('\nGot S3 URL:', s3_url)


# from pynwb import NWBHDF5IO

# print('\n-------------- Step #1: Creating NWB IO Object --------------\n')
# t1_start = perf_counter()
# with NWBHDF5IO(
#     s3_url, 
#     mode='r', 
#     # load_namespaces=True, # Comment this to speed up Step #1
#     driver='ros3'
# ) as io:

#     t1_stop = perf_counter()    
#     print("Elapsed time:" ,t1_stop-t1_start)

#     print('\n-------------- Step #2: Begin streaming NWB data from S3 bucket... --------------\n')
#     t2_start = perf_counter()
#     nwbfile = io.read()
#     t2_stop = perf_counter()    
#     print("Elapsed time:" ,t2_stop-t2_start)

#     print('\n-------------- NWB File Contents --------------\n')
#     print(nwbfile)
#     # print(nwbfile.acquisition['lick_times'].time_series['lick_left_times'].data[:]) # This data is not available in the current dataset


import fsspec
import pynwb
import h5py
from fsspec.implementations.cached import CachingFileSystem

# first, create a virtual filesystem based on the http protocol and use
# caching to save accessed data to RAM.
fs = CachingFileSystem(
    fs=fsspec.filesystem("http"),
    cache_storage="nwb-cache",  # Local folder for the cache
)

# next, open the file
print('\n-------------- Step #1: Creating NWB IO Object --------------\n')
t1_start = perf_counter()
with fs.open(s3_url, "rb") as f:
    with h5py.File(f) as file:
        with pynwb.NWBHDF5IO(
            file=file, 
            load_namespaces=True
        ) as io:

            t1_stop = perf_counter()    
            print("Elapsed time:" ,t1_stop-t1_start)

            print('\n-------------- Step #2: Begin streaming NWB data from S3 bucket... --------------\n')
            t2_start = perf_counter()
            nwbfile = io.read()
            t2_stop = perf_counter()    
            print("Elapsed time:" ,t2_stop-t2_start)

            print('\n-------------- NWB File Contents --------------\n')
            print(nwbfile)
# JS8call_Scanner
Addon for JS8Call - scanner for 80, 40, 30 and 20 meters. I have devided the hour in 4 x 15 minute intervals, and each interval into 60 slots. I randomly transmit a beacon within one slot in each band. In this way the system could automatically find a suitable band for a JS8 connection, let’s say for emergency communication.
The band hopping had to be standardized, so that all stations would be on the same band at the same time. If we used 6 bands: 160, 80, 60, 40, 30 and 20 meters, the system would be very solid, with 10 minute intervals times 4 time slots. This system requires the use of a broadband antenna and/or an antenna tuner.
I initially used the JS8Call API and some code by Jeff Francis - https://github.com/jfrancis42.
I am a terrible programmer, but maybe someone out there could go through my code and clean it up! I am looking for someone experimenting together.
-> For more details and Python code follow this link: https://docs.google.com/document/d/1FTO3lXU46c4l8EWcBevSu4frgFRDZwWIr_KKcTz4-5U/edit?usp=sharing 

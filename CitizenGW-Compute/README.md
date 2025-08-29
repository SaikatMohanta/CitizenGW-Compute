# !CitizenGW-Compute!
--------------------------

**Citizen-driven timing anomaly experiment for gravitational wave events.**

This project proposes a **distributed citizen science platform** where normal 
computers log deterministic workloads during GW alerts (from LIGO/Virgo APIs) 
and anomalies in throughput are aggregated to explore possible correlations.

It is developed by myself only, so there may be several issues, 
that is why I pledge to all of the curious minds out there to come 
and contribute to this novel idea, and push this small program further.

I am open to any kind of contribution, suggestion, modification.
this project need YOU ....   **you are more valuable than you think**
----------

## Features:

- Deterministic ANN-like benchmark (NumPy/PyTorch).
- Event-triggered "logging mode" on GW alerts.
- Local CSV/JSON logging of performance metrics.
- Optional upload to a central Flask-based server.
- Designed for **Windows/Linux/MacOS** (Python 3.8+).

-------------

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SaikatMohanta/CitizenGW-Compute.git
   cd CitizenGW-Compute

-----------

2. Install dependencies:

pip install -r requirements.txt


-----------


##Usage
###Client

Run the client, listening for GW alerts and switching to logging mode:

python client.py --server http://127.0.0.1:5000/upload --alert-endpoint https://gwosc.org/api/


####If a GW alert is detected, you’ll be prompted:
GW ALERT received!
Switch system to logging mode? (y/n):

####Server
Start the minimal Flask server to collect logs:
python server_stub.py


####View logs in browser:
http://127.0.0.1:5000/logs

--------

##Roadmap

 - Real-time integration with LIGO/Virgo alert API.
 - Advanced ML-based anomaly correlation.
 - Visualization dashboards for citizen contributors.
 - Multi-user distributed logging network.

---------

##About GWOSC:

###Gravitational Wave Open Science Center:

The Gravitational Wave Open Science Center (GWOSC), formerly known as the LIGO Open Science Center, 
was created to provide public access to gravitational-wave data products. The collaborations running 
LIGO, Virgo, GEO600, and KAGRA have all agreed to use GWOSC services as the primary access points 
for public data products. This collaborative approach benefits users by creating a uniform interface 
to access data from multiple observatories, and provides cost savings to the various observatories 
by sharing the tools, services, and human resources.

###Public Data Policy:

Data from the above projects are made available to the public via the Gravitational Wave Open Science 
Center (GWOSC), as described in the LIGO Data Management Plan. All public data releases are managed by 
the LIGO, Virgo, and KAGRA collaborations, and GWOSC is jointly operated by these same organizations.


---------------

##The gravitational wave community forum:

A community for discussion of gravitational wave science with LIGO, Virgo, and KAGRA.

Link:  https://ask.igwn.org/

-----------
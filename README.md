#CitizenGW-Compute 🚀🌌
| From DESKTOP to the distant COSMOS |

Turning Computational Operations into a Gravitational Wave Sensor

CitizenGW-Compute is an open science initiative that reimagines your computer’s raw processing power as a virtual gravitational wave antenna. Instead of trying to detect tiny clock shifts directly (impossible at ~$10^{-21}$ strains), we treat the total number of operations per second as an amplification channel. By scaling tiny spacetime ripples into measurable deviations in throughput, everyday CPUs, GPUs, and even supercomputers can join in the hunt for gravitational waves.

##The vision:

Citizen PCs contribute idle compute cycles as sensitive probes.
HPC clusters & cloud systems (Azure, EAGLE, etc.) act as ultra-stable mega-detectors, triggered when LIGO/Virgo spot an event.
Collective correlation across thousands of devices boosts confidence and explores frequency bands beyond current interferometers.
In short: we turn computation itself into a scientific instrument, opening gravitational wave science to everyone. 🌍💻✨

It is developed by myself only, so there may be several issues, 
that is why I pledge to all of the curious minds out there to come 
and contribute to this novel idea, and push this small program further.

I am open to any kind of contribution, suggestion, modification. Also there is two PDFs available in the 'Docs' folder
of this Repo, please check it out, if you want to know the theoratical concept standing behind.
The project needs YOUR contribution & support ....   **you can be more valuable than you realise**

----------

##Features:

-Deterministic Dummy ANN-like benchmark (NumPy/PyTorch).
-Event-triggered "logging mode" on GW alerts.
-Local CSV/JSON logging of performance metrics.
-Optional upload to a central Flask-based server.
-Designed for **Windows/Linux/MacOS** (Python 3.8+).

-------------

##Installation

1.Clone the repository:
   ```bash
   git clone https://github.com/SaikatMohanta/CitizenGW-Compute.git
   cd CitizenGW-Compute
   ```
  
-----------

2.Install dependencies:

pip install -r requirements.txt


-----------


##Usage

###Client

Run the client, listening for GW alerts and switching to logging mode:

python client.py --server http://127.0.0.1:5000/upload --alert-endpoint https://gwosc.org/api/

Below is example on how to fetch data from our API in python languages. 
For more details do visit:  https://gwosc.org/api/

```bash
import requests
r = requests.get(
  "https://gwosc.org/api/v2/runs"
  )
r.json()
```

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

Please visit:  https://ask.igwn.org/


-----------



###### Note: 
- We are assuming a 1st or 5th floor demarc and a demarc extension that will allow us to place an EF and an ER on the second floor
- Primary ER will contain:
	- Core switch, firewall, wlc, company servers
- Distribution switches will be located either TR A or B on floor 2
	- redundant connection between distribution switches

###### CORE Switch
- 1x Cisco Catalyst 9300X - 24 ports (managed)
	- https://www.cdw.ca/product/cisco-catalyst-9300x-network-advantage-switch-24-ports-managed-ra/6550809?pfm=srh
###### DISTRIBUTION Switches
- 2x Cisco Catalyst 9300X - 24 ports (managed)
	- https://www.cdw.ca/product/cisco-catalyst-9300x-network-advantage-switch-24-ports-managed-ra/6550809?pfm=srh
###### ACCESS Switches
- 8x Cisco Business 350 Series CBS350-24FP-4X - 24 Port Access (managed)
	- https://www.cdw.ca/product/cisco-business-350-series-cbs350-24fp-4x-switch-24-ports-managed-ra/6309673?pfm=srh
- 8x Cisco Business 350 Series CBS350-48FP-4X - 48 Port Access (managed)
	- https://www.cdw.ca/product/cisco-business-350-series-cbs350-48fp-4x-switch-48-ports-managed-ra/6309668?pfm=srh
###### Firewall
- 1x Cisco FirePOWER 3140 Next-Generation Firewall
	- https://www.cdw.ca/product/cisco-firepower-3140-next-generation-firewall-firewall/7310376?pfm=srh
###### SFP Modules
- (x48) Cisco - SFP+ transceiver module - 10GbE
	- https://www.cdw.ca/product/cisco-sfp-transceiver-module-10gbe/3639620?pfm=srh
	- 32 are required to uplink from distribution to access
	- 16 are required to connect core to distribution
		- 4 uplinks per distribution (includes redundancy)
###### Patch Panels
- (x10) Eaton Tripp Lite Series 36-Port LC/LC Rackmount Fiber Enclosure Feed Through Patch Panel 1U - patch panel - 1U - 19"
	- [https://www.cdw.ca/product/tripp-lite-36-port-lc-lc-rackmount-fiber-enclosure-feed-thru-patch-panel-1u/3423705?pfm=srh](https://www.cdw.ca/product/tripp-lite-36-port-lc-lc-rackmount-fiber-enclosure-feed-thru-patch-panel-1u/3423705?pfm=srh "https://www.cdw.ca/product/tripp-lite-36-port-lc-lc-rackmount-fiber-enclosure-feed-thru-patch-panel-1u/3423705?pfm=srh")
	- 1 per TR, allows for redundant connections between distribution and TRs

###### Floor Breakdown
- 5th floor
	- Firewall:
		- (x1) Cisco FirePOWER 3140
	- Core: 
		- (x1) Cisco Catalyst 9300x
	- Distribution:
		- (x2) Cisco Catalyst 9300x
	- Access: 
		- (3x) 24 Port - Cisco CBS350-24P-4X
- 4th floor
	- Access:
		- (x1) 24 Port - Cisco CBS350-24P-4X
		- (x2) 48 Port - Cisco CBS350-48FP-4X
- 3rd floor
	- Access:
		- (x2) 24 Port - Cisco CBS350-24P-4X
		- (x2) 48 Port - Cisco CBS350-48FP-4X
- 2nd floor
	- Access:
		- (x1) 24 Port - Cisco CBS350-24P-4X
		- (x2) 48 Port - Cisco CBS350-48FP-4X
- 1st floor
	- Access:
		- (x1) 24 Port - Cisco CBS350-24P-4X
		- (x2) 48 Port - Cisco CBS350-48FP-4X

###### Other
- need to finalize details
	- WLC
	- APs
	- AP Switches (4 port poe+)
	- additional SFPs
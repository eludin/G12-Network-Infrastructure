## Network Infrastructure
### Group Meeting 3
#### November 14th, 2024
###### Github: [Repo](https://github.com/eludin/G12-Network-Infrastructure), [Org](https://github.com/G12-Network-Infrastructure-2024)

###### Objectives
- Go over intent letter response
- Build a discussion plan for video
	- Schedule video
- Discuss ER locations
- Discuss Managed Switches

###### Intent Letter Response
```
From: Simon Galton  
Subject: Thank you for your interest  
Date: November 11, 2024 11:34:56 AM EST  
To: SHANA Networks  
----------------------------------------------------------  
To the SHANA Networks team,

Thank you for your interest in our RFP. 

We can see that you have a complete team of five staff working on putting together a proposal.  You've noted our size, and the details of the building we are moving into.

We're looking forward to seeing what you come up with!  Please let us know if you have any questions, or if would like to meet regarding the project.

Simon Galton  
Purchasing Manager  
Apollo Business Consulting
```

###### Video Discussion Plan
- ~5 min video, simulate quick call with the client (looking for status update on proposal)
- don't need exhaustive detail just the highlights
- "It is 100% okay if this is not the final design"
	- allowed to change it before submitting final proposal and presentation
- don't need to cover EVERY aspect but DO need to cover the following:
	- **Proposed cabling plant choices**
		- we decided locations today: see visio
		- neil will look at cables
	- **Proposed hardware choices**
		- scott will look at hardware and build a basic list
	- **Total cost of these elements**
		- adam & henry have worked with the excel docs
		- final counts will come once hardware/cabling is decided
- we will receive full marks if submission is on time, company can understand our presentation and required elements are all included

###### ER/Datacenter locations
- ["i would accept a design that has a containerized data center..."](https://www.youtube.com/watch?v=UGqQDDNGC00)
- see Rittal IT containers
- ![[Pasted image 20241114143458.png]]
- edge computing enclosures
	- climate control, power, remote management
		- maybe necessary if we relocate data center to top floor

###### Managed/Unmanaged Switch Examples
- CBS110-24 (24 port unmanaged gigabit switch from Cisco)
	- ~$166
- WS-C2960L-24TS-LL (24 port managed gigabit switch from Cisco)
	- ~$1700
- ["Make sure you specify high quality managed switches for your proposal"](https://www.youtube.com/watch?v=xuluwkxY60Y)

###### Misc
- deciding router number and config
	- will depend on cost/hardware capabilities/expected traffic
		- 1 at core?
		- 2 at distribution level?
		- ~10 access level routers?
- choosing hardware
	- probably choosing cisco to familiarize ourselves with the ecosystem
	- definitely 1 core switch
	- definitely 2 distribution switch
	- definitely at least 2 access level per floor (see department breakdown)
		- 11 departments, each department should have at least 1 switch
		- business consultants is biggest department with 61 employees
- choosing closet locations
	- done, see visio

###### Department breakdown
- HR: all 25 on floor 1
- Finance: all 28 on floor 1
- Sales & Marketing: split 16 floor 1, 9 floor 2
- Legal: all 25 floor 2
- IT: split 36 floor 2, 10 floor 3
- Security: all 16 floor 3
- communications: all 22 floor 3
- Business Consultants: split 27 floor 3, 34 floor 4
- Client Management: all 31 floor 4
- Research and Analysis: split 4 floor 4, 12 floor 5
- Project Management: all 16 floor 5

- **Totals (17 access level):**
	- Floor 1: 3 switches
		- 25, 28, 16
	- Floor 2: 3 switches
		- 9, 25, 36
	- Floor 3: 4 switches
		- 10, 16, 22, 27
	- Floor 4: 3 switches
		- 34, 31, 4
	- Floor 5: 2 switches
		- 12, 16

###### Conclusions
- Planned date/time to record call: 
	- friday at ~3pm call
	- each person take a topic
		- Scott - hardware
		- Adam - plant specifics
		- Neil - cabling
		- Henry - cost?
		- Antonio - will build slides, guide conversation, do recording
- will make basic powerpoint to have structure for video presentation
- upload department breakdown specifics to canvas for reference]
- Scott will work on a basic list of hardware components
- Neil will build a basic list of cable requirements
	- they will both forward these to the group for cost analysis
	- submit that data back to Antonio to compile into presentation
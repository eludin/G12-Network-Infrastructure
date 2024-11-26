## Network Infrastructure
### Group Meeting 5
#### November 22nd, 2024
###### Github: [Repo](https://github.com/eludin/G12-Network-Infrastructure), [Org](https://github.com/G12-Network-Infrastructure-2024)

###### Video Call:
- https://www.youtube.com/watch?v=U-O2a2vRtGI

###### Objectives
- Go over Galton's response to our video
- Go over Adam's meeting with Galton
	- and any other subsequent conversations/feedback
- Plan final document / presentation?
	- go over requirements and delegate

###### Galton's Response:
- Presentation was very professional and easy to follow
- Liked that we got right into the details:
- **Distribution Switches**
	- " ... for the Distribution layer (we believe) was the business 350 series of switches ... "
		- " ... that's a series ... need to know more about the specific model ... "
		- " ... every model is a bit different: port count ... one thing that's consistent is they have a pretty limited uplink speed ... I think they're limited to 1gbit per second ..."
		- " ... if we're taking these from the distribution layer up to the core layer, are we not going to be bottlenecked by these switches on the way up?"
- **Core Switches**
	- " ... for the core you're proposing a Cisco Catalyst 9300 ... that's a series of switches not a specific model ... "
- **Access Switches**
	- " ... not sure if we had access switches in the specification or not ... its a bit confusing ... "
	- " ... is the business 350 series also going to be the access switches ... i think they might be ... again same set of concerns ... "
- **Fibre Cabling**
	- " ... for backbone cabling you were thinking of both single mode and multimode fibre. I'd like to know where that's going to go. So that will need to be articulated ... "
		- " ... and how much of each ... "
		- " ... is any of it going through riser or plenum space ... we have to make sure we understand what the cost implications of those parts of the runs would be"
- **Equipment Room and Top Floor Space**
	- " ... it looks like the equipment room will displace a bunch of IT staff on that second floor office ... "
		- " ... it's a big space you've carved out ... "
		- " ... we have a lot of IT staff that are supposed to be in there ... are they moving somewhere ... "
		- " ... I think there are some empty rooms on the upper floors, maybe that's a good spot for the ER... maybe locate a couple of IT desks out there for monitoring ... it might be interesting"
- **Horizontal Cabling**
	- "Do make sure that all the cabling you're talking about, not just the fibre cabling (but) whatever twisted pair cabling you're putting in, make sure you're looking at the rating of those ... "
		- " ... regular communications cable or plenum or ... riser ... whatever the case may be ..."
- **Cost Table**
	- "Was nice to see your cost table ... helped us understand what you were think about ..."
		- "... There was an item in there that was a bit confusing: Misc Hardware ... I think you spoke to it being racks and patch panels but it seemed like a bit number ... "
		- " ... we weren't quite sure if there was anything else in there ... "
		- " ... what we didn't see is specifically spoken to, which does need to be addressed for the final is other ancillary stuff: cable trays, conduit ... transceivers for your switches, telecommunications outlets ... "
			- "Please make sure that it's clear to us in that final report what it is you're proposing there ... It'll be super useful for us to understand that if it's articulated there."

###### Responding to Galton's Feedback
- **Clarifying our planned switches:**
	- access level switches are currently planned to be some 350 series switch
		- (ie. 350-24P-4G)
		- specific model/size depends on the department
	- distribution switches are currently planned to be the 9300 series
		- specific model/size will depend on final decision for access level
	- core switch is currently planned to be a 9300X
		- subject to change if it is determined we need more uplink
- **On cabling:**
	- very useful to know we need to specify cable rating as well (thanks for that feedback)
- **On ER location:**
	- In our meetings we decided on locating our data centre on the 5th floor
	- we may have had a miscommunication somewhere regarding second floor
		- either way, our infrastructure can't and wont displace several employees
- **Cost table:**
	- the costs we came up with were very "quick and dirty":
		- the $8100 "Misc Hardware" included:
			- 20 x 48 port patch panels (two per tr)
			- 10 x racks or cabinets (one per tr)
			- 24 x 25 pack of keystone jacks (600 total - covers all employees with lots of spares)
			- 1 x 42u rack cabinet for the core/distribution switches (more substantial/secure)
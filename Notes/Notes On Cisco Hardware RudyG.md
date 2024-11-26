### Meeting with Rudy
###### Notes on Cisco Hardware

###### About Rudy
- **Unified Communication Sales Engineer & Cisco Sales Specialist**
	- caveat:
		- hasn't worked with this hardware in 4+ years, specs/recommendations/standards change CONSTANTLY
		- take his recommendations with a grain of salt
- Take the provided company info, build a framework, make a recommendation for the long term

###### Consider:
- What the end user at the company needs/uses:
	- will workers need printers / print server
	- will workers need phones
		- many network phones have a switch on the back that computer connects to

###### Sizing Tools
- Cisco sizing tools are very useful:
	- https://www.cisco.com/c/en/us/products/switches/switch-selector.html
	- https://www.cisco.com/c/en_ca/solutions/small-business/selector-tool.html
- Meraki sizing tool: https://merakisizing.com/#/ms
	- note: MS = switches
	- includes Cisco products

###### Meraki
- Meraki itself is a cisco product
	- more user friendly (simpler, easier to understand & configure)
	- Merakis tend to be layer 2 (ie. no routing on the 100 series)

###### POE ?
- 100% of customers need POE switches
	- phones, cameras, aps
- POE / POE+ (~30W)
	- gives higher wattage than normal POE for cameras aps phones etc.
- UPOE / UPOE+ (~90W)
	- cisco product
	- never used it personally
	- more power
![[Pasted image 20241120225638.png]]

###### Business 350 Series
- On "Business 350 series":
	- "that's the small series"
	- small business line of switches
	- worth considering depending on pricing

###### Catalyst 9300
- Catalyst 9300 not considered "core" necessarily
	- we could use a 9300x as a core switch
		- implement 2 of them for redundancy
	- he would use one or more 9300s on each floor for access
		- maybe 9200s for access level
		- he thought 9300 was only 40gbit

###### Bandwidth
- Bandwidth rough ballparks
	- 40gig uplink minimum
	- 10gbit from core to access
	- 1g from access to node

###### Access Level Switches
- On number and type of access level switches:
	- "companies move people around all the time"
	- positioning, configuring switches on a per-department basis can be done but doesn't happen very often in practice (from his experience)
		- more often than not companies want to pay for 1 big access switch and would separate departments with a vlan
		- 1 switch per department seems unnecessary complicated and if an employee has to move to another location in the building for some reason this would cause problems
		- if company wants room for growth this design is likely too rigid
	- Anecdote:
		- no customer has ever said "we want 3 switches to serve 3 departments"
			- the customer never wants to buy 3 switches
			- its totally normal to put everyone on the same switch

###### Switch Stacking
- redundancy, switches in switches, if one fails traffic still works
- 3x 24port switches to stack at access level?
- need to buy separate "stacking" cables

###### Multigig
- worth considering but likely not for our project

###### Routing
- probably routing at the core
	- many customers prefer to save money by only routing at core, making access layer switches only layer 2 rather than layer 2 and 3
- Anecdote: he has had customers who took older lower end cisco switches to core, and used smaller/weaker switches at access layer

###### StackPower
- no customer buys this on access level
- they DO buy it on core
- redundant power supplies are very important at core
- RPS (redundant power supply)

###### Converged Layer Switches
- IMPORTANT:
	- 2 core switches ALWAYS
		- for redundancy
		- industry standard

###### Recommendations
- CORE:
	- 2 switch stack
	- uplink: 40gbit
	- 2.5gbit to access level
- licensing model is common now
	- license cost covers maintenance, upgrade, cabling for redundant power
- Re-iterates: 
	- Meraki is very simple and easy to configure
	- "as simple as using the Meraki tool"
	- anyone can put together a network with Meraki
- **Core solution: 2x Catalyst 9300x**

- ACCESS:
	- another 9300 or equivalent
		- isolate departments with vlan
	- some logic/reasoning to splitting departments physically at a switch level but that wasn't his experience in the workforce
		- reiterates: most companies who wanted department isolation would do so with a vlan

---
###### Post-Meeting Followup
- Summary from email:

> Cisco Business 350 Series switch is suitable for use as access layer switches in a network that needs core switches; for core switches, depending on your network size and traffic demands, consider options like the Cisco Catalyst 9000 Series, Cisco Nexus 5000 Series, or Cisco Catalyst 9300 Series, which are designed for high performance and scalability at the core level. 
> 
> **Explanation:**
> ==**Cisco Business 350 Series as Access Layer:**==
> This series is designed as a managed switch with features like VLANs, QoS, and security capabilities, which are ideal for connecting end-user devices like desktops and laptops at the access layer of a network. 
> 
> The Cisco Business 350 Series switch is suitable for use as an access layer switch in a network that also requires core switches; its features and capabilities make it a good choice for connecting end-user devices to the network while allowing you to use a separate, more powerful switch for core routing functions. 
> 
> **Key points about the Cisco Business 350 Series for access layer usage:**
> **Designed for small businesses:**
> Primarily marketed as a solution for smaller businesses, it provides essential features for managing network access at the edge. 
> 
> **Layer 2 and 3 functionality:**
> Supports basic Layer 2 switching and some Layer 3 routing capabilities, making it capable of managing network traffic at the access layer. 
> 
> **Security features:**
> Includes features like VLANs, port security, and access control to segment network traffic and enhance security at the access layer. 
> 
> **Easy management:**
> Simple configuration interface suitable for smaller network administrators. 
> 
> **Why you might need a separate core switch:**
> When a network grows beyond a small scale, a dedicated core switch is needed to handle high volumes of traffic between different access layer switches, requiring more robust features and higher bandwidth capacity. 
> 
> **High bandwidth needs:**
> If your network requires high-speed data transfer between different network segments, a dedicated core switch with greater processing power and uplink capacity is necessary. 
> 
> **Advanced routing features:**
> For complex routing policies and traffic management, a core switch with more advanced Layer 3 features might be needed. 
> 
> ==**Recommended Core Switches:**==
> **Cisco Catalyst 9000 Series:**
> A high-performance, modular series suitable for large enterprise networks with advanced features like automation and security.
> 
> **Cisco Nexus 5000 Series:**
> Designed for data center environments with high scalability and advanced routing capabilities.
> 
> **Cisco Catalyst 9300 Series:**
> A good option for smaller to mid-sized enterprise networks, offering a balance between performance and cost. 
> The Cisco 9300 switch is beneficial as a core switch due to its high-performance capabilities, scalability, advanced security features, flexible management options, and robust stacking capabilities, allowing it to handle large volumes of data traffic efficiently while providing robust network security and seamless management in a large network environment.
> 
> **Key points to consider when choosing core switches:**
> **Network size and traffic volume:**
> Select a switch with sufficient port density and bandwidth to handle your expected network traffic. 
> 
> **Scalability:**
> Consider future network growth and choose a switch that can be easily expanded. 
> 
> **Advanced features:**
> Depending on your needs, you might require features like load balancing, security policies, and quality of service (QoS).



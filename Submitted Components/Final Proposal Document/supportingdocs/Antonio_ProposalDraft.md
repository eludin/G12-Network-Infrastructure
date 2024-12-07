## Network Infrastructure
### Network Design Proposal Draft
#### November 22nd, 2024
###### Github: [Repo](https://github.com/eludin/G12-Network-Infrastructure), [Org](https://github.com/G12-Network-Infrastructure-2024)

###### Title Page
- Company Logo
- Network Design Proposal for Apollo Business Consulting
- Prepared Fall 2024

###### Table of Contents
- Section ....... Page Num
	- Introduction ..... 1
	- Executive Summary ..... 2
	- Business Profile ..... 3
	- Logical Network ..... 4
	- Physical Network ..... 5
	- Cabling ..... 6
	- Wireless Option ..... 7
	- Cost Estimates ..... 8
	- Conclusions ..... 9
	- Appendices ..... 10

###### Introduction
- Intro will thank the business for the opportunity and acknowledge several key points that influenced design decisions.
- Brief summary of topology, keywords, wide overview

The purpose of this document is to provide a thorough overview of SHANA Networks' proposed 3-tier network design for Apollo Business Consulting's new 5 floor campus. At every stage of our  process, we have made design decisions with your future in mind. In the dialogue we've had with your representatives, and the supplementary research we've done into your enterprise, it has been made abundantly clear that our design needs to support the growth your company expects to see over the coming years. We at SHANA believe our design will provide you with a fast, robust, and scalable network that can act as a sturdy foundation the folks at Apollo Business Consulting can rely on for years to come.

This report will clarify the specifics of our design, rationalize those decisions in the context of your organization, and provide insight and analysis where appropriate. At a glance, this design will provide your campus with a suite of high-end Cisco switches including: 3x Catalyst 9300X, 8x CBS350-24FP-4X, 8x CBS350-48FP-4X, and 5x CBS350-8FP-E-2G. These switches will be interconnected by 345 meters of multi-mode fibre, and 13388 meters of Category 6 cabling all of which comply with TIA/EIA 568 standards. 

We look forward to bringing this project to life and on behalf of the SHANA team: 
Thank you for the opportunity to provide this proposal.

###### Executive Summary
- Breakdown what is being offered and for how much
- example:
> 	Client Company Name has asked Your Company Name to bid on an upcoming network buildout at their new head office. Our proposal includes 228 pairs of tin cans and 6000 feet of category 17 twisted twine to interconnect them, as well as a few pigeons for stringless communications. Total hardware costs are estimated to be $250, with a buffer of $300 in case the lower-cost cat 17 string is not available. Annual upkeep of the pigeons will be $200, plus the time of a co-op student. Installation labour costs for this job are not a factor as Your Company Name will use a government program to employ co-op and newly graduated students, therefore labour costs will be covered. Internet access will cost a total of $7500 in year one, and $4800 on an annual basis. 
> 	
> 	In summary, first-year costs will be $8050. Total annual upkeep should be budgeted at $5000 to include low-cost co-op students for maintenance activities, the pigeons, monthly costs for Internet access, the replacement of rusting tin cans and to accommodate changing office layouts and, of course, new runs of string.

This report provides a thorough overview of the 3-tiered network SHANA networks is proposing for Apollo Business Consulting's new 5 floor campus. 

This design makes use of top of the line Cisco switches including the Cisco Catalyst 9300X for both the core and distribution layers as well as a suite of Cisco Business 350 series switches such as the CBS350-24FP-4X, and CBS350-48FP-4X which will provide access level connectivity. Additionally, our design will provide a set of Cisco CBS350-8FP-E-2G switches which will allow for the implementation of an AP array after a thorough site survey is conducted. This hardware will be connected vertically by a 345 meter multi-mode fibre backbone and distributed to your employee workstations via 13,388 meters of Category 6 cabling all of which comply with TIA/EIA 568 standards. 

This design will provide all 311 employees of Apollo Business Consulting and its president each with a 1 Gigabit connection to this network with significant room for growth.

Our installation estimate will amount to a total of $XXX and our team has calculated a yearly upkeep of $XXX which includes any necessary service, maintenance, and upkeep.

###### Business Profile
- acknowledge the business, it's growth etc
- share department breakdown and the services they use
- example:
> 	 The business has identified the following major servers/services:
> 	 E-mail
> 	 Internet use
> 	 **S**hoelace **A**cquisition and **S**ales **Sy**stem  (SASSy) – this is a large, non-virtualized database application system
> 	 **A**utomatic **W**izard for **E**nterprise **S**hoelace **O**rdering and **M**anufacture **E**nablement (AWESOME) – this is a second, non-virtualized database application server
> 	 Approximately 20 virtualized application servers, such as **E**mployee **S**elf-**S**ervice (ESS), **C**ustomer **R**elationship **M**anagement (CRM), **E**nterprise **R**esource **P**lanning (ERP), etc.
> 	 A collection of file servers, each hosting about 150 employees
> 	 A physical server hosting corporate VOIP and IM services
> 	 A physical server hosting Videoconferencing services

Over it's 15 year history, Apollo Business Consulting's commitment to corporate excellence has fuelled it's growth to an impressive 311 employees which span 11 distinct departments.
This year marks a bold milestone for Apollo, as the company has opted to relocate their operations to a brand-new, cutting-edge 5 floor campus; citing a dedication to provide their staff with an environment that fosters collaboration and innovation. This move will provide Apollo with the opportunity to develop and deliver meaningful initiatives to the clients and communities that have come to rely on their services and will undoubtedly stoke the next 15 years of their growth.

At the heart of this operation is an impressive 311 employee workforce which is broken down into 11 major departments: HR, Finance, Sales and Marketing, Legal, IT, Security, Communications, Business Consultants, Client Management, Research and Analysis, and Project Management. The cornerstone of their success can be found in the hierarchical structuring of these departments and the integration of its executive individuals into each of their respective departments where they work alongside their staff as a unified team.

To support this workforce and their clients, Apollo Business Consulting maintains a series of networked printers and VOIP phones as well as several on-site physical and virtual servers. These servers provide internal staff with e-mail and other office productivity services like file sharing, and collaborative task management. Additionally, these servers host numerous web-services which provide clients with access to real-time analytics, collaboration tools, and database services all through a convenient and modern dashboard interface. This modular implementation of a virtualized servers provides Apollo with the flexibility to grow seamlessly with the demands of their clientele, and demonstrate the company's dedication to innovation and productivity.

###### Proposed Logical Network Layout
- The following diagrams outline the proposed logical network for Apollo Business Consulting's 5 story campus.
- Provide a high-level summary of the connections, some rationale, any caveats and notes

###### Proposed Physical Network Layout
- The following diagrams outline the proposed physical network for Apollo Business Consulting's 5 story campus.
- Provide a high-level summary of the connections, some rationale, any caveats and notes
- major cable runs
- locations of key IT infrastructure

###### Optional: Wireless Configuration
- Would need to perform a Wireless Site Survey to determine the most efficient location for our APs.
- This section provides a general overview of how we would implement an array of APs to provide an ESS to the building.
- Reference Wireless Site Survey lecture (wireless class) heavily

###### Cost Estimates
- provide thorough cost analysis
- include table 

###### Additional Comments
- Any additional remarks, contexts, rationale can go here
- Conclusions, thanks etc.

###### Appendix A - Current Office Layout
- "The unoccupied offices are currently configured as follows:"
	- any other documentation, imagery, diagrams or supporting material can go here.

---
###### Report Rubric
- All required elements present and in a logical sequence; spelling, grammar, and professionalism
	- 5 to >3.75 pts: Excellent
	- Proposal contains all the elements from the template in a sensible order; document looks professional (consistent layout, fonts, etc.) No more than two spelling/grammar errors noted
- Network design meets the needs of the case study company and is reasonable, thoughtful, and logical
	- 10 to >7.5 pts: Excellent
	- The network design submitted will address the needs of the company. All of the structured cabling rules are consistently followed. Good hardware and cabling decisions are made.
- Drawings clear, informative, and accurate.
	- 10 to >7.5 pts: Excellent
	- All drawings are easily readable. All drawings reflect the final proposed design. All drawings follow the rules outlined in the assignment.
- Costing accurate, reflects design.
	- 10 to >7.5 pts: Excellent
	- Equipment and cabling costs reflect all of the hardware and cabling choices in the proposal. All costs are sensible. All the costs are cited. No extraneous cost items.

###### Presentation Rubric
- All required elements present and in a logical sequence; presented with professionalism
	- 6 to >4.5 pts: Excellent
	- All the elements specified in the assignment are presented The presentation flow is logical. The format is appropriate to the topic and the audience. Presentation length requirements are met.
- Proposal is clearly explained
	- 6 to >4.5 pts: Excellent
	- The details of the proposal are presented well, Information presented in a clear and unambiguous way by all of the participants.
- Shows creativity
	- 3 to >1.5 pts: Excellent
	- Presentation shows enthusiasm of team. A consistent effort is made to make the presentation interesting to watch.
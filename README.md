DataTrain
=========
A social dictionary for our nation's wealth of data.

DataTrain is a data service that makes it easier and faster to understand and communicate the meaning, value and implications of open, public data. 

* URL (reserved) http://data-train.org
* Twitter (reserved) @TheDataTrain

### Features
* Add: Import dataset sample, get permalink to metadata about the dataset fields (elements and properties.)
* Collaboratively edit information about for fields and values in data sets based on user-tested questions
* Search for field abbreviations
* Share your learning and expertise and help raise the bar of what we can do as a nation.
* Export or make API requests for plain-language labels, descriptions, glossaries and metadata files for apps, APIs and data platforms.

### The Problem
In government, words matter. Specific words carry deep meaning about how and why we do things the way we do. For better or worse.

A growing open data movement is making more of the complicated government data available to encourage innovation, efficiency and better collaborations among agencies, the private sector, organizations and civilians.

A common problem for anyone using a government dataset is to develop a functional understanding of the fields and values of a given dataset, be it data that is publicly downloaded through a web-based service or open data portal, or some FOIA's information that was extracted from PDFs. This is similar to any training a government worker would do in the course of their work, as they become oriented to the various processes that are part of the every day functioning of government.

To understand the data, researchers, journalists, industry professionals and others conduct deep research and technical phone calls with government agencies to make sense of the specific meanings and implications of certain values. Sometimes this is simple, somethings this takes many meetings and nuanced interviews.

A big problem is that this work must be repeated by anyone working with a similar dataset, and they may be likely to have similar questions, or make similar mistakes. In some cases, it can take months to understand the real government processes taking place behind the data. This could be permit data, information about businesses, regulated data and other forms of data that were put in place to help improve our quality of life and help us function as a civilization.

The questions we ask are not only useful to us. The questions we ask of government, the small requests we make to reformat the data to be more useful to our needs. Usually the data a government holds is housed in a service provided by a government contractor, and most government contractors would *like* to make their product more valuable to governments. The explanations we help create can help train new government staff, or help with inter-agency communication.

### Previous solutions
In ideal circumstances, a data provider shares a 'metadata dictionary' with a dataset. This can sometimes be found in GIS shapefiles, and sometimes there is a website for an agency that links to a document that explains the process. Sometimes you can find the original form where the data was collected, and figure out the meaning in that way. The more documented datasets tend to be the more highly used datasets, such as weather or the simpler tables like zipcodes.

There is a lot of information that is the product of various administrations and subject matter experts. Data that is newly released after an encouragment to open up data is less likely to have a metadata dictionary accompanying it, and this dictionary is most certainly not an intelligent product of the answers given by agencies to people working with the datasets. 

For whever reasons, it's very rare to find descriptions of open data. This is probably because data was converted from a less machine-readable format, just to make it open and available at all, and the process of documenting and "being right" would form a cultural and process bottleneck that would mean the data would never be publishing at all! Which wouldn't be helpful. Raw data is better than no data. 

Somewhere in that process, however, it seems that the important part of making the dataset very clear and understandable was perhaps not prioritized. It's also very likely that the dialogue between citizens and goverment have traditionally been carried out over email, phone and at conferences, by industry workers, and so it's not a budgetary priority to make the data comprehensible to the general public, who typically have little power or influence over the day-to-day operations within government. However, as we see new applications that leverage open data to provide services and useful information for citizens and the public good, the capacity of the public to use datasets to make smarter decisions and investments in the future is shifting. Civic hackers and civic service companies are using this data and developing the capacity to work with more complex data. In order to innovate and continue to progress, we will need to lower the bar for understanding our valuable and complicated bureaucratic datasets.

Fortunately, we have many many open datasets and data platforms to work with and support. We can easily create a service & community of translators that focus on making data much more comprehensible, and this can plug in easily to existing data platforms.


### Examples & Stories
While some data is pretty self-explanatory (such as latitude, longituge, name, email, url), there are many others that *almost* make sense, and yet if you ask any government worker, you can usually get a very long explanation of the historical and precise meanings of a datasets. For example, we can look at the Nominations & Appointments dataset on <a href="https://opendata.socrata.com/dataset/The-White-House-Nominations-Appointments/n5m4-mism">Socrata</a> that has over 500K views, and appears on <a href="http://www.whitehouse.gov/briefing-room/nominations-and-appointments">White House.gov.</a>

#### On "Confirmations"
In this dataset, there is a field called "Confirmed." I clicked the little (i) information button, which doesn't tell me anything. (However, the "Re-nomination" field does say "Indicates that the Nomination Date listed is for a re-nomination (after a previous nomination of the same individual to the same post was returned by the Senate at a recess or adjournment).")

The value of Confirmation is a checkbox, and there is an accompanying date. 

*But what is a Confirmation?* Yes, anyone in government will cringe that most people don't know. In my case, I'm fine admitting my ignorance because I know I speak for most people. I lost any feeling of shame and instead adopted this as a personal mission when I was able to ask some city employees of Seattle what percentage of their population had any idea what they were doing, and they said that 10% of people had a clue at all. And then, later on, I realized that *most* government bureaucratic process *are* processes made by people, from our brains, and so somewhat arbitrary. Most complicated government data requires training and education to understand it. This encourages a culture of specialists.

My guess about a "confirmation" is that maybe it is a swearing in session, and the day on which an appointee becomes "official." But, after watching every episode of West Wing and The Good Wife, it could *also* be that the confirmation is the day that one of the government bodies agreed to an appointee, and the appointee would start working an some sort of transition day. I really don't know. I am going to have to ask some people who studied government in college. Fortunately for me, I know people like that, but most of my life, it wasn't something I thought about. Remember, we stopped civics education in America. I've gone through my whole life hearing these words and knowing that they mean something 'governmenty' and also that it has no relevance to me. But in actuality, this is my country, and a government I would like to improve and I would like to help improve how we live, so actually I would really like to know what a confirmation is.

So I looked at Wikipedia, and got very confused. I also looked up "Confirmation" in the dictionary, and this was also not helpful. Surely there is a dictionary of government terminology, perhaps in a textbook? We should link these textbook definitions to these public datasets if we can.


#### On terminology

There are some things you can say and some kinds of information that are sensitive. For example, some government language uses complex wording because any other word could be inaccurate and imply that something has happened that actually hasn't. This can really stress out or freak out someone who fears certain consequences. It may be that these consequences are fictitious, or they are very real. In any case, datasets with obscure and technical elements should be explained in a plain-language way that helps all tax payers understand the spirit and value of the point of data collection.

When I was working with California Water Rights data, there were two statuses for a water right (a type of permit) that were "Adjudicated" and "Claimed." It took me a lot of conferences, conversations with lawyers and with the State Water Resource Control board to understand that "Adjudicated" often meant that a many year long court process had happened, potentially involving hundreds of water basin residents. "Claimed" meant that someone had simply claimed that they had a water right, and it might not be official. Even today I am only 90% certain that I fully understand. There was no way for me to share this valuable information, aside from trying to make notes in a github repository. This information could help Californians prepare better for droughts.

Similarly, in building permits, there is a staged called "Issuance" -- which means that a permit is in a stage in which it is in the process of being issued. No regular person uses this word, and so that presents one more barrier to new business owners, in making a process of getting permission just a little more complicated.


#### On technical data
In scientific data, sometimes there are very specific API's that reflect the measurement of sensors. My favorite example is that of RFID tags on whales, sea turtles and sharks in the ocean. There is a whole public API of this information, which means you can make animated maps of where whales are swimming. But the problem is, the API is entirely based on acronyms and the only reason I learned about it was because an NOAA scientist took a day to do a public workshop. Imagine how many other sensor readings have a similar fate... and this data is already public and already in API-format. (I would get you a URL for this project, but it had such a complicated and technical name that I have been unable to locate it again, despite looking for it on 4 separate occasions!)

There are many other words that are 'red flags', because of history and legality. Similarly, with a dataset such as a gun registry database, there are implications about the personally identifiable information and the address of the permit applicant. There is no way to communicate about the political sensitivity of that dataset, or to build on what others have learned. If we want to keep innovating in how we present all of this new data that is becoming public, then we need to build on what we learn. Governments shut down sensitive data as soon as it seems like it might become problematic. If we don't create a way to discuss the ethical use and implications of datasets, then we will continue to have struggles. The same goes for crime data, which at first glance seems like a useful thing to publish, but there are many discussions about how presenting crime data without other contextual information can have unintended societal implications.


#### On plain-language communication.
<a href="http://gov.uk">Gov.UK</a>  has a great <a href="https://gds.blog.gov.uk/2012/02/07/writing-simply/">document</a> and effort to encourage government workers to use plain-language wherever possible, and this also means choosing the "slightly less accurate" in favor of helping more people understand. Service providers often must translate "gov-speak" into plain-language to make it possible to provide better services. We have a new movment of civic designers who care about the quality and comprehensibility of content. We need a way to share our best "labels" for certain types of information.

We have a lot of potential to understand better what we are actually *doing* to make our cities and lives better.


# The Solution
DataTrain is a social data service that encourages us to share our notes and research regarding the meanings of various fields and values in datasets. We are modernizing an older technology, "metadata registries", and making them more social and more attuned to the kinds of questions that non-subject matter experts might have with regard to the meaning of various datasets. We ask sets of questions appropriate to each field, and capture information such as legal or political implications, information about sensors and measurements, and allow for notes about the data collection process.

In addition to a collaborative workspace in the form of a data service & an open source application, a metadata schema will be researched, and we will publish our best practices that we learn as a result of doing this project. 


### Get On Board! Ways to help

#### Have a dataset you have worked closely with and would like to share what you learned?

We are prototyping this application, and have a simple manual checklist of questions you can do with your dataset. We will format your answers according to a JSON schema, and make those available to a demonstration interface prototype, and then uploaded more formally one our research period is concluded.


#### App development hack days

In January and February 2015 we will have some hack days to build out the prototype. Let us know if you are interested in volunteering. There is a schema. We will probably build this with nodejs (maybe sails) (or rails or drupal.) We might use PostGRES 9.4 sort of as a document object store, or we might use MongoDB. We will try out some fun CSS/bootstrappy frameworks and use markdown whereever possible. We will probably host the app on Digital Ocean. Early datasets will be stored in GitHub, since we may refactor the data as we learn more.

Hack days and nights will happen at some Brigade nights, at Code for America, and on google hangouts.

#### Librarians and Content-writers
Do you love plain-language writing? Do you get excited about the difference between 4th grade reading level and 10th grade? Bring your public understanding of everything skills to look at some tricky NSF project data and help translate it for the public.


#### Design & User Research
We are prototyping the questions we can ask of the elements of a dataset, based on various types of information. If you are interested in doing some phone calls and taking notes, let us know.


#### Subject matter experts
Do you know a lot about a certain area of government and would be willing to be interviewed. You probably already have a good idea of the ways that people using data get confused. We want to help you get word out so that citizens understand and represent your data accurately. 

#### Team, Partners & Advisors
If you are interested and want to get this off the ground in 2015, get in touch! Otherwise, I will be reaching out and then updating this list. Will be reaching out to agencies, data platform providers. city governments & departments, information scientists, Code for America brigades and civic hackers & companies. This should be a pretty simple service to get going and be able to add value to existing data sets.


## ROADMAP
Timeline & Next Steps
12/04/2014 - project conception (after several years of observation)
12/24/2014 - publish project description

* Publish technical road map
* Publish schema
* Publish draft of question sets
* MVP & Research: Jan - March: reach out to possible projects and document datasets according to working draft of metadata schema. Use question sets & publish results as JSON in github.
* Build design mockup of app interface
* Mock up app
* Document spec of app (currently is in scribble notes on a pieces of paper)
* Raise some cash to support active development and outreach efforts in 2015 and get this going as a public data utility.
* Prototype ajax widget for integration with data platforms


### Train Conductor
Chach Sikes @chachasikes, chachasikes@gmail.com, http://chachaville.com

Chach is an open data advocate and web engineer/designer/facilitator who is interested in increasing comprehension around technical and specialized information, especially after working in science museums for a long time, where writers and researchers figured out how to democratize understanding of science.

She currently works at CivicInsight publishing building development and code enforcement data, & was a Code for America Alum, '11 where she co-founded the Iconathon, a design event that encourages citizens and designers to work with subject matter experts to create visual symbols for civic concepts.


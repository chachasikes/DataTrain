http://pds.nasa.gov/tools/ddlookup/data_dictionary_lookup.cfm

http://pds.nasa.gov/tools/ddlookup/data_dictionary_detail.cfm?ResultsSelBox=a_axis_radius

  Column Name = a_axis_radius

  BL Name = aaxisradius
  Terse Name = aaxisradius
  Gen Data Type = REAL
  Unit Id = km
  Std Value Type = RANGE
  Minimum Column Value = N/A 
  Maximum Column Value = UNK 
  Minimum Length = N/A 
  Maximum Length = N/A 
  Default =  
  

  Change Date = 1989-01-01
  Status Type = APPROVED
  Source Name = 
  SQL Format =  FLOAT 
  BL SQL Format = bcdflt(31)
  Display Format = SCI(1,2)
  Std Val Output Flag = N
  Text Flag = N
  Available Value Type =  
  
Description
  
                                                                             
The a_axis_radius element provides the value of the semimajor axis of        
the ellipsoid that defines the approximate shape of a target body.  'A'      
is usually in the equitorial plane.                                          

No Standard Values exist for this Element.

 General Classification  
GEOMETRY                   

 System Classification  
COMMON                     

Object Name Required
image_map_projection  Y
No Aliases exist for this Element.

No Formation Rule exists for this Element.

No Standard Value Description exists for this Element.

Label Revision Note


#### average_orbit_peri_tdb_time
* http://pds.nasa.gov/tools/ddlookup/data_dictionary_detail.cfm?ResultsSelBox=average_orbit_peri_tdb_time
 Column Name = average_orbit_peri_tdb_time

  BL Name = mgn18
  Terse Name = 
  Gen Data Type = REAL
  Unit Id = none
  Std Value Type = RANGE
  Minimum Column Value = N/A 
  Maximum Column Value = UNK 
  Minimum Length = N/A 
  Maximum Length = N/A 
  Default =  
  

  Change Date = 1991-05-30
  Status Type = APPROVED
  Source Name = 
  SQL Format =  
  BL SQL Format = 
  Display Format = JUSTLEFT
  Std Val Output Flag = N
  Text Flag = N
  Available Value Type =  
  
Description
  
 The average_orbit_peri_tdb_time element provides the value                  
of the periapsis time of the predicted orbit. This orbit is                  
based on the elements used to generate the uplink commands                   
for the current mapping pass. It represents an average over                  
the entire orbit, and is not the result of post-orbit                        
navigation solutions. The elements should be used for                        
comparison purposes only, since they may involve large                       
errors.  The predicted orbit elements are copied from the                    
orbit header file of the ALT-EDR tape, or, if unavailable,                   
from the orbit header file of the C-BIDR.                                    

No Standard Values exist for this Element.

 General Classification  
SYSTEM                     

 System Classification  
PDS_GEO_MGN                

No Objects are listed for this Element.

No Aliases exist for this Element.

No Formation Rule exists for this Element.

No Standard Value Description exists for this Element.

Label Revision Note
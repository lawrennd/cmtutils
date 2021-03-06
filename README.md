# CMTUTILS

### 28th October 2014 Neil D. Lawrence

As well as pandas and the standard numpy/scipy stack, the library has the following dependencies: `lxml`, `openpyxl`, `gdata`, `pods`

```
pip install lxml
pip install openpyxl
pip install gdata
pip install pods
```


In 2014 [Corinna Cortes](http://research.google.com/pubs/author121.html) and I
were NIPS program Co-Chairs. Alan Saul was our Program Manager. As part of the
process we wrote a lot of scripts for processing the data. The scripts I wrote
used the `IPython notebook` (now [Project Jupyter](http://jupyter.org/)) and
`pandas`. It was always my intention to summarise this work in case others find
it useful. It is also quite a good document for summarising what is involved in
program chairing a major conference like NIPS.

In May 2021, I separated out the utility files used for the notebooks into a separate python module. The library, `cmtutils`, which manages the submissions.  For
reviewer management (which was the first thing written) the scripts are based
around a local mirror of the CMT user data base in SQLite. For review management
we moved things much more towards `pandas` and used CMT as the central
repository of reviews, exporting them on a daily basis.

A lot of communication was required between CMT through imports and exports. Some
of the links used for CMT exports are available [here](http://nbviewer.ipython.org/github/sods/conference/blob/master/Useful%20Links.ipynb).
The various tasks are structured in IPython notebooks in the conference repo. The code used was
first written for the NIPS 2014 conference, but ideas were based on experience
from using CMT for AISTATS 2012 and some preliminary code written then (for
example for importing the XML formatted version of Excel that CMT uses).

Right from the start it was felt that being able to import and export
information to Google spreadsheets would be very useful. With this in mind an
interface between `pandas` and Google sheets was created (initially just for
reading, then later for updating). This made it much easier to import reviewer
suggestions and export information about paper statuses to reviewers. That
software has been spun out as part of a suite of tools for [Open Data
Science](http://inverseprobability.com/2014/07/01/open-data-science/) that is
[available on github here](https://github.com/sods/ods). These notebooks are
also available in their own [github repository for conference
software](https://github.com/lawrennd/neurips2014).

A note on the code. A lot of this code was written 'live' as reviews were coming
in or as a crisis required averting. The original code for sharing information
via Google spreadsheets was written across two or three days whilst on a family
holiday in the Catskills. Much of the code could do with rewriting, and this is
an ongoing process that I hope other conference chairs or program managers will
contribute to. It is shared here as a record of the work required for a
conference like NIPS as well as in the hope that it will be useful for others.
It is not shared as an example of 'best practice' in python coding. There are
some parts I'm proud of and others I'm not. However, I think it *is* a very good
example of how the notebook can be used with python and `pandas`to do 'live'
data processing of some importance whilst under a great deal of pressure. I
can't imagine having done it quite like this with a different suite of tools.

As well as the installed files, you need to create a file called `.cmt_user.cfg` in your home directory and give it the following fields:

```
# This is a user's personal configuration file for CMT
[conference]
short_name = NIPS
year = 2014
chair_email = program-chairs@nips.cc

[cmt]
export_directory = 

[gmail]
account = 
name = 
password = 

[google docs]
# Here include the spreadsheet keys of program committee and reviewer candiates
program_committee_key = 
reviewer_candidate_key =  
buddy_pair_key = 
global_results_key = 

[review data]
directory = 
file = all_reviews.pickle
```

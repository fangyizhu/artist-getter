# Artist Getter

Building on top of [sfmoma/getty-getter](https://github.com/sfmoma/getty-getter) to retrieve artist information from
both Getty ULAN and WikiData.

## Installation

`pip install artist-getter`

Getty Getter was built on Django 1.8 and Python 3.12.

## Artist Getter

[Getty Getter](https://github.com/sfmoma/getty-getter) was a script developed by SFMOMA for associating artists with the
Getty ULAN vocabulary and gathering additional metadata
based on an artist's ULAN.

The ULAN vocabulary is a wealth of information regarding people and organizations involved in art and culture. More
about ULAN can be found [here](http://www.getty.edu/research/tools/vocabularies/ulan/about.html).

Wikidata is later added as a supplement on top of ULAN, in case there are entries missing from one of the two artist
databases. Together they constitute Artist Getter.

This script is a work in progress.

### ULAN Functions

Right now there are four basic functions.

#### 1. get_getty_ulan

`get_getty_ulan` consumes and artist's name (formatted    `u'Last, First'`) and does a best guess match against
similar names in the Getty ULAN vocabulary. The returned data will include the name of the artist or organization, the
ULAN, the "type" og thing returned (e.g. person, organization etc) and a scope note, which is a brief summary of the
artist's career.

`get_getty_ulan(u"Stieglitz, Alfred")`

```
{'scopenote': u'Renowned photographer Stieglitz first studied photochemistry with Hermann Wilhelm Vogel at the Technische Hochschule in Berlin, from 1882-1886, and took his first photographs in 1883. He continued to travel and photograph in Germany, Austria, and Switzerland until 1890, when he returned to New York City. From 1890 to 1895 he was a partner in a photogravure firm. During this time he concentrated on photographing the streets of New York City. In 1894, Stieglitz travelled to Europe and was elected a member of the Linked Ring, a pictorialist society in London. In 1902, Stieglitz founded the Photo-Secession Movement which attempted to prove that pictorialist photography was a fine art form. From 1903 to 1917, Stieglitz was publisher and director of Camera Work magazine. The graphic section was run by Edward Steichen (1879-1973). In 1905, Stieglitz opened the Little Galleries of the Photo-Secession "291" on Fifth Avenue in New York City with Steichen. The galleries operated until 1917. In 1907, Stieglitz exhibited his autochrome photographs. Stieglitz stopped photographing in 1937. During his lifetime, Stieglitz was also a close friend and collaborator of Joseph T. Keiley. Together they invented the glycerine process which permitted partial development of platinum papers. Also, they produced joint research on the history of photography. Keiley also acted as the associate editor of Stieglitz\'\'s publications "Camera Notes" and "Camera Works". American photographer.', 'ulan': u'500024301', 'type': u'Persons, Artists', 'term': u'Stieglitz, Alfred'}
```

#### 2. get_getty_relationship

`get_getty_relationship` consumes an artist's ULAN and returns a list of the relationships that artist had with
other artists in the ULAN vocabulary. The `object_ulan` being the ULAN of the related person or organization.
`get_getty_relationship("500024301")`

```
{'relationship_type': u'student of', 'object_ulan': u'500063166'}{'relationship_type': u'influenced', 'object_ulan': u'500007426'}{'relationship_type': u'colleague of', 'object_ulan': u'500004441'}{'relationship_type': u'collaborated with', 'object_ulan': u'500001336'}{'relationship_type': u'collaborated with', 'object_ulan': u'500000431'}{'relationship_type': u'spouse of', 'object_ulan': u'500018666'}{'relationship_type': u'friend of', 'object_ulan': u'500070483'}
```

#### 3. get_getty_artist_name

`get_getty_artist_name` consumes an ULAN and returns just the artist's name formatted `Last, First`.
`get_getty_artist_name("500024301")`
```Stieglitz, Alfred```

#### 4. get_getty_artist_data

`get_getty_artist_data` consumes an ULAN and returns entire set of data from given ulan as a dictionary.
`get_getty_artist_data("500024301")`

```
{
'@context': 'https://linked.art/ns/v1/linked-art.json',
'_label': 'Stieglitz, Alfred',
'born': { 'id': 'http://vocab.getty.edu/ulan/activity/birth/4000062133',
'timespan': { 'begin_of_the_begin': '1864-01-01T00:00:00',
    'end_of_the_end': '1864-12-31T23:59:59',
    'id': 'http://vocab.getty.edu/ulan/time/birth/4000062133',
    'type': 'TimeSpan' },
'took_place_at': [ { '_label': 'Hoboken',
    'id': 'http://vocab.getty.edu/tgn/7013711-place',
    'type': 'Place' } ],
...
```

The dictionary is parsed from [this json file on ULAN](http://vocab.getty.edu/ulan/500024301.json)

#### 5. get_getty_artist_sex

`get_getty_artist_name` consumes an ULAN and returns just the artist's sex as a string, available sexes are '
male', 'female' and None if unknown.
`get_getty_artist_sex("500024301")`

`male`

#### 6. get_getty_artist_birth_year

`get_getty_artist_birth_year` consumes an ULAN and returns artist birth year as an integer

`get_getty_artist_birth_year("500024301")`

`1864`


### WikiData Functions
#### 1. get_wiki_artist_data
`get_wiki_artist_data` consumes a WikiData ID like `Q948598` and returns the entire data set from WikiData.

#### 2. get_wiki_artist_name
`get_wiki_artist_data` consumes a WikiData ID and returns the artist name in 'First Last' format, as seen on WikiData.

`get_wiki_artist_name("Q948598")`

`Albert Pinkham Ryder`

#### 3. get_wiki_artist_sex
`get_wiki_artist_sex` consumes a WikiData ID and returns just the artist's gender and sex as a string, available sexes are '
male', 'female' and None if unknown.

`get_wiki_artist_sex("Q948598")`

`male`

#### 4. get_wiki_artist_birth_year
`get_wiki_artist_birth_year` consumes a WikiData ID and returns just the artist's birth year as an integer.

`get_wiki_artist_birth_year("Q948598")`

`1864`

### Example View

```python
from django.views.generic.base import View
from django.http import HttpResponse
from artist_getter import *
import json


class GetUlanView(View):
    def get(self, request):
        artist_ulan = json.dumps(get_getty_ulan(u"Stieglitz, Alfred"))

        return HttpResponse(artist_ulan, content_type="application/json")
```

### Build & Release

For maintainers of this package only.

Download setuptools:
`pip install --upgrade setuptools`

First, bump up the release version in setup.py.

Run this command to build package:
`python -m build`

Run checks before releasing to PyPI:
`twine check --strict dist/*`

Release to PYPI by:
`twine upload --skip-existing dist/*`

Push everything and create a release on GitHub.

#### Test unreleased package locally
`pip uninstall artist-getter`

Change to the dist directory and install the newest distribution by calling:
`pip install artist_getter-$NEWEST_EDITION`
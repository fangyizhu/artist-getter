from artist_getter.__init__ import *

assert '500024301' == get_getty_ulan("Stieglitz, Alfred")[0]['ulan']
assert 'Stieglitz, Alfred' == get_getty_artist_name('500024301')
assert 'male' == get_getty_artist_sex('500024301')
assert 'relationship_type' in get_getty_relationship('500024301')[0]
assert type(get_getty_artist_data('500024301')) is dict
assert 'Albert Pinkham Ryder' == get_wiki_artist_data('Q948598').label
assert 'male' == get_wiki_artist_sex("Q948598")